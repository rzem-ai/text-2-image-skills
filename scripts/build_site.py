#!/usr/bin/env python3
"""Build the static catalogue and matching skill downloads for GitHub Pages."""

import argparse
import hashlib
import html
import json
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from collections import Counter
from pathlib import Path

import package_skills


ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = 'https://github.com/rzem-ai/text-2-image-skills'


def family_for(name):
    for prefix, label in (('nano-banana', 'Google'), ('gpt-image', 'OpenAI'),
                          ('flux-', 'Black Forest Labs'), ('qwen-', 'Qwen'),
                          ('moss-', 'OpenMOSS')):
        if name.startswith(prefix):
            return label
    if name in {'sdxl', 'juggernaut-xl', 'pony-diffusion-xl'}:
        return 'SDXL family'
    return 'Independent'


def skill_row(entry, description, commit):
    name = entry['directory']
    title = entry['display_name']
    family = family_for(name)
    command = f'npx skills add rzem-ai/text-2-image-skills --skill {name}'
    summary = description.split('. ')[0].rstrip('.') + '.'
    search = ' '.join((name, title, family, description, entry['model_identity'])).lower()
    escape = html.escape
    guide = f'{REPOSITORY}/blob/{commit}/{name}/SKILL.md'
    return f'''<article class="skill-row" id="{escape(name)}" data-family="{escape(family)}" data-search="{escape(search)}">
  <div class="skill-main">
    <div class="row-heading"><h3>{escape(title)}</h3><span class="skill-family">{escape(family)}</span></div>
    <p class="skill-description">{escape(summary)}</p>
    <details class="skill-install"><summary>Install command</summary><code>{escape(command)}</code></details>
  </div>
  <div class="skill-actions">
    <a href="{escape(guide)}" aria-label="Read the {escape(title)} guide">Read guide</a>
    <a href="downloads/{escape(name)}.skill" download aria-label="Download {escape(title)} skill">Download</a>
    <button type="button" class="copy-button" data-copy="{escape(command)}" data-label="{escape(title)}" aria-label="Copy install command for {escape(title)}" hidden>Copy install</button>
  </div>
</article>'''


def build_site(output, commit=None):
    output = Path(output)
    if output.exists():
        raise ValueError(f'Site output already exists: {output}; choose a fresh directory')
    if commit is None:
        commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    if not re.fullmatch(r'[0-9a-f]{40}', commit):
        raise ValueError('Site provenance requires a full Git commit SHA')
    catalog = package_skills.load_catalog()
    entries = catalog['skills']
    validated = [package_skills.validate(entry) for entry in entries]
    rows = []
    for entry, (directory, _) in zip(entries, validated):
        match = re.search(r'^description: ("[^\n]*")$', (directory / 'SKILL.md').read_text(), re.M)
        rows.append(skill_row(entry, json.loads(match[1]), commit))
    counts = Counter(family_for(entry['directory']) for entry in entries)
    filters = [f'<button type="button" data-family-filter="all" aria-pressed="true">All models ({len(entries)})</button>']
    filters.extend(f'<button type="button" data-family-filter="{html.escape(family)}" aria-pressed="false">{html.escape(family)} ({count})</button>'
                   for family, count in sorted(counts.items()))
    page = (ROOT / 'site/index.html').read_text()
    substitutions = {'SKILL_COUNT': str(len(entries)), 'FAMILY_FILTERS': '\n'.join(filters),
                     'MODEL_ROWS': '\n'.join(rows), 'SOURCE_COMMIT': commit, 'SHORT_COMMIT': commit[:7]}
    for key, value in substitutions.items():
        page = page.replace(f'<!-- {key} -->', value)
    if re.search(r'<!-- [A-Z_]+ -->', page):
        raise ValueError('Site contains an unresolved build marker')
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.site-', dir=output.parent) as temporary:
        stage = Path(temporary) / 'site'
        stage.mkdir()
        assets = ROOT / 'site/assets'
        if any(path.is_symlink() for path in assets.rglob('*')):
            raise ValueError('Site assets cannot contain symlinks')
        shutil.copytree(assets, stage / 'assets')
        (stage / 'index.html').write_text(page)
        (stage / '.nojekyll').touch()
        (stage / 'catalog.json').write_bytes((ROOT / 'catalog.json').read_bytes())
        (stage / 'build.json').write_text(json.dumps({'source_commit': commit, 'skill_count': len(entries)}, indent=2) + '\n')
        downloads = stage / 'downloads'
        downloads.mkdir()
        archives = [package_skills.build(directory, files, output=downloads) for directory, files in validated]
        (downloads / 'catalog.json').write_bytes((ROOT / 'catalog.json').read_bytes())
        bundle = downloads / 'text-2-image-skills.zip'
        bundle_files = [(path.name, path) for path in archives]
        bundle_files.extend((name, ROOT / name) for name in ('catalog.json', 'README.md', 'LICENSE'))
        with zipfile.ZipFile(bundle, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
            for name, path in sorted(bundle_files):
                info = zipfile.ZipInfo(name, (2026, 10, 19, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, path.read_bytes())
        with zipfile.ZipFile(bundle) as archive:
            if archive.testzip():
                raise ValueError('Combined site download failed ZIP verification')
            for name, path in bundle_files:
                if archive.read(name) != path.read_bytes():
                    raise ValueError(f'Combined site download mismatch: {name}')
        checksum_lines = [f'{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.name}'
                          for path in sorted(downloads.iterdir())]
        (downloads / 'SHA256SUMS').write_text('\n'.join(checksum_lines) + '\n')
        stage.replace(output)
    print(f'Built catalogue, {len(entries)} individual downloads and combined ZIP in {output}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'dist/site')
    args = parser.parse_args()
    build_site(args.output)


if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, OSError, subprocess.CalledProcessError) as error:
        print(f'Error: {error}', file=sys.stderr)
        sys.exit(1)
