# Qwen Image 2.1: identity and constraints

Reference check: 2026-10-19. Bracketed evidence labels resolve in [sources.md](sources.md). Tables mix documented facts with explicitly labelled author suggestions. Settings are context for writing prompts, not instructions to execute a generation workflow.

## Model identity

Qwen-Image-2.1 unifies generation and editing, supports native RGBA output and up to ten reference images. The model card names QwenImage21Pipeline and a 40-step example. Its visual generator has 7B parameters. Don't confuse a prompt-enhancement language model with the image generator, or import the original Qwen-Image's runtime assumptions. [Q1]

## Prompt-relevant settings

| Concern | Prompt-writing consequence |
| --- | --- |
| Canvas | Card examples: 2048x2048 square, 2752x1536 landscape, 1536x2752 portrait. These local examples aren't universal hosted dimensions. [Q1] |
| Transparency | Use the documented RGBA opening and closing wording, then specify subject and clean silhouette. [Q1] |
| Reference edits | Up to ten references; circles, annotations or separate masks can indicate edits on supported workflows. [Q1] |
| Hosted negatives | The Qwen 2.1 series doesn't support negative_prompt in the consulted hosted guide; use ordinary prompt constraints. [Q2] |
| Rewriting | Hosted automatic enhancement and official PE models are separate from manually improving a prompt. |

## What wording cannot guarantee

A prompt cannot attach an absent reference, enable a disabled tool, force factual correctness, guarantee exact typography or prove transparency. Keep reference identity, settings and file requirements separate from visible content. If a user requires exact geometry or pixel-identical preservation, describe that need honestly rather than claiming stronger model guarantees.

Use the user's selected model and installed frontend as the scope of any refinement. New fine-tunes and hosted wrappers can change behaviour; a version-specific parameter should not be promoted into a family-wide rule.
