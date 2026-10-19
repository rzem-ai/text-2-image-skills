#!/usr/bin/env python3
"""Verify real skills CLI discovery and isolated installations of this collection."""

import argparse
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import package_skills


ROOT = Path(__file__).resolve().parents[1]
ANSI = re.compile(r'\x1b\[[0-?]*[ -/]*[@-~]')


def run_cli(cli, project, *arguments):
    result = subprocess.run(
        ['node', str(cli), 'add', str(ROOT), *arguments], cwd=project,
        env={**os.environ, 'DISABLE_TELEMETRY': '1', 'DO_NOT_TRACK': '1',
             'CI': '1', 'NO_COLOR': '1'},
        capture_output=True, text=True, timeout=120,
    )
    output = ANSI.sub('', result.stdout + result.stderr)
    if result.returncode:
        raise ValueError(f'skills CLI exited with {result.returncode}:\n{output}')
    return output


def verify_install(project, entries, validated):
    expected = {entry['directory'] for entry in entries}
    # In the pinned CLI, Codex and Cursor share the universal .agents directory;
    # Claude Code also receives its own directory. No user/global install is used.
    for prefix in ('.agents/skills', '.claude/skills'):
        base = project / prefix
        discovered = {path.parent.name for path in base.glob('*/SKILL.md')}
        if discovered != expected:
            raise ValueError(f'{prefix}: installed {sorted(discovered)}, expected {sorted(expected)}')
        for directory, files in validated:
            for source in files:
                installed = base / directory.name / source.relative_to(directory)
                if not installed.is_file() or installed.read_bytes() != source.read_bytes():
                    raise ValueError(f'Missing or altered installed file: {installed.relative_to(project)}')


def check(cli):
    if not cli.is_file():
        raise ValueError('Skills CLI is missing. Run npm ci --ignore-scripts first.')
    catalog = package_skills.load_catalog()
    entries = catalog['skills']
    validated = [package_skills.validate(entry) for entry in entries]
    with tempfile.TemporaryDirectory(prefix='skills-compatibility-') as temporary:
        workspace = Path(temporary)
        listed = run_cli(cli, workspace, '--list')
        names = set(re.findall(r'(?m)^[│\s]*([a-z0-9]+(?:-[a-z0-9]+)*)\s*$', listed))
        expected = {entry['directory'] for entry in entries}
        if names != expected:
            raise ValueError(f'Discovery differs from catalog: {sorted(names)} != {sorted(expected)}\n{listed}')
        copied = workspace / 'copy-project'
        copied.mkdir()
        run_cli(cli, copied, '--skill', '*', '--agent', 'codex', 'claude-code', 'cursor',
                '--copy', '--yes')
        verify_install(copied, entries, validated)
        selected = workspace / 'selected-project'
        selected.mkdir()
        entry = entries[0]
        run_cli(cli, selected, '--skill', entry['directory'], '--agent', 'codex',
                'claude-code', 'cursor', '--yes')
        verify_install(selected, [entry], [validated[0]])
    print(f'Skills CLI discovered all {len(entries)} skills; copy and selected/default installs passed.')
    print('Verified every installed SKILL.md, reference and agent metadata file byte for byte.')
    print('All installations were project-scoped in temporary directories; telemetry was disabled.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cli', type=Path, default=ROOT / 'node_modules/skills/bin/cli.mjs')
    args = parser.parse_args()
    check(args.cli.resolve())


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, subprocess.TimeoutExpired) as error:
        print(f'Error: {error}', file=sys.stderr)
        sys.exit(1)
