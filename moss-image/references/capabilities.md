# MOSS Image: identity and constraints

Reference check: 2026-10-22. Evidence labels resolve in [sources.md](sources.md). This package covers prompt writing, not inference or training.

## Identity

OpenMOSS publishes MOSS-Image-Base and its curated-data fine-tune MOSS-Image-SFT. Both are text-to-image models accepting captions, tags and structured layouts. SFT uses the same architecture and inference pipeline; this package uses SFT as its default prompting example without substituting it for an explicit Base request. MOSS-VL, MOSS audio models and the older MOSS language models are separate products. [M1, M2]

## Prompt-relevant context

| Concern | Consequence |
| --- | --- |
| Caption versus layout | Use prose for scenes; use experimental native layout JSON for explicit element placement. Layout is still text-to-image conditioning. [M3] |
| Text | Preserve exact copy and intended newlines. English descriptive prose is recommended upstream; Chinese and other input languages are supported. [M3] |
| Negative prompts | Supported. The SFT card's default is empty; the guide also offers targeted negative tags. Start with the user's needs rather than applying every upstream suggestion. [M1, M3] |
| Canvas | Positive multiples of 16. The guide recommends roughly 1M, 1.5M or 2M pixels and describes a wider 0.25M-4M range. [M3] |
| Official SFT baseline | 50 steps, CFG 3, shift 5, flow-matching Euler; negative-branch layer skipping uses index 22. These are runtime context, not prompt text. [M1] |
| Image references | No general native reference-image editing interface is established here. The guide discusses further post-training for reference-based generation. [M3] |
| Alpha | Native transparent RGBA output isn't established by these sources. Don't promise it. |

## Limits

Changing a layout caption or bounding box doesn't guarantee preservation of the previous image. Tiny lettering and precise geometry still need visual inspection. Don't carry assumptions from community Turbo, DMD or reference-conditioned derivatives into Base/SFT.

The model's licence is separate from the licence for these authored prompt notes. This package doesn't assess commercial rights or prescribe installation, hardware or training changes.
