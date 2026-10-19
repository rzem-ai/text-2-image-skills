# FLUX.2 Dev: identity and constraints

Reference check: 2026-10-19. Bracketed evidence labels resolve in [sources.md](sources.md). Tables mix documented facts with explicitly labelled author suggestions. Settings are context for writing prompts, not instructions to execute a generation workflow.

## Model identity

FLUX.2 Dev supports generation and multi-reference image editing using Flux2Pipeline. It differs from FLUX.1 Dev and the smaller Klein models. BFL's published model-card example uses 50 steps, guidance 4, with 28 steps noted as a possible trade-off. These are contextual baselines, not words to insert into an image prompt. [F1]

## Prompt-relevant settings

| Concern | Prompt-writing consequence |
| --- | --- |
| Reference mode | Image inputs can be passed as a list; map reference roles to their actual order. [F1] |
| Negative prompt | The FLUX.2 guide favours positive descriptions and does not support conventional negative prompting. [F2] |
| Colour | Associate colour names or hex targets with individual objects; exact output colour still needs checking. [F2] |
| JSON | Optional organisation for complex prompts, not a special API schema or mandatory format. |
| Settings | Don't borrow the Pro hosted API's image count/size contract as a guarantee for every local Dev workflow. |

## What wording cannot guarantee

A prompt cannot attach an absent reference, enable a disabled tool, force factual correctness, guarantee exact typography or prove transparency. Keep reference identity, settings and file requirements separate from visible content. If a user requires exact geometry or pixel-identical preservation, describe that need honestly rather than claiming stronger model guarantees.

Use the user's selected model and installed frontend as the scope of any refinement. New fine-tunes and hosted wrappers can change behaviour; a version-specific parameter should not be promoted into a family-wide rule.
