# Qwen Image 3: identity and constraints

Reference check: 2026-10-19. Bracketed evidence labels resolve in [sources.md](sources.md). Tables mix documented facts with explicitly labelled author suggestions. Settings are context for writing prompts, not instructions to execute a generation workflow.

## Model identity

In this image-generation context, Qwen 3 means Qwen-Image-3.0, not Qwen3 or Qwen3-VL. The official release describes longer, information-rich prompts and multilingual text rendering. Alibaba Cloud documents both standard and Pro generation/editing models. This package does not assume downloadable 3.0 weights or native RGBA merely because those exist for Qwen-Image-2.1. [Q1, Q2]

## Prompt-relevant settings

| Concern | Prompt-writing consequence |
| --- | --- |
| Input budget | Release material advertises up to 4.5K prompt tokens; provider limits can differ. Use the space for real layout requirements, not padding. [Q1] |
| Hosted I2I | 1-3 reference images; don't copy 2.1's ten-reference allowance. [Q2] |
| Size | Hosted area 512x512 to 2048x2048 pixels, ratio 1:8 to 8:1; size syntax uses width*height. [Q2] |
| Negatives | Hosted 3.0 supports a negative_prompt field. [Q2] |
| Enhancement | prompt_extend defaults on; agent enhancement is T2I-only, not I2I. [Q2] |
| Transparency | Not established for 3.0 by the consulted sources; don't promise an alpha output. |

## What wording cannot guarantee

A prompt cannot attach an absent reference, enable a disabled tool, force factual correctness, guarantee exact typography or prove transparency. Keep reference identity, settings and file requirements separate from visible content. If a user requires exact geometry or pixel-identical preservation, describe that need honestly rather than claiming stronger model guarantees.

Use the user's selected model and installed frontend as the scope of any refinement. New fine-tunes and hosted wrappers can change behaviour; a version-specific parameter should not be promoted into a family-wide rule.
