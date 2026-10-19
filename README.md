# Image prompt skills

Fifteen independently packageable skills for writing, refining and troubleshooting text-to-image prompts and image-to-image briefs. They contain embedded reference notes and original prompt examples. They do not run image generation, install models or call provider APIs.

Reference documentation checked on **2026-10-19**. Technical facts are scoped to the named model/version. Prompt examples and repair advice are original recommendations, not claims of measured model performance.

## Install with skills.sh

This repository follows the [Agent Skills format](https://agentskills.io/specification) and works with the [skills CLI](https://github.com/vercel-labs/skills). Each model directory is discovered as a separate skill; its embedded references are installed with it. No npm publication, repository-level skill manifest or directory rearrangement is required.

Run the installer from the project where you want to use the skills. The current CLI requires Node.js 22.20 or later; Node isn't required to read or use the installed prompt guidance.

Choose skills and target agents interactively:

```sh
npx skills add rzem-ai/text-2-image-skills
```

List the available skills without installing:

```sh
npx skills add rzem-ai/text-2-image-skills --list
```

Install one skill for Codex, Claude Code or Cursor:

```sh
npx skills add rzem-ai/text-2-image-skills --skill nano-banana --agent codex --yes
npx skills add rzem-ai/text-2-image-skills --skill nano-banana --agent claude-code --yes
npx skills add rzem-ai/text-2-image-skills --skill nano-banana --agent cursor --yes
```

Install the entire collection for selected agents:

```sh
npx skills add rzem-ai/text-2-image-skills --skill '*' --agent codex claude-code cursor --yes
```

Project installation is the default. Add `--global` for a user-wide installation, or `--copy` to request copies instead of the default shared-directory/symlink layout. Use any skill directory name from the table below with `--skill`.

For a specific tagged release, use the full GitHub tree URL with the tag in place of the branch:

```sh
npx skills add https://github.com/rzem-ai/text-2-image-skills/tree/v1.0.0 --skill nano-banana --agent codex --yes
```

Replace `v1.0.0` with an existing tag. CLI installs read the Git repository; individual `.skill` downloads remain available separately as GitHub Release assets. A release archive isn't needed for normal repository installation.

According to the [skills.sh FAQ](https://skills.sh/docs/faq), directory/leaderboard listings are driven by installation telemetry. Compatibility doesn't itself register a listing or guarantee indexing. Set `DISABLE_TELEMETRY=1` if you want to opt out; this repository's compatibility tests always do so.

## Packages

| Requested model | Skill directory | Identity and scope |
| --- | --- | --- |
| Nano Banana | [nano-banana](nano-banana/SKILL.md) | Google Gemini 2.5 Flash Image (`gemini-2.5-flash-image`) |
| Nano Banana Pro | [nano-banana-pro](nano-banana-pro/SKILL.md) | Google Gemini 3 Pro Image (`gemini-3-pro-image`) |
| Nano Banana 2 | [nano-banana-2](nano-banana-2/SKILL.md) | Google Gemini 3.1 Flash Image (`gemini-3.1-flash-image`) |
| GPT Image 2 | [gpt-image-2](gpt-image-2/SKILL.md) | OpenAI GPT Image 2 (`gpt-image-2`) |
| GPT Image 2.5 | [gpt-image-2-5](gpt-image-2-5/SKILL.md) | OpenAI GPT Image 2.5 Flare (`gpt-image-2.5-flare`) or Sunburst (`gpt-image-2.5-sunburst`) |
| FLUX.1 Dev | [flux-1-dev](flux-1-dev/SKILL.md) | Black Forest Labs FLUX.1 [dev] (`black-forest-labs/FLUX.1-dev`) |
| FLUX.1 Pro | [flux-1-pro](flux-1-pro/SKILL.md) | Black Forest Labs original FLUX.1 [pro] (legacy hosted model) |
| FLUX.2 Dev | [flux-2-dev](flux-2-dev/SKILL.md) | Black Forest Labs FLUX.2 [dev] (`black-forest-labs/FLUX.2-dev`) |
| FLUX.2 Pro | [flux-2-pro](flux-2-pro/SKILL.md) | Black Forest Labs FLUX.2 [pro] (`flux-2-pro`) |
| FLUX.2 Klein 9B | [flux-2-klein-9b](flux-2-klein-9b/SKILL.md) | Black Forest Labs distilled FLUX.2 [klein] 9B (`black-forest-labs/FLUX.2-klein-9B`) |
| SDXL | [sdxl](sdxl/SKILL.md) | Stability AI Stable Diffusion XL 1.0 base (`stabilityai/stable-diffusion-xl-base-1.0`) |
| Juggernaut XL | [juggernaut-xl](juggernaut-xl/SKILL.md) | RunDiffusion Juggernaut XL, an SDXL fine-tune family; v9 is the documented baseline here |
| Pony Diffusion XL | [pony-diffusion-xl](pony-diffusion-xl/SKILL.md) | PurpleSmartAI/AstraliteHeart Pony Diffusion V6 XL; use the V6 checkpoint, not V6-1.5 or Turbo merges |
| Qwen Image 2.1 | [qwen-image-2-1](qwen-image-2-1/SKILL.md) | Qwen-Image-2.1 (`Qwen/Qwen-Image-2.1`); hosted Pro/Turbo variants have separate contracts |
| Qwen Image 3 | [qwen-image-3](qwen-image-3/SKILL.md) | Qwen-Image-3.0: hosted `qwen-image-3.0` and `qwen-image-3.0-pro` |

## Each package

```text
model-name/
  SKILL.md
  agents/openai.yaml
  references/
    capabilities.md
    prompting.md
    editing.md
    sources.md
```

Every reference is inside its package. No symlinks, shared parent references, external skill dependencies, API keys or runtime libraries are required for prompt writing. Source URLs provide provenance and a refresh path; the useful guidance is embedded locally.

For a normal request, select the skill for the model and provide the image idea or existing prompt. For a refinement from an image, supply that image and the desired change. The skill returns a fenced copy-ready prompt, plus a separate negative prompt only when supported and useful.

## Build or inspect archives

From this directory:

```sh
python3 scripts/package_skills.py --check
python3 scripts/package_skills.py
python3 scripts/package_skills.py --only nano-banana
```

The builder validates all selected directories before writing archives. Each `dist/<name>.skill` is a ZIP file containing only that skill's top-level directory. A `.skill` suffix does not guarantee support in every client; the directory is the portable source package. The standard-library builder also verifies byte-for-byte archive contents and emits SHA-256 sums. Nothing is installed automatically.

## CI and tagged releases

Pull requests and pushes to `main` run the release-tooling tests, validate every skill, build each `.skill` archive and verify its SHA-256 checksum. A separate job uses the pinned skills CLI to discover all 15 skills, install them for Codex, Claude Code and Cursor in temporary projects, and compare the installed files to the source. The resulting packages are also saved as a GitHub Actions build artefact for 14 days. Tagged releases run the same CLI compatibility check before building release assets.

The release workflow runs when a collection-wide version tag is pushed. Once these workflow files are committed and pushed, create a release from the intended commit:

```sh
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0
```

Tags must use `vMAJOR.MINOR.PATCH`, optionally followed by a SemVer prerelease suffix such as `v1.1.0-rc.1`. Leading zeroes in version numbers and numeric prerelease identifiers are rejected. Build metadata suffixes (`+...`) aren't accepted. Prerelease tags are automatically marked as prereleases. Version numbers refer to this skill collection, independently of the model versions in directory names.

Every successful release has these **19 downloadable assets**:

- All 15 skills attached individually as `<skill-name>.skill`, each containing its own directory and embedded references.
- `text-2-image-skills-<tag>.zip`, containing all 15 source skill directories plus the README, licence and catalogue.
- `catalog.json` and `release.json`, recording the model catalogue, version tag and source commit.
- `SHA256SUMS`, covering every other attached asset.

The workflow builds the tagged source, tests and verifies its assets, creates a draft with automatically generated release notes, uploads the individual files, then publishes. It uses the repository's built-in `GITHUB_TOKEN`; no personal access token or additional secret is required. Write permission is confined to the publishing job. Third-party action references are pinned to verified commit SHAs.

If an upload fails, the release remains a draft. Rerun the failed workflow to replace the draft assets and publish it. An already published release is never overwritten by the script; use a new version tag for changes. The Actions page also provides a manual **Tagged release** run with an existing tag, useful for retrying a missed trigger. The tag must already exist remotely and contain the release scripts.

To build the same assets locally without publishing:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/build_release.py --tag v1.0.0
```

The builder creates `dist/release/` and refuses to overwrite an existing output directory. For another local preview, pass a fresh path using `--output`. Generated assets remain ignored by Git. Finder `.DS_Store` files are ignored by both Git and the packager.

Verify a downloaded release by placing the files together and running:

```sh
sha256sum --check SHA256SUMS
```

On macOS, `shasum -a 256 --check SHA256SUMS` is an alternative.

The workflow follows GitHub's [draft-first publication guidance](https://docs.github.com/en/code-security/concepts/supply-chain-security/immutable-releases) and uses the documented [release creation](https://cli.github.com/manual/gh_release_create) and [publication](https://cli.github.com/manual/gh_release_edit) commands. It doesn't change the repository's release-immutability or tag-protection settings.

## Test installer compatibility locally

The npm manifest and lockfile are development tooling only. They don't make the skill packages depend on Node.js or npm.

```sh
npm ci --ignore-scripts
npm run test:skills
```

The test uses `skills@1.7.4`, disables telemetry, and checks full-collection copy installation plus a selected-skill installation using the default layout. Every installed entry point, embedded reference and agent metadata file must match its source. Installs are project-scoped inside temporary directories and removed afterwards.

The top-level model folders are intentional. Don't add an umbrella `SKILL.md` at the repository root: normal CLI discovery can treat that as a single skill and stop before finding the individual packages. The compatibility job catches this regression. See the CLI's [creation and discovery documentation](https://github.com/vercel-labs/skills/blob/main/docs/creating-skills.md).

## Important identity distinctions

- Nano Banana, Pro and 2 map to Gemini 2.5 Flash Image, Gemini 3 Pro Image and Gemini 3.1 Flash Image respectively. Later Nano Banana releases aren't substituted.
- GPT Image 2.5 covers Flare and Sunburst within the requested single model-family directory.
- Original FLUX.1 Pro remains a legacy prompt-writing package. Its original endpoint wasn't present in BFL's current OpenAPI schema; current provider access isn't assumed.
- Klein 9B means the distilled model. Base, 4B, KV and moving preview variants aren't silently substituted.
- Juggernaut XL uses v9 as an explicitly documented baseline while preserving a supplied XL version. Pony targets original V6 XL.
- Qwen 3 means Qwen-Image-3.0 in this collection. Qwen3 language models and Qwen3-VL aren't image generators by that name. Qwen 2.1 RGBA and reference limits aren't carried forward into 3.0.

## Validation scope

The repository packaging checks cover expected packages, frontmatter, metadata, required embedded files, internal links, package isolation and archive integrity. They do not run models or verify the visual quality of prompt examples. The source notes record where model-specific claims came from.
