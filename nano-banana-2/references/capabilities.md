# Nano Banana 2: identity and constraints

Reference check: 2026-10-19. Bracketed evidence labels resolve in [sources.md](sources.md). Tables mix documented facts with explicitly labelled author suggestions. Settings are context for writing prompts, not instructions to execute a generation workflow.

## Model identity

Nano Banana 2 maps to Gemini 3.1 Flash Image. It is neither Nano Banana Pro nor the later Nano Banana 2.1. The documented improvements include more output sizes, extreme aspect ratios, text and image Search grounding, and improved visual consistency. Keep the user's chosen version even when a documentation page defaults to a newer one. [G1]

## Prompt-relevant settings

| Concern | Prompt-writing consequence |
| --- | --- |
| Size | 0.5K, 1K, 2K and 4K tiers; default 1K. Treat tiers as runtime notes. [G1] |
| Ratio | Includes 1:4, 4:1, 1:8 and 8:1 in addition to conventional ratios. Compose deliberately for narrow or panoramic formats. [G1] |
| References | Guidance covers up to four characters and ten objects within a workflow. Use explicit input roles. [G2] |
| Negative prompt | Use natural-language constraints; don't import SDXL weights or negative syntax. |
| Current information | Grounding depends on the selected interface and enabled tools. A written request doesn't prove it ran. |

## What wording cannot guarantee

A prompt cannot attach an absent reference, enable a disabled tool, force factual correctness, guarantee exact typography or prove transparency. Keep reference identity, settings and file requirements separate from visible content. If a user requires exact geometry or pixel-identical preservation, describe that need honestly rather than claiming stronger model guarantees.

Use the user's selected model and installed frontend as the scope of any refinement. New fine-tunes and hosted wrappers can change behaviour; a version-specific parameter should not be promoted into a family-wide rule.
