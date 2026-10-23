---
name: sd-3-5
description: "Write, refine and troubleshoot text-to-image prompts and image-to-image briefs for Stability AI Stable Diffusion 3.5 Large, Large Turbo and Medium, including quoted typography, CLIP/T5 prompt splitting, negative prompts and ControlNet or hosted-edit briefs. Use for stabilityai/stable-diffusion-3.5-* checkpoints or the Stability API sd3 endpoint, not SD3 Medium (June 2024), SDXL, Stable Image Ultra/Core or fine-tunes with their own conventions. Prompt writing only."
---

# Stable Diffusion 3.5 prompt writing

Write copy-ready prompts for Stability AI Stable Diffusion 3.5 Large, Large Turbo and Medium (`stabilityai/stable-diffusion-3.5-large`, `-large-turbo`, `-medium`). This skill writes and refines prompts; it does not generate images, call APIs, install models or run a prompt-enhancement model.

## Read selectively

- Read [capabilities and settings](references/capabilities.md) to resolve the variant, text-encoder limits, guidance behaviour and resolution assumptions.
- Read [prompting and examples](references/prompting.md) when building or repairing a prompt, including quoted text and negative prompts.
- Read [image-to-image guidance](references/editing.md) for img2img strength, masks, ControlNets or hosted edit services.
- Read [sources](references/sources.md) for evidence, conflicts and refresh needs. Embedded notes were checked on 2026-10-23; browse only when the task needs information beyond them or current verification.

## Workflow

1. Extract fixed requirements: subject, count, action, setting, medium, composition, exact visible text, language, reference roles and exclusions. Preserve names and supplied copy. Fill harmless visual gaps coherently; ask only when a missing detail materially changes the result.
2. Preserve the selected variant. Large, Large Turbo and Medium respond differently, and SD3 Medium is an older, separate checkpoint. If the variant is unknown and it changes the answer (negative prompt, length, settings), state the assumption outside the prompt. Don't substitute a newer or hosted model silently.
3. Choose text-to-image, image-to-image, inpainting or structural control using the embedded mode guidance. If an image is available, inspect it before claiming its contents. If it isn't, write a conditional brief without pretending to have seen it.
4. Draft in clear natural language: style, then subject and action, composition, lighting and colour, then camera terms. Put essentials in the first sentence or two because the CLIP encoders truncate at 77 tokens. Wrap short exact lettering in double quotes. Keep runtime settings outside the image prompt.
5. Refine against the brief: fix conflicts, bind attributes to the correct objects, preserve exact lettering and remove decorative detail that changes the intended subject. If an output is supplied, address its observed failure first.
6. Deliver one prompt in a fenced text block. Add a separate labelled negative prompt block only for a guided variant (Large, Medium) and only when there is a concrete reason; omit it for Turbo at its documented no-CFG baseline. Offer a separate short CLIP prompt and long T5 prompt only when the user's surface exposes both fields. For a prompt-only request, return just the fenced prompt.

## Refinement discipline

Keep successful content while repairing the specific failure. Explain a substantial intentional change briefly. For variants, hold the subject fixed and vary one meaningful visual choice. Don't add parenthesis weights unless the target surface documents them. Treat improvements as recommendations unless actual rendered comparisons are supplied; never claim this skill ran a model or verified image fidelity.
