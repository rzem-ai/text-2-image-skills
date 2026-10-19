# FLUX.1 Dev: identity and constraints

Reference check: 2026-10-19. Bracketed evidence labels resolve in [sources.md](sources.md). Tables mix documented facts with explicitly labelled author suggestions. Settings are context for writing prompts, not instructions to execute a generation workflow.

## Model identity

FLUX.1 Dev is the original open-weight text-to-image model. Its base text-to-image pipeline is not FLUX.1 Kontext and does not become an instruction editor merely because a prompt says to change something. An image-to-image pipeline can condition generation on a source image; Fill, Redux and Kontext are separate models or workflows. [F1, F2]

## Prompt-relevant settings

| Concern | Prompt-writing consequence |
| --- | --- |
| Reference baseline | The model-card example uses 1024x1024, 50 steps, guidance 3.5 and max_sequence_length 512. These are runtime context, not prompt tokens. [F1] |
| Guidance | FLUX distilled guidance is not interchangeable with SDXL CFG. |
| Text | Prefer connected natural language; don't assume AUTOMATIC1111 weighting or LoRA syntax is parsed. |
| Exclusions | Use positive scene specification; a conventional negative branch is not a baseline capability to assume. |
| I2I | Identify the actual image-to-image workflow before giving strength or mask advice. [F2] |

## What wording cannot guarantee

A prompt cannot attach an absent reference, enable a disabled tool, force factual correctness, guarantee exact typography or prove transparency. Keep reference identity, settings and file requirements separate from visible content. If a user requires exact geometry or pixel-identical preservation, describe that need honestly rather than claiming stronger model guarantees.

Use the user's selected model and installed frontend as the scope of any refinement. New fine-tunes and hosted wrappers can change behaviour; a version-specific parameter should not be promoted into a family-wide rule.
