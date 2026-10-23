---
name: stable-diffusion-2
description: "Write, refine and troubleshoot text-to-image prompts, negative prompts and image-to-image, inpainting, depth2img and x4-upscaler briefs for Stability AI Stable Diffusion 2.x (2.0, 2.1 768-v, 2.1-base 512 and its official variants). Use when this model is requested or an existing prompt targets it; provides embedded model references without executing generation. Not for SD 1.5, SDXL or SD3."
---

# Stable Diffusion 2 prompt writing

Write copy-ready prompts for Stability AI Stable Diffusion 2.1 (`stabilityai/stable-diffusion-2-1`, the 768x768 v-prediction checkpoint). Also covers 2.0, the 512x512 base checkpoints and the official inpainting, depth, x4-upscaler and unCLIP variants when the user names one. This skill writes and refines prompts; it does not generate images, call APIs, install models or run an official prompt-enhancement model.

Stable Diffusion 1.5, SDXL and SD3 use different text encoders and prompting habits. Don't apply this package to them, and don't silently move an SD 2.x request to a newer model.

## Read selectively

- Read [capabilities and settings](references/capabilities.md) to resolve identity, variant, resolution, text-encoder or parameter assumptions.
- Read [prompting and examples](references/prompting.md) when building or repairing a prompt or negative prompt.
- Read [image-to-image guidance](references/editing.md) for img2img, inpainting masks, depth2img, upscaling or unCLIP variations.
- Read [sources](references/sources.md) for evidence, scope and refresh needs. Embedded notes were checked on 2026-10-23; browse only when the task needs information beyond them or current verification.

## Workflow

1. Extract fixed requirements: subject, count, action, setting, medium, composition, exact visible text, language, reference roles and exclusions. Preserve names and supplied copy. Fill harmless visual gaps coherently; ask only when a missing detail materially changes the result.
2. Preserve the selected checkpoint. 768-v and 512-base differ in native canvas, and the editing variants are separate checkpoints. If the variant affects the answer, state the assumption outside the prompt.
3. Choose text-to-image, img2img, inpainting, depth2img, upscaling or unCLIP variation using the embedded mode guidance. If an image is available, inspect it before claiming its contents. If it isn't available, write a conditional brief without pretending to have seen it.
4. Draft in English with concrete visual description. Describe style through medium, technique and lighting rather than relying on artist or celebrity names. Keep runtime settings and attachment instructions outside the image prompt. Don't invent syntax, unsupported controls or reference images.
5. Write a focused negative prompt. It carries more weight on 2.x than on SD 1.5 workflows, but it must never contradict the brief.
6. Refine against the brief: fix conflicts, bind attributes to the correct objects, keep essentials inside the first 75 tokens and remove decorative detail that changes the intended subject. If an output is supplied, address its observed failure first.
7. Deliver one prompt in a fenced text block and the negative prompt in a separate labelled fenced block. Add brief assumptions, canvas or variant notes only when useful. For a prompt-only request, return just the fenced blocks.

## Refinement discipline

Keep successful content while repairing the specific failure. Explain a substantial intentional change briefly. For variants, hold the subject fixed and vary a meaningful visual choice. Treat improvements as recommendations unless actual rendered comparisons are supplied; never claim this skill ran a model or verified image fidelity.
