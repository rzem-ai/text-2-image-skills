# FLUX.2 Pro: identity and constraints

Reference check: 2026-10-19. Bracketed evidence labels resolve in [sources.md](sources.md). Tables mix documented facts with explicitly labelled author suggestions. Settings are context for writing prompts, not instructions to execute a generation workflow.

## Model identity

FLUX.2 Pro is a hosted generation and multi-reference editing model. flux-2-pro is a fixed snapshot; flux-2-pro-preview is a separate moving endpoint. Preserve that distinction when comparing prompt revisions. Automatic prompt upsampling is enabled by default on the documented Pro API; disable_pup=true requests use of the supplied prompt without that expansion. [F1, F2]

## Prompt-relevant settings

| Concern | Prompt-writing consequence |
| --- | --- |
| Inputs | Documented Pro editing supports up to ten reference images; use an explicit role map. [F3] |
| Resolution | FLUX.2 output can reach 4 megapixels; don't equate 4MP with a 4K square. [F2] |
| Prompt expansion | Keep automatic expansion in mind when a precise written prompt appears to gain unrequested content. [F1] |
| Negative prompt | No conventional negative prompting; state the desired scene positively. [F4] |
| Control | Don't invent user-adjustable steps/guidance merely because a different FLUX endpoint exposes them. |

## What wording cannot guarantee

A prompt cannot attach an absent reference, enable a disabled tool, force factual correctness, guarantee exact typography or prove transparency. Keep reference identity, settings and file requirements separate from visible content. If a user requires exact geometry or pixel-identical preservation, describe that need honestly rather than claiming stronger model guarantees.

Use the user's selected model and installed frontend as the scope of any refinement. New fine-tunes and hosted wrappers can change behaviour; a version-specific parameter should not be promoted into a family-wide rule.
