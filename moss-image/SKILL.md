---
name: moss-image
description: "Write and refine MOS / MOSS Image prompts for OpenMOSS-Team/MOSS-Image-Base and MOSS-Image-SFT, including typography and native JSON layouts. Use for MOSS image generation, not MOSS language, audio or video models. Prompt writing only."
---

# MOSS Image prompt writing

Write copy-ready prompts for OpenMOSS's MOSS-Image family. In this collection, the user's label MOS refers to MOSS-Image-Base and MOSS-Image-SFT. Preserve an explicit checkpoint; otherwise use SFT as the declared prompting baseline. This skill writes captions and layouts, without generating images, installing models or running the upstream enhancer.

## Read selectively

- Read [capabilities](references/capabilities.md) for Base/SFT distinctions, supported modes and prompt-relevant settings.
- Read [prompting](references/prompting.md) for captions, lettering, native layout JSON, coordinate conversion and original examples.
- Read [editing](references/editing.md) when revising a layout or working from a source image. Native reference-image editing isn't established by the consulted model documentation.
- Read [sources](references/sources.md) for provenance and version scope. References were checked on 2026-10-22.

## Workflow

1. Extract the fixed subject, count, relationships, medium, spatial constraints, exact visible wording and language. Fill harmless visual gaps coherently. Don't invent event details or factual copy.
2. Choose a caption for ordinary photographs and illustrations. Choose a native JSON layout when independently placed text, objects or panels justify explicit boxes. Complexity alone doesn't require a layout.
3. Preserve Base versus SFT and any supplied fine-tune. Don't assume a community few-step variant has the official checkpoints' controls or capabilities.
4. Write concrete visible content. English is a useful descriptive default, while displayed copy remains verbatim in the user's language, including requested line breaks. Avoid redundant quality tags and imported Pony score prefixes.
5. For layout output, establish width and height first. Convert top-left pixel boxes into integer centred yxyx boxes using the embedded reference; keep dimensions outside the final positive prompt. Check bounds, reading order and exact text before delivering.
6. Return the complete caption in a fenced text block, or the ready-to-paste layout in a fenced JSON block. Put an optional focused negative prompt in its own labelled block. For a layout, state the matching canvas outside the prompt. Keep sampling controls outside both.

## Refinement discipline

Retain successful content and repair the observed failure. A request to edit layout JSON changes the next generation specification; it doesn't establish a native image-editing workflow. If an image is supplied, inspect it before describing its contents. Without it, label a source-based brief as conditional. Treat typography, placement and visual quality as recommendations to verify, rather than measured outcomes.
