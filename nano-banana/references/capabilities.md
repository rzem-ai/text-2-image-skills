# Nano Banana: identity and constraints

Reference check: 2026-10-19. Bracketed evidence labels resolve in [sources.md](sources.md). Tables mix documented facts with explicitly labelled author suggestions. Settings are context for writing prompts, not instructions to execute a generation workflow.

## Model identity

This package targets the original Nano Banana. Nano Banana Pro, Nano Banana 2 and Nano Banana 2.1 are different models. The stable model identifier is distinct from the deprecated preview identifier. It accepts text and image inputs and can generate and conversationally edit images. The original model does not offer the newer models' Search grounding or thinking capability. [G1]

## Prompt-relevant settings

| Concern | Prompt-writing consequence |
| --- | --- |
| Canvas | Design around roughly 1K output; a square example is 1024 x 1024. Don't promise native 2K or 4K. [G2] |
| References | Google recommends up to three input images for best results. Give each a separate role. [G2] |
| Exclusions | Express exclusions in ordinary language; no SDXL-style negative field or weighting syntax is established here. |
| Transparency | Don't claim that a transparent-looking background proves an alpha channel. |
| Editing | Name the change and essential visual invariants; text alone doesn't supply a reference image. |

## What wording cannot guarantee

A prompt cannot attach an absent reference, enable a disabled tool, force factual correctness, guarantee exact typography or prove transparency. Keep reference identity, settings and file requirements separate from visible content. If a user requires exact geometry or pixel-identical preservation, describe that need honestly rather than claiming stronger model guarantees.

Use the user's selected model and installed frontend as the scope of any refinement. New fine-tunes and hosted wrappers can change behaviour; a version-specific parameter should not be promoted into a family-wide rule.
