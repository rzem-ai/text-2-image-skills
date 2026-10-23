---
name: ideogram-4-5
description: "Write and refine plain-language, structured JSON and Precise Edit prompts for Ideogram 4.5 (API model ideogram-4-5), with exact-typography, layout, Magic Prompt and preservation guidance. Use for this flagship hosted version, not Ideogram 4.0, 4.0 Transparent, 3.0 (style presets, style references, negative prompt), 2.0/2a, Auto model selection or partner models served inside the Ideogram app. Prompt writing only."
---

# Ideogram 4.5 prompt writing

Write copy-ready prompts for Ideogram 4.5 (`ideogram-4-5`), Ideogram's hosted flagship for generation and precise editing in the Ideogram app, MCP and API. This skill writes and refines prompts; it does not generate images, call APIs, read accounts or run Magic Prompt.

## Read selectively

- Read [capabilities and settings](references/capabilities.md) to resolve identity, the version boundary with 4.0 and 3.0, Magic Prompt, quality, size and background assumptions.
- Read [prompting and examples](references/prompting.md) when building or repairing a plain-language or JSON prompt, especially one with exact lettering.
- Read [image-to-image guidance](references/editing.md) for reference images, Precise Edit, masks, edit windows, Remix, reframing, background replacement or upscaling.
- Read [sources](references/sources.md) for evidence, conflicts and refresh needs. Embedded notes were checked on 2026-10-23; browse only when the task needs information beyond them or current verification.

## Workflow

1. Extract fixed requirements: image type, subject, count, action, setting, medium, composition, exact visible text, language, reference roles and exclusions. Preserve names and supplied copy character for character. Fill harmless visual gaps coherently; ask only when a missing detail materially changes the result.
2. Preserve the selected model. Ideogram 4.5, 4.0, 3.0, their Transparent variants, Auto and partner models have different controls. If the user wants a 3.0-only control (style preset, style reference, negative prompt, colour-palette preset), say so outside the prompt rather than silently switching models.
3. Choose the mode: text-to-image, generation with references (an edit instruction), Precise Edit with or without a mask, or a separate tool. If an image is available, inspect it before claiming its contents. If it isn't, write a conditional brief without pretending to have seen it.
4. Choose plain language or JSON. Use sentences for ordinary images; use the structured JSON schema when several text blocks, hex colours or placement must be stated separately. Validate any JSON before delivery.
5. Decide the Magic Prompt note. For an approved, detailed or exact-copy prompt, advise Magic Prompt off (`magic_prompt: off` in the API) outside the prompt. For a short exploratory idea, leaving it on is reasonable. It does not apply once references make the prompt an edit instruction.
6. Refine against the brief: put the main idea and quoted text early, bind attributes to the correct objects, phrase exclusions positively and remove decorative detail that competes with lettering. If an output is supplied, address its observed failure first.
7. Deliver one prompt in a fenced text block (or a fenced json block for a structured prompt). Ideogram 4.5 has no negative-prompt field, so never add a negative block. Keep size, quality, background, seed, image count and Magic Prompt as brief notes outside the prompt. For a prompt-only request, return just the fenced prompt.

## Refinement discipline

Keep successful content while repairing the specific failure. Change one thing per iteration so the user can tell what helped, and for edits change one thing per turn. Treat improvements as recommendations unless rendered comparisons are supplied; never claim this skill ran a model, verified spelling in an output or guaranteed pixel preservation.
