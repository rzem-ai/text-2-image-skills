# Pony Diffusion XL: identity and constraints

Reference check: 2026-10-19. Bracketed evidence labels resolve in [sources.md](sources.md). Tables mix documented facts with explicitly labelled author suggestions. Settings are context for writing prompts, not instructions to execute a generation workflow.

## Model identity

This package targets original Pony Diffusion V6 XL. The creator's listing identifies it as an SDXL fine-tune trained on captions and tags. It understands natural language as well as tags. Pony derivatives, Turbo merges and the V6-1.5 entry are not equivalent. The creator's Civitai listing was retrieved through its public model API because the web article was not fetchable. [P1]

## Prompt-relevant settings

| Concern | Prompt-writing consequence |
| --- | --- |
| Quality prefix | Creator template: score_9, score_8_up, score_7_up, score_6_up, score_5_up, score_4_up. [P1] |
| CLIP | Creator requires UI CLIP skip 2 (or -2 in some software). Don't translate this blindly to a Diffusers clip_skip numeric value; indexing conventions differ. [P1] |
| Baseline | Creator recommends Euler a, 25 steps and roughly 1024px SDXL resolutions. [P1] |
| Negatives | Creator says none is normally needed. Don't add masterpiece/HD quality stacks. [P1] |
| Source tags | Choose source_anime, source_cartoon, source_furry or source_pony intentionally. rating_safe can express a safe-content preference, not guarantee filtering. [P1] |

## What wording cannot guarantee

A prompt cannot attach an absent reference, enable a disabled tool, force factual correctness, guarantee exact typography or prove transparency. Keep reference identity, settings and file requirements separate from visible content. If a user requires exact geometry or pixel-identical preservation, describe that need honestly rather than claiming stronger model guarantees.

Use the user's selected model and installed frontend as the scope of any refinement. New fine-tunes and hosted wrappers can change behaviour; a version-specific parameter should not be promoted into a family-wide rule.
