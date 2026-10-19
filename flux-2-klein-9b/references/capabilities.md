# FLUX.2 Klein 9B: identity and constraints

Reference check: 2026-10-19. Bracketed evidence labels resolve in [sources.md](sources.md). Tables mix documented facts with explicitly labelled author suggestions. Settings are context for writing prompts, not instructions to execute a generation workflow.

## Model identity

This package targets the distilled 9B model, not Klein Base 9B or Klein 4B. It unifies text-to-image and multi-reference editing. The model-card example uses Flux2KleinPipeline, 1024x1024, four inference steps and guidance_scale=1.0. More steps and high SDXL CFG are not a general recipe for improving this distilled model. [F1]

## Prompt-relevant settings

| Concern | Prompt-writing consequence |
| --- | --- |
| Distillation | Four steps and guidance 1.0 are the published example context. Don't copy Dev's 50-step/guidance-4 baseline. [F1] |
| Variant | Preserve 9B distilled versus Base/KV/preview labels when given. |
| References | Native reference editing exists, but input limits depend on local or hosted surface. |
| Wording | Start with a direct scene or edit instruction; a short prompt is a useful baseline, not a hard token limit. |
| Negatives | Don't assume a conventional negative branch; special community guidance methods are workflow-specific. |

## What wording cannot guarantee

A prompt cannot attach an absent reference, enable a disabled tool, force factual correctness, guarantee exact typography or prove transparency. Keep reference identity, settings and file requirements separate from visible content. If a user requires exact geometry or pixel-identical preservation, describe that need honestly rather than claiming stronger model guarantees.

Use the user's selected model and installed frontend as the scope of any refinement. New fine-tunes and hosted wrappers can change behaviour; a version-specific parameter should not be promoted into a family-wide rule.
