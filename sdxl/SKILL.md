---
name: sdxl
description: "Write, refine and troubleshoot text-to-image prompts and image-to-image briefs for SDXL. Use when this model is requested or an existing prompt targets it; provides embedded model references without executing generation."
---

# SDXL prompt writing

Write copy-ready prompts for Stability AI Stable Diffusion XL 1.0 base (`stabilityai/stable-diffusion-xl-base-1.0`). This skill writes and refines prompts; it does not generate images, call APIs, install models or run an official prompt-enhancement model.

## Read selectively

- Read [capabilities and settings](references/capabilities.md) to resolve identity, variant, supported modes or parameter assumptions.
- Read [prompting and examples](references/prompting.md) when building or repairing a prompt.
- Read [image-to-image guidance](references/editing.md) for source images, edits, masks or preservation requirements.
- Read [sources](references/sources.md) for evidence, scope and refresh needs. Embedded notes were checked on 2026-10-19; browse only when the task needs information beyond them or current verification.

## Workflow

1. Extract fixed requirements: subject, count, action, setting, medium, composition, exact visible text, language, reference roles and exclusions. Preserve names and supplied copy. Fill harmless visual gaps coherently; ask only when a missing detail materially changes the result.
2. Preserve the selected model and checkpoint. If a variant affects the answer, state the assumption outside the prompt. Don't substitute a newer model silently.
3. Choose text-to-image, native editing or source-image regeneration using the embedded mode guidance. If an image is available, inspect it before claiming its contents. If it isn't available, write a conditional brief without pretending to have seen it.
4. Draft using this model's conventions. Keep runtime settings and attachment instructions outside the image prompt. Don't invent syntax, unsupported controls or reference images.
5. Refine against the brief: fix conflicts, bind attributes to the correct objects, preserve exact lettering and remove decorative detail that changes the intended subject. If an output is supplied, address its observed failure first.
6. Deliver one prompt in a fenced text block. Put an optional negative prompt in a separate labelled fenced block only when the model/workflow supports one. Add brief assumptions or reference-slot notes only when useful. For a prompt-only request, return just the fenced prompt.

## Refinement discipline

Keep successful content while repairing the specific failure. Explain a substantial intentional change briefly. For variants, hold the subject fixed and vary a meaningful visual choice. Treat improvements as recommendations unless actual rendered comparisons are supplied; never claim this skill ran a model or verified image fidelity.
