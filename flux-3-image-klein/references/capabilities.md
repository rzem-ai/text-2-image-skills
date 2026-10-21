# FLUX 3 Image Klein: identity and constraints

Reference check: 2026-10-22. Evidence labels resolve in [sources.md](sources.md). Settings are prompt-writing context, not instructions to run inference.

## Identity and conditioning

The linked model is the distilled FLUX 3 Image Klein checkpoint. Its 5.6B label describes the image transformer, with a separate Qwen3-VL-4B-Instruct conditioning encoder. It supports text-to-image and editing with up to ten references. The official generation baseline is 16 steps without CFG. Base is a separate checkpoint; FLUX.2 Klein 9B is another generation entirely. [F1]

| Concern | Prompt-writing consequence |
| --- | --- |
| Full captions | Upstream expects an upsampled prompt for generation, editing and layouts. A terse idea isn't the final caption. This skill supplies an authored expansion. [F1, F2] |
| Separate PUP | The official PUP is a Qwen3.5-9B rewriter, not the image model's conditioning encoder. Another LLM can write the expanded prompt; don't claim to have executed PUP. [F2] |
| References | Explain which actual image supplies the base composition, subject identity or visual treatment. References anchor content without locking structure. [F1] |
| Box layouts | The final caption can include element IDs and a 0-1000 y-first box table. Boxes guide placement, not clipping or exact pixel preservation. [F3] |
| Negative prompts | No conventional negative-prompt branch is established for the distilled baseline here. Describe the intended content and relevant exclusions in prose. |
| Transparency | Native RGBA output isn't established by the consulted Klein documentation. Don't infer it from another image model. |

## Preserve version scope

The model card and reference repository differ in Base guidance examples; this package doesn't choose between them because it targets distilled Klein. Keep steps, guidance, quantisation, dimensions and seeds outside the prompt. Don't convert a file format or memory estimate into a visual instruction.

If a supplied surface already runs automatic prompt expansion, distinguish the user's short request from this skill's expanded handoff. Re-expansion can alter an approved brief; the appropriate control is surface-specific and isn't enabled or disabled by writing words inside the prompt.
