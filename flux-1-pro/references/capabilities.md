# FLUX.1 Pro: identity and constraints

Reference check: 2026-10-19. Bracketed evidence labels resolve in [sources.md](sources.md). Tables mix documented facts with explicitly labelled author suggestions. Settings are context for writing prompts, not instructions to execute a generation workflow.

## Model identity

This skill preserves the original FLUX.1 Pro request. FLUX1.1 Pro, Ultra, Fill Pro and Kontext Pro are distinct releases. The original FLUX.1 family included a hosted Pro model. At the research date, BFL's current OpenAPI schema did not list /v1/flux-pro; treat present-day availability and provider settings as unconfirmed, not as a working integration. [F1, F2]

## Prompt-relevant settings

| Concern | Prompt-writing consequence |
| --- | --- |
| Endpoint | No currently verified original-Pro endpoint is prescribed by this package. [F2] |
| Parameters | Ask for the exact provider/model label if settings materially affect a rewrite; don't invent steps, CFG, strength or resolution limits. |
| Prompt form | Start with a coherent natural-language scene; this package's examples are author recommendations, not a claimed official original-Pro formula. |
| Image editing | Native original-Pro instruction editing isn't established by the consulted sources. Don't transfer Kontext or Ultra features. |
| Substitution | Offer an alternative only explicitly; preserve the requested model in the actual prompt handoff. |

## Unverified image-to-image handoff

The example in editing.md is a desired-result brief only. It is not evidence that original FLUX.1 Pro can accept a reference image. If a user needs faithful editing, explain this limit and identify their actual surface before producing model-specific editing instructions. Do not silently switch models.

## What wording cannot guarantee

A prompt cannot attach an absent reference, enable a disabled tool, force factual correctness, guarantee exact typography or prove transparency. Keep reference identity, settings and file requirements separate from visible content. If a user requires exact geometry or pixel-identical preservation, describe that need honestly rather than claiming stronger model guarantees.

Use the user's selected model and installed frontend as the scope of any refinement. New fine-tunes and hosted wrappers can change behaviour; a version-specific parameter should not be promoted into a family-wide rule.
