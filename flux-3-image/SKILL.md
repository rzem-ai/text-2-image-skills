---
name: flux-3-image
description: "Write, refine and troubleshoot prompts, edit instructions and bounding-box layouts for Black Forest Labs FLUX 3 Image, the hosted flux-3-image endpoint. Use when this model is requested or an existing prompt targets it. Not for FLUX 3 Image Klein, FLUX.2 or FLUX.1. Prompt writing only; never executes generation."
---

# FLUX 3 Image prompt writing

Write copy-ready prompts for Black Forest Labs FLUX 3 Image (`flux-3-image`), the hosted generation and editing endpoint. This skill writes and refines prompts; it does not call the API, generate images, verify outputs or run any prompt-expansion model.

## Read selectively

- Read [capabilities](references/capabilities.md) for identity, the Klein distinction, automatic expansion, grounding and prompt-relevant settings.
- Read [prompting](references/prompting.md) for scene captions, exact lettering, hex colours, layouts and original examples.
- Read [editing](references/editing.md) for reference roles, local edits and hosted edit-row boxes.
- Read [sources](references/sources.md) for evidence, conflicts and refresh boundaries. References were checked on 2026-10-23.

## Workflow

1. Extract fixed requirements: subject, count, action, setting, medium, framing, exact visible text, colours, references and exclusions. Preserve supplied names and copy. Fill harmless gaps coherently; ask only when a missing detail materially changes the image.
2. Preserve the target. FLUX 3 Image is the hosted flagship; FLUX 3 Image Klein is a separate 5.6B open-weights model with its own endpoint and a different local box convention. FLUX.2 and FLUX.1 endpoints are older generations. Don't transfer their parameters, step counts or schema quirks.
3. One endpoint covers generation and editing. With no references, write a scene caption. With references, write an instruction that names each image by position and states its role. Inspect supplied images before naming their contents; if absent, write a conditional brief.
4. Describe the wanted scene positively. There is no negative-prompt or prompt-upsampling field, and the service expands prompts itself. Write the intended content directly rather than relying on exclusion lists.
5. Add a bounding-box array only when placement matters. Choose the aspect ratio first, then follow the schema in the references. Match every `<id>` token to a row and check coordinates. Use the hosted `from: null` convention for new content in edits; never Klein's local `"target"`.
6. Deliver the full prompt in one fenced text block. A caption followed by its JSON array is one prompt string. Keep `aspect_ratio`, `resolution`, `grounding`, image order and other settings in a short note outside it. For a prompt-only request, return only the fenced prompt.

## Refinement discipline

Keep exact text and working structure while repairing the observed failure. If the user supplies the expanded prompt returned by the service, compare it with the intent before rewriting. Don't invent faces, labels or product details from names alone. Treat any improvement as a recommendation unless rendered comparisons are supplied; never claim this skill ran the model or verified pixel preservation.
