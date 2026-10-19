# GPT Image 2.5: identity and constraints

Reference check: 2026-10-19. Bracketed evidence labels resolve in [sources.md](sources.md). Tables mix documented facts with explicitly labelled author suggestions. Settings are context for writing prompts, not instructions to execute a generation workflow.

## Model identity

GPT Image 2.5 is a family with two documented variants, not a verified bare gpt-image-2.5 API identifier. Flare prioritises speed; Sunburst prioritises quality. Both support image generation, editing and transparent backgrounds. A family-level prompt can be written before choosing a variant; identify that choice in any settings notes. [O1, O2]

## Prompt-relevant settings

| Concern | Prompt-writing consequence |
| --- | --- |
| Quality | auto, low, medium, high, xhigh or max; higher values aren't a universal improvement. [O1] |
| Size | Edges <=3840 and divisible by 16; ratio <=3:1; area 655360-8294400. Output above 3686400 pixels is experimental. [O1] |
| Transparency | Request transparent output with PNG/WebP outside the visual prompt; inspect real alpha if subsequently rendered. [O1] |
| Reference fidelity | Explicitly name the features to preserve; repeated edits can still drift. |
| Syntax | No dedicated negative-prompt field or SDXL-style numerical prompt weights is established here. |

## What wording cannot guarantee

A prompt cannot attach an absent reference, enable a disabled tool, force factual correctness, guarantee exact typography or prove transparency. Keep reference identity, settings and file requirements separate from visible content. If a user requires exact geometry or pixel-identical preservation, describe that need honestly rather than claiming stronger model guarantees.

Use the user's selected model and installed frontend as the scope of any refinement. New fine-tunes and hosted wrappers can change behaviour; a version-specific parameter should not be promoted into a family-wide rule.
