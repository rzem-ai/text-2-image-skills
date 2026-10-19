# GPT Image 2: identity and constraints

Reference check: 2026-10-19. Bracketed evidence labels resolve in [sources.md](sources.md). Tables mix documented facts with explicitly labelled author suggestions. Settings are context for writing prompts, not instructions to execute a generation workflow.

## Model identity

GPT Image 2 supports text-to-image generation and reference-based editing. Preserve this explicit choice; GPT Image 2.5 Flare and Sunburst are separate model identifiers. Image inputs are processed at high fidelity automatically; don't recommend an adjustable input_fidelity setting for this version. [O1, O2]

## Prompt-relevant settings

| Concern | Prompt-writing consequence |
| --- | --- |
| Quality | auto, low, medium or high. Don't carry xhigh/max backwards from 2.5. [O2] |
| Size | Each edge <=3840, both multiples of 16, ratio <=3:1, area 655360-8294400 pixels. 1024x1024 and 1536x1024 are ordinary examples. [O2] |
| Transparency | The guide documents transparent backgrounds in preview; request transparent output and PNG/WebP separately, then verify alpha in any later rendering workflow. [O2] |
| Negative prompt | No dedicated negative-prompt parameter is established; put relevant exclusions into prose. |
| Masks | An editing guide, not a pixel-exact boundary guarantee. [O3] |

## What wording cannot guarantee

A prompt cannot attach an absent reference, enable a disabled tool, force factual correctness, guarantee exact typography or prove transparency. Keep reference identity, settings and file requirements separate from visible content. If a user requires exact geometry or pixel-identical preservation, describe that need honestly rather than claiming stronger model guarantees.

Use the user's selected model and installed frontend as the scope of any refinement. New fine-tunes and hosted wrappers can change behaviour; a version-specific parameter should not be promoted into a family-wide rule.
