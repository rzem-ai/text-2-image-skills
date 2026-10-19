# SDXL: identity and constraints

Reference check: 2026-10-19. Bracketed evidence labels resolve in [sources.md](sources.md). Tables mix documented facts with explicitly labelled author suggestions. Settings are context for writing prompts, not instructions to execute a generation workflow.

## Model identity

SDXL 1.0 base is the reference here. Its two text encoders, optional refiner and image-to-image pipelines differ from newer instruction editors. The base can be used alone; the refiner is optional. SDXL Turbo, Lightning, LCM and fine-tunes can require different settings and prompting. Don't silently treat those as the base checkpoint. [S1, S2]

## Prompt-relevant settings

| Concern | Prompt-writing consequence |
| --- | --- |
| Canvas | Use around 1024x1024 as a base starting point; 1216x832 and 832x1216 are practical landscape/portrait suggestions, not universal requirements. |
| Author baseline | For a non-distilled base workflow, 25-40 steps and CFG around 5-7 are reasonable experiments; these are author suggestions, not fixed model limits. |
| Prompt length | CLIP context is limited; different frontends truncate or chunk long prompts differently. Put essentials first. [S2] |
| Negatives | A separate negative prompt is supported by the pipeline. Start focused. [S2] |
| Syntax | Parenthesis weights, BREAK and LoRA tags belong to particular frontends, not universal SDXL syntax. |

## What wording cannot guarantee

A prompt cannot attach an absent reference, enable a disabled tool, force factual correctness, guarantee exact typography or prove transparency. Keep reference identity, settings and file requirements separate from visible content. If a user requires exact geometry or pixel-identical preservation, describe that need honestly rather than claiming stronger model guarantees.

Use the user's selected model and installed frontend as the scope of any refinement. New fine-tunes and hosted wrappers can change behaviour; a version-specific parameter should not be promoted into a family-wide rule.
