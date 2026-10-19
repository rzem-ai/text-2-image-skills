# Juggernaut XL: identity and constraints

Reference check: 2026-10-19. Bracketed evidence labels resolve in [sources.md](sources.md). Tables mix documented facts with explicitly labelled author suggestions. Settings are context for writing prompts, not instructions to execute a generation workflow.

## Model identity

Juggernaut XL names a family, not a unique checkpoint. This package uses RunDiffusion/Juggernaut-XL-v9 as its explicit reference while preserving a user's supplied XL release. Juggernaut Pro Flux and Juggernaut Z use different architectures. Don't apply their guidance or assume every XL release has identical defaults. [J1]

## Prompt-relevant settings

| Concern | Prompt-writing consequence |
| --- | --- |
| v9 canvas | 832x1216 portrait or 1216x832 landscape. [J1] |
| v9 baseline | DPM++ 2M Karras, 30-40 steps, CFG 3-7; v9 includes a VAE. Keep these outside the prompt. [J1] |
| Negatives | The current v9 card recommends starting empty and adding specific exclusions when needed. [J1] |
| Medium | Photography is a useful default only when the user's brief calls for it. |
| I2I | Use an SDXL-compatible workflow; this is not a conversational instruction editor. [J2] |

## What wording cannot guarantee

A prompt cannot attach an absent reference, enable a disabled tool, force factual correctness, guarantee exact typography or prove transparency. Keep reference identity, settings and file requirements separate from visible content. If a user requires exact geometry or pixel-identical preservation, describe that need honestly rather than claiming stronger model guarantees.

Use the user's selected model and installed frontend as the scope of any refinement. New fine-tunes and hosted wrappers can change behaviour; a version-specific parameter should not be promoted into a family-wide rule.
