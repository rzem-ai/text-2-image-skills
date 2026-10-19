#!/usr/bin/env python3
"""Build versioned release assets without contacting GitHub or publishing anything."""

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

import package_skills


TAG = re.compile(
    r'v(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)'
    r'(?:-([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?'
)


def validate_tag(tag):
    """Accept vMAJOR.MINOR.PATCH with an optional SemVer prerelease suffix."""
    match = TAG.fullmatch(tag)
    if not match:
        raise ValueError('Use vMAJOR.MINOR.PATCH or a prerelease such as v1.1.0-rc.1')
    prerelease = match[4]
    if prerelease and any(p.isdigit() and len(p) > 1 and p.startswith('0')
                          for p in prerelease.split('.')):
        raise ValueError('Numeric prerelease identifiers cannot contain leading zeroes')
    return prerelease is not None


def build_release(tag, commit, output):
    validate_tag(tag)
    if not re.fullmatch(r'[0-9a-f]{40}', commit):
        raise ValueError('Source commit must be a full Git SHA-1')
    root = package_skills.ROOT
    output = Path(output)
    if output.exists():
        raise ValueError(f'Release output already exists: {output}; use a fresh output directory')
    catalog = package_skills.load_catalog()
    validated = [package_skills.validate(entry) for entry in catalog['skills']]
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.release-', dir=output.parent) as temporary:
        stage = Path(temporary) / 'assets'
        stage.mkdir()
        for directory, files in validated:
            package_skills.build(directory, files, output=stage)
        (stage / 'catalog.json').write_bytes((root / 'catalog.json').read_bytes())
        metadata = {
            'schema_version': 1,
            'tag': tag,
            'source_commit': commit,
            'reference_date': catalog['reference_date'],
            'skill_count': len(validated),
            'skills': [{'name': entry['directory'], 'asset': entry['directory'] + '.skill'}
                       for entry in catalog['skills']],
        }
        (stage / 'release.json').write_text(json.dumps(metadata, indent=2) + '\n')
        bundle_name = f'text-2-image-skills-{tag}'
        bundle = stage / f'{bundle_name}.zip'
        bundle_files = [root / name for name in ('README.md', 'LICENSE', 'catalog.json')]
        bundle_files.extend(path for _, files in validated for path in files)
        with zipfile.ZipFile(bundle, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
            for path in sorted(bundle_files):
                name = bundle_name + '/' + path.relative_to(root).as_posix()
                info = zipfile.ZipInfo(name, (2026, 10, 19, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, path.read_bytes())
        with zipfile.ZipFile(bundle) as archive:
            if archive.testzip() or len(archive.namelist()) != len(bundle_files):
                raise ValueError('Combined ZIP failed integrity verification')
            for path in bundle_files:
                name = bundle_name + '/' + path.relative_to(root).as_posix()
                if archive.read(name) != path.read_bytes():
                    raise ValueError(f'Combined ZIP content mismatch: {name}')
        checksums = [f'{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.name}'
                     for path in sorted(stage.iterdir())]
        (stage / 'SHA256SUMS').write_text('\n'.join(checksums) + '\n')
        stage.replace(output)
    print(f'Built {len(validated)} individual skills, combined ZIP, catalog, metadata and checksums in {output}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tag', required=True)
    parser.add_argument('--check-tag', action='store_true', help='Validate tag only; build no assets')
    parser.add_argument('--output', type=Path, default=package_skills.ROOT / 'dist' / 'release')
    args = parser.parse_args()
    prerelease = validate_tag(args.tag)
    if args.check_tag:
        if os.environ.get('GITHUB_OUTPUT'):
            with open(os.environ['GITHUB_OUTPUT'], 'a') as stream:
                stream.write(f'tag={args.tag}\nprerelease={str(prerelease).lower()}\n')
        print(f'{args.tag}: {"prerelease" if prerelease else "stable release"}')
        return
    commit = subprocess.check_output(
        ['git', 'rev-parse', 'HEAD'], cwd=package_skills.ROOT, text=True,
    ).strip()
    build_release(args.tag, commit, args.output)


if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, OSError, subprocess.CalledProcessError) as error:
        print(f'Error: {error}', file=sys.stderr)
        sys.exit(1)
