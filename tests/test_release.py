"""Exercise release contents and publication failure paths without accessing GitHub."""

import contextlib
import hashlib
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import build_release
import package_skills


class VersionTests(unittest.TestCase):
    def test_stable_versions(self):
        for tag in ('v0.1.0', 'v1.0.0', 'v12.34.56'):
            with self.subTest(tag=tag):
                self.assertFalse(build_release.validate_tag(tag))

    def test_prereleases(self):
        for tag in ('v1.0.0-rc.1', 'v2.0.0-alpha', 'v2.0.0-beta-1'):
            with self.subTest(tag=tag):
                self.assertTrue(build_release.validate_tag(tag))

    def test_invalid_versions(self):
        for tag in ('1.0.0', 'v1.0', 'v01.0.0', 'v1.0.0-01', 'v1.0.0-',
                    'v1.0.0-rc..1', 'v1.0.0+build', 'v1.0.0\nother=value', '../v1.0.0'):
            with self.subTest(tag=tag), self.assertRaises(ValueError):
                build_release.validate_tag(tag)

    def test_action_outputs_contain_validated_tag_and_prerelease_flag(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / 'outputs'
            process = subprocess.run(
                [sys.executable, str(ROOT / 'scripts/build_release.py'),
                 '--tag', 'v1.0.0-rc.1', '--check-tag'],
                env={**os.environ, 'GITHUB_OUTPUT': str(output)}, capture_output=True, text=True,
            )
            self.assertEqual(process.returncode, 0, process.stderr)
            self.assertEqual(output.read_text(), 'tag=v1.0.0-rc.1\nprerelease=true\n')


class BuildTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / 'source'
        self.root.mkdir()
        for name in ('README.md', 'LICENSE', 'catalog.json'):
            shutil.copyfile(ROOT / name, self.root / name)
        self.catalog = json.loads((self.root / 'catalog.json').read_text())
        for entry in self.catalog['skills']:
            shutil.copytree(ROOT / entry['directory'], self.root / entry['directory'],
                            ignore=shutil.ignore_patterns('__pycache__'))
        self.root_patch = patch.object(package_skills, 'ROOT', self.root)
        self.root_patch.start()
        self.addCleanup(self.root_patch.stop)

    def build(self, name='release'):
        output = Path(self.temporary.name) / name
        with contextlib.redirect_stdout(io.StringIO()):
            build_release.build_release('v1.0.0', 'a' * 40, output)
        return output

    def test_individual_assets_bundle_metadata_and_checksums(self):
        # macOS metadata must be excluded, even when a user has opened these folders in Finder.
        (self.root / 'nano-banana' / '.DS_Store').write_bytes(b'Finder metadata')
        output = self.build()
        skills = {entry['directory'] + '.skill' for entry in self.catalog['skills']}
        expected = skills | {'catalog.json', 'release.json', 'SHA256SUMS',
                             'text-2-image-skills-v1.0.0.zip'}
        self.assertEqual({p.name for p in output.iterdir()}, expected)
        for entry in self.catalog['skills']:
            with zipfile.ZipFile(output / (entry['directory'] + '.skill')) as archive:
                self.assertIsNone(archive.testzip())
                self.assertEqual(len(archive.namelist()), 6)
                for name in archive.namelist():
                    self.assertTrue(name.startswith(entry['directory'] + '/'))
                    self.assertNotIn('.DS_Store', name)
                    self.assertEqual(archive.read(name), (self.root / name).read_bytes())
        with zipfile.ZipFile(output / 'text-2-image-skills-v1.0.0.zip') as bundle:
            self.assertEqual(len(bundle.namelist()), 15 * 6 + 3)
            self.assertIsNone(bundle.testzip())
        metadata = json.loads((output / 'release.json').read_text())
        self.assertEqual(metadata['source_commit'], 'a' * 40)
        self.assertEqual(metadata['tag'], 'v1.0.0')
        self.assertEqual({item['asset'] for item in metadata['skills']}, skills)
        hashed = set()
        for line in (output / 'SHA256SUMS').read_text().splitlines():
            digest, name = line.split('  ')
            self.assertEqual(hashlib.sha256((output / name).read_bytes()).hexdigest(), digest)
            hashed.add(name)
        self.assertEqual(hashed, expected - {'SHA256SUMS'})

    def test_reproducible_builds(self):
        first, second = self.build('first'), self.build('second')
        self.assertEqual({p.name: p.read_bytes() for p in first.iterdir()},
                         {p.name: p.read_bytes() for p in second.iterdir()})

    def test_existing_output_is_preserved(self):
        output = self.build()
        before = (output / 'SHA256SUMS').read_bytes()
        with self.assertRaisesRegex(ValueError, 'already exists'):
            build_release.build_release('v1.0.0', 'a' * 40, output)
        self.assertEqual((output / 'SHA256SUMS').read_bytes(), before)

    def test_invalid_skill_does_not_publish_partial_assets(self):
        (self.root / 'nano-banana' / 'references' / 'editing.md').unlink()
        with self.assertRaises(ValueError):
            self.build()
        self.assertFalse((Path(self.temporary.name) / 'release').exists())


class PublishTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.assets = self.root / 'assets'
        self.assets.mkdir()
        self.names = [entry['directory'] + '.skill'
                      for entry in json.loads((ROOT / 'catalog.json').read_text())['skills']]
        for name in self.names:
            (self.assets / name).write_text(name)
        (self.assets / 'SHA256SUMS').write_text(''.join(
            f'{hashlib.sha256((self.assets / name).read_bytes()).hexdigest()}  {name}\n'
            for name in self.names))
        binary = self.root / 'bin'
        binary.mkdir()
        self.log = self.root / 'gh.log'
        stub = binary / 'gh'
        stub.write_text('#!' + sys.executable + '\n' + textwrap.dedent('''\
            import json, os, sys
            from pathlib import Path
            args = sys.argv[1:]
            with open(os.environ['GH_TEST_LOG'], 'a') as log:
                log.write(json.dumps(args) + '\\n')
            mode = os.environ['GH_TEST_MODE']
            if args[0] == 'api':
                if mode == 'api-fail': sys.exit(1)
                if mode == 'published': print('v1.0.0\\tfalse')
                if mode == 'draft': print('v1.0.0\\ttrue')
            if args[:2] == ['release', 'upload'] and mode == 'upload-fail': sys.exit(1)
            if args[:2] == ['release', 'create'] and mode == 'create-fail': sys.exit(1)
            '''))
        stub.chmod(0o755)
        self.env = {**os.environ, 'PATH': str(binary) + os.pathsep + os.environ['PATH'],
                    'GH_REPO': 'example/skills', 'GH_TOKEN': 'test-token',
                    'RELEASE_TAG': 'v1.0.0', 'PRERELEASE': 'false', 'GH_TEST_LOG': str(self.log)}

    def publish(self, mode='new', prerelease='false'):
        result = subprocess.run(
            ['bash', str(ROOT / 'scripts/publish_release.sh'), str(self.assets)],
            env={**self.env, 'GH_TEST_MODE': mode, 'PRERELEASE': prerelease},
            capture_output=True, text=True,
        )
        calls = [json.loads(line) for line in self.log.read_text().splitlines()] if self.log.exists() else []
        return result, calls

    def test_new_release_attaches_every_individual_skill_before_publication(self):
        result, calls = self.publish()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual([call[:2] for call in calls[1:]],
                         [['release', 'create'], ['release', 'upload'], ['release', 'edit']])
        self.assertIn('--draft', calls[1])
        self.assertIn('--verify-tag', calls[1])
        for name in self.names:
            self.assertIn(str(self.assets / name), calls[2])
        self.assertIn('--draft=false', calls[3])

    def test_prerelease_flag_survives_draft_publication(self):
        result, calls = self.publish(prerelease='true')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('--prerelease=true', calls[1])
        self.assertIn('--prerelease=true', calls[-1])

    def test_draft_can_be_resumed(self):
        result, calls = self.publish('draft')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual([call[:2] for call in calls[1:]],
                         [['release', 'upload'], ['release', 'edit']])

    def test_failures_do_not_publish(self):
        for mode in ('published', 'api-fail', 'create-fail', 'upload-fail'):
            with self.subTest(mode=mode):
                self.log.unlink(missing_ok=True)
                result, calls = self.publish(mode)
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse(any(call[:2] == ['release', 'edit'] for call in calls))
                if mode in ('published', 'api-fail'):
                    self.assertEqual(len(calls), 1)

    def test_corrupt_asset_stops_before_api_access(self):
        (self.assets / self.names[0]).write_text('tampered')
        result, calls = self.publish()
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(calls, [])


if __name__ == '__main__':
    unittest.main()
