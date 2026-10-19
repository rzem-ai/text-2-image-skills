# Image prompt skills

Fifteen independently packageable skills for writing, refining and troubleshooting text-to-image prompts and image-to-image briefs. They contain embedded reference notes and original prompt examples. They do not run image generation, install models or call provider APIs.

Reference documentation checked on **2026-10-19**. Technical facts are scoped to the named model/version. Prompt examples and repair advice are original recommendations, not claims of measured model performance.

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

## Important identity distinctions

- Nano Banana, Pro and 2 map to Gemini 2.5 Flash Image, Gemini 3 Pro Image and Gemini 3.1 Flash Image respectively. Later Nano Banana releases aren't substituted.
- GPT Image 2.5 covers Flare and Sunburst within the requested single model-family directory.
- Original FLUX.1 Pro remains a legacy prompt-writing package. Its original endpoint wasn't present in BFL's current OpenAPI schema; current provider access isn't assumed.
- Klein 9B means the distilled model. Base, 4B, KV and moving preview variants aren't silently substituted.
- Juggernaut XL uses v9 as an explicitly documented baseline while preserving a supplied XL version. Pony targets original V6 XL.
- Qwen 3 means Qwen-Image-3.0 in this collection. Qwen3 language models and Qwen3-VL aren't image generators by that name. Qwen 2.1 RGBA and reference limits aren't carried forward into 3.0.

## Validation scope

The repository packaging checks cover expected packages, frontmatter, metadata, required embedded files, internal links, package isolation and archive integrity. They do not run models or verify the visual quality of prompt examples. The source notes record where model-specific claims came from.
