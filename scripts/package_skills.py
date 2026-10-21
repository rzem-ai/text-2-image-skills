#!/usr/bin/env python3
"""Validate standalone prompt skills and build deterministic ZIP-format .skill files."""

import argparse
import hashlib
import json
import re
import sys
import tempfile
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    'SKILL.md', 'agents/openai.yaml', 'references/capabilities.md',
    'references/prompting.md', 'references/editing.md', 'references/sources.md',
)


def fail(message):
    raise ValueError(message)


def validate(entry):
    name = entry['directory']
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) > 64:
        fail(f'Invalid package name: {name}')
    directory = ROOT / name
    if not directory.is_dir() or directory.is_symlink():
        fail(f'{name}: missing directory or symlinked package')
    for relative in REQUIRED:
        path = directory / relative
        if not path.is_file() or not path.read_text().strip():
            fail(f'{name}: missing or empty {relative}')
    text = (directory / 'SKILL.md').read_text()
    front = re.match(r'\A---\nname: ([a-z0-9-]+)\ndescription: ("[^\n]*")\n---\n', text)
    if not front or front[1] != name:
        fail(f'{name}: invalid frontmatter or directory/name mismatch')
    # This collection deliberately uses the JSON-compatible YAML string subset.
    description = json.loads(front[2])
    if not description or len(description) > 1024:
        fail(f'{name}: empty or excessive description')
    ui = (directory / 'agents/openai.yaml').read_text().splitlines()
    if not ui or ui[0] != 'interface:':
        fail(f'{name}: missing interface metadata')
    fields = {}
    for line in ui[1:]:
        match = re.fullmatch(r'  (display_name|short_description): (".*")', line)
        if not match or match[1] in fields:
            fail(f'{name}: invalid or duplicate UI metadata')
        fields[match[1]] = json.loads(match[2])
    if set(fields) != {'display_name', 'short_description'}:
        fail(f'{name}: incomplete UI metadata')
    if not 25 <= len(fields['short_description']) <= 64:
        fail(f'{name}: short description outside 25-64 characters')

    files = []
    for path in sorted(directory.rglob('*')):
        if path.is_symlink():
            fail(f'{name}: symlinks are not portable: {path.relative_to(directory)}')
        if not path.is_file():
            continue
        if path.name == '.DS_Store':
            continue
        if path.suffix not in {'.md', '.yaml'}:
            fail(f'{name}: unexpected package file: {path.name}')
        files.append(path)
        content = path.read_text()
        if '/Users/' in content or '/private/tmp/' in content:
            fail(f'{name}: machine-specific path in {path.name}')
        if re.search(r'\b(?:TODO|TBD|FIXME)\b|\[INSERT\b', content):
            fail(f'{name}: unfinished scaffold in {path.name}')
        if path.suffix == '.md':
            if sum(line.startswith('```') for line in content.splitlines()) % 2:
                fail(f'{name}: unclosed code fence in {path.name}')
            for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', content):
                if re.match(r'https?://', target) or target.startswith('#'):
                    continue
                destination = (path.parent / target.split('#')[0]).resolve()
                if not destination.is_relative_to(directory.resolve()):
                    fail(f'{name}: reference escapes package: {target}')
                if not destination.is_file():
                    fail(f'{name}: broken embedded reference: {target}')
    source_text = (directory / 'references/sources.md').read_text()
    if not re.search(r'https://', source_text):
        fail(f'{name}: no source provenance')
    return directory, files


def build(directory, files, output=None):
    output = Path(output) if output is not None else ROOT / 'dist'
    output.mkdir(parents=True, exist_ok=True)
    destination = output / f'{directory.name}.skill'
    # Write then verify a temporary archive before publishing it over an old one.
    with tempfile.TemporaryDirectory(prefix='.package-', dir=output) as temporary:
        candidate = Path(temporary) / destination.name
        with zipfile.ZipFile(candidate, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
            for path in files:
                info = zipfile.ZipInfo(path.relative_to(ROOT).as_posix(), (2026, 10, 19, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, path.read_bytes())
        with zipfile.ZipFile(candidate) as archive:
            expected = {path.relative_to(ROOT).as_posix(): path.read_bytes() for path in files}
            if set(archive.namelist()) != set(expected) or archive.testzip():
                fail(f'{directory.name}: archive members or CRC mismatch')
            for name, content in expected.items():
                if archive.read(name) != content:
                    fail(f'{directory.name}: archive content mismatch: {name}')
        candidate.replace(destination)
    return destination


def load_catalog():
    """Read the catalog and check that it matches the independently shipped skills."""
    catalog = json.loads((ROOT / 'catalog.json').read_text())
    entries = catalog['skills']
    names = [entry['directory'] for entry in entries]
    if not names or len(names) != len(set(names)):
        fail('Catalog must contain at least one skill and unique model skill directories')
    discovered = {p.parent.name for p in ROOT.glob('*/SKILL.md')}
    if discovered != set(names):
        fail('Catalog does not match skill directories')
    return catalog


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Validate without creating archives')
    parser.add_argument('--only', help='Validate/package a single directory from catalog.json')
    args = parser.parse_args()
    catalog = load_catalog()
    entries = catalog['skills']
    names = [entry['directory'] for entry in entries]
    if args.only:
        entries = [entry for entry in entries if entry['directory'] == args.only]
        if not entries:
            fail(f'Unknown package: {args.only}')
    validated = [validate(entry) for entry in entries]
    print(f'Validated {len(validated)} self-contained skill package(s).')
    if args.check:
        return
    archives = [build(directory, files) for directory, files in validated]
    # Include every currently built catalog archive, even after --only.
    hashes = []
    for name in sorted(names):
        archive = ROOT / 'dist' / f'{name}.skill'
        if archive.exists():
            hashes.append(f'{hashlib.sha256(archive.read_bytes()).hexdigest()}  {archive.name}')
    (ROOT / 'dist' / 'SHA256SUMS').write_text('\n'.join(hashes) + '\n')
    print(f'Built and byte-verified {len(archives)} archive(s) in {ROOT / "dist"}.')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, OSError, json.JSONDecodeError) as error:
        print(f'Error: {error}', file=sys.stderr)
        sys.exit(1)
