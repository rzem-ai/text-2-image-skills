"""Check that catalogue pages and downloadable packages stay in sync."""

import contextlib
import hashlib
import io
import json
import sys
import tempfile
import unittest
import zipfile
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import build_site


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.local_links = []
        self.rows = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            if attrs['id'] in self.ids:
                raise AssertionError('Duplicate HTML id: ' + attrs['id'])
            self.ids.add(attrs['id'])
        if tag == 'article' and attrs.get('class') == 'skill-row':
            self.rows.append(attrs['id'])
        for key in ('href', 'src'):
            target = attrs.get(key, '')
            if target and not target.startswith(('https://', 'http://')):
                self.local_links.append(target)


class SiteTests(unittest.TestCase):
    def test_catalogue_and_local_links_match_built_files(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / 'site'
            with contextlib.redirect_stdout(io.StringIO()):
                build_site.build_site(output, commit='b' * 40)
            parser = PageParser()
            parser.feed((output / 'index.html').read_text())
            catalog = json.loads((ROOT / 'catalog.json').read_text())
            self.assertEqual(set(parser.rows), {entry['directory'] for entry in catalog['skills']})
            for target in parser.local_links:
                if target.startswith('#'):
                    self.assertIn(target[1:], parser.ids)
                else:
                    self.assertTrue((output / target).exists(), target)
            for line in (output / 'downloads/SHA256SUMS').read_text().splitlines():
                digest, name = line.split('  ')
                self.assertEqual(hashlib.sha256((output / 'downloads' / name).read_bytes()).hexdigest(), digest)
            with zipfile.ZipFile(output / 'downloads/text-2-image-skills.zip') as bundle:
                for entry in catalog['skills']:
                    self.assertEqual(bundle.read(entry['directory'] + '.skill'),
                                     (output / 'downloads' / (entry['directory'] + '.skill')).read_bytes())
            metadata = json.loads((output / 'build.json').read_text())
            self.assertEqual(metadata, {'source_commit': 'b' * 40, 'skill_count': len(catalog['skills'])})

    def test_row_escapes_catalogue_and_frontmatter_text(self):
        entry = {'directory': 'example-model', 'display_name': '<script>alert(1)</script>',
                 'model_identity': 'Example'}
        row = build_site.skill_row(entry, 'Description with "quotes" and <img src=x>.', 'b' * 40)
        self.assertNotIn('<script>', row)
        self.assertNotIn('<img ', row)
        self.assertIn('&lt;script&gt;', row)
        self.assertIn('&quot;quotes&quot;', row)

    def test_existing_output_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / 'site'
            output.mkdir()
            sentinel = output / 'index.html'
            sentinel.write_text('keep this')
            with self.assertRaisesRegex(ValueError, 'already exists'):
                build_site.build_site(output, commit='b' * 40)
            self.assertEqual(sentinel.read_text(), 'keep this')

    def test_invalid_commit_cannot_become_html(self):
        with tempfile.TemporaryDirectory() as temporary:
            with self.assertRaisesRegex(ValueError, 'commit SHA'):
                build_site.build_site(Path(temporary) / 'site', commit='<script>')


if __name__ == '__main__':
    unittest.main()
