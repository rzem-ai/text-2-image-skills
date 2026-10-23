---
name: noobai-xl
description: "Write, refine and troubleshoot Danbooru-style tag prompts, negative prompts and image-to-image briefs for Laxhar Lab's NoobAI-XL (Epsilon-pred 1.1 and V-Pred 1.0). Use when NoobAI-XL is requested or an existing prompt targets it; provides embedded tag-order, quality-tag and variant-setting references without executing generation. Not for Pony Diffusion, Illustrious base checkpoints or generic SDXL."
---

# NoobAI-XL prompt writing

Write copy-ready prompts for Laxhar Lab's NoobAI-XL, an Illustrious-derived SDXL anime fine-tune. The baseline is Epsilon-pred 1.1 (`Laxhar/noobai-XL-1.1`); V-Pred 1.0 (`Laxhar/noobai-XL-Vpred-1.0`) is supported as a distinct variant with different runtime settings. This skill writes and refines prompts; it does not generate images, call APIs, install models or configure samplers.

## Read selectively

- Read [capabilities and settings](references/capabilities.md) to resolve identity, epsilon versus v-prediction, supported modes or parameter assumptions.
- Read [prompting and examples](references/prompting.md) when building or repairing a prompt.
- Read [image-to-image guidance](references/editing.md) for source images, inpainting, ControlNet or preservation requirements.
- Read [sources](references/sources.md) for evidence, conflicts and refresh needs. Embedded notes were checked on 2026-10-23; browse only when the task needs information beyond them or current verification.

## Workflow

1. Extract fixed requirements: subject count, character and series, action, setting, medium, composition, exact visible text, reference roles and exclusions. Preserve supplied names and tags. Fill harmless visual gaps coherently; ask only when a missing detail materially changes the result.
2. Preserve the selected checkpoint. If epsilon versus v-prediction affects the answer, state the assumption outside the prompt. Don't treat a NoobAI merge, Illustrious base or Pony checkpoint as equivalent.
3. Choose text-to-image, inpainting, ControlNet-guided or source-image regeneration using the embedded mode guidance. If an image is available, inspect it before claiming its contents. If it isn't, write a conditional brief without pretending to have seen it.
4. Draft in the creator's tag order with the creator quality prefix. Keep sampler, CFG, rescale and attachment notes outside the image prompt. Don't invent tags, unsupported controls or reference images.
5. Refine against the brief: fix conflicting tags, bind attributes to the right subject, keep the rating tag consistent with the brief and remove decorative tags that change the intended subject. If an output is supplied, address its observed failure first.
6. Deliver one prompt in a fenced text block and the negative prompt in a separate labelled fenced block. Add brief variant or settings notes only when useful. For a prompt-only request, return just the fenced blocks.

## Content boundaries

Default to the safe rating with clearly adult characters. Don't add sexual, suggestive or violent tags the user didn't request, and don't remove `nsfw` from the negative to "improve" results. Name real living artists only when the user supplies them, and don't build prompts that depict real people.

## Refinement discipline

Keep successful tags while repairing the specific failure. Explain a substantial intentional change briefly. For variants, hold the subject fixed and vary one meaningful visual choice. Treat improvements as recommendations unless rendered comparisons are supplied; never claim this skill ran a model or verified image fidelity.
