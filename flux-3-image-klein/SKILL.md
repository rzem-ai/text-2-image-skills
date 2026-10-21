---
name: flux-3-image-klein
description: "Write and refine expanded prompts for FLUX 3 Image Klein, including native reference edits and bounding-box layouts. Use for black-forest-labs/flux-3-image-klein, not FLUX.2 Klein 9B, Klein Base or the separate prompt-upsampler model. Prompt writing only."
---

# FLUX 3 Image Klein prompt writing

Target the distilled `black-forest-labs/flux-3-image-klein` image model. Supply the expanded visual caption or editing brief it expects. This skill performs LLM-based prompt writing only; it doesn't run the official prompt-upsampler weights, generate images or install a runtime.

## Read selectively

- Read [capabilities](references/capabilities.md) for checkpoint identity, distillation, references and upsampling expectations.
- Read [prompting](references/prompting.md) for full captions, exact lettering, layouts and original examples.
- Read [editing](references/editing.md) for source-aware edits, multi-reference composition and local versus hosted box conventions.
- Read [sources](references/sources.md) for provenance, conflicting schema details and refresh boundaries. References were checked on 2026-10-22.

## Workflow

1. Extract the supplied subject, count, action, medium, exact wording, spatial constraints and intended references. Preserve the user's visual choices; resolve ordinary gaps into one coherent plan.
2. Preserve the exact variant. Distilled FLUX 3 Klein, its Base checkpoint, the PUP rewriter and FLUX.2 Klein 9B are distinct components. Don't transfer four-step FLUX.2 guidance into this skill.
3. For generation, expand the idea into a complete scene caption covering medium, setting, framing, light, subjects, material, colour and relationships. Prefer concrete visible choices over quality suffixes. Keep a deliberately simple scene simple.
4. For editing, inspect the actual source images, identify their roles, then write the expanded source-aware instruction. Include the changed appearance and the scene details needed to preserve the composition; a one-line change can reframe the shot. If a reference is missing, make the brief conditional.
5. Use box layouts only when placement warrants them. Read the schema before writing one. Match caption IDs to rows, validate coordinates and reference indexing, and preserve any user-supplied valid boxes. Don't mix generation rows, local edit rows and hosted edit rows.
6. Return the full prompt in one fenced text block. A caption followed by an element array is one model prompt, not an API request. Keep canvas, attachment mapping and any upsampler handoff note outside it. For a prompt-only request, return only the fenced prompt.

## Refinement discipline

Keep exact displayed text and successful structure while repairing the specific failure. Don't invent faces, labels or source details from names alone. State that this is an authored expanded prompt, not output from the official PUP model. If the target surface performs another expansion pass, mention that setting only when needed to avoid intent drift. Never claim verified image quality or pixel-perfect preservation without rendered evidence.
