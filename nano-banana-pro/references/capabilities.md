# Nano Banana Pro: identity and constraints

Reference check: 2026-10-19. Bracketed evidence labels resolve in [sources.md](sources.md). Tables mix documented facts with explicitly labelled author suggestions. Settings are context for writing prompts, not instructions to execute a generation workflow.

## Model identity

Nano Banana Pro is Google's reasoning-oriented image generation and editing model. It is distinct from Gemini 3 Pro's text model and from Nano Banana 2. Its documented uses include demanding layouts, product mockups and text-heavy graphics, with Search grounding supported on the appropriate surface. Don't imply that a prompt alone enables a tool. [G1]

## Prompt-relevant settings

| Concern | Prompt-writing consequence |
| --- | --- |
| Resolution | 1K, 2K and 4K outputs are documented. Keep the requested tier outside the copy-ready visual prompt. [G2] |
| References | Up to 14 total; documented guidance distinguishes six object references, five character references and three style references. These aren't guarantees of perfect preservation. [G2] |
| Grounding | Supply verified facts or identify the need for grounding outside the image prompt. |
| Layout | State text hierarchy, panel order, margins and relationships explicitly. |
| Exclusions | Ordinary language; no conventional diffusion negative-prompt field is established here. |

## What wording cannot guarantee

A prompt cannot attach an absent reference, enable a disabled tool, force factual correctness, guarantee exact typography or prove transparency. Keep reference identity, settings and file requirements separate from visible content. If a user requires exact geometry or pixel-identical preservation, describe that need honestly rather than claiming stronger model guarantees.

Use the user's selected model and installed frontend as the scope of any refinement. New fine-tunes and hosted wrappers can change behaviour; a version-specific parameter should not be promoted into a family-wide rule.
