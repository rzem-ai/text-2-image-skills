# Stable Diffusion 3.5: identity and constraints

Reference check: 2026-10-23. Bracketed evidence labels resolve in [sources.md](sources.md). Tables mix documented facts with explicitly labelled author suggestions. Settings are context for writing prompts, not instructions to execute a generation workflow.

## Model identity

Stable Diffusion 3.5 is a family of open-weight rectified-flow transformer models released in October 2024 under the Stability AI Community Licence. All three variants condition on three frozen text encoders: CLIP-ViT/L, OpenCLIP-ViT/G and T5-XXL. [S1, S2, S3, S5]

| Variant | Identifier | Architecture | Upstream baseline |
| --- | --- | --- | --- |
| Large | `stabilityai/stable-diffusion-3.5-large` | MMDiT, about 8.1B parameters, around 1MP | 28 steps, guidance 3.5 (4.5 in the long-prompt example) [S1, S5] |
| Large Turbo | `stabilityai/stable-diffusion-3.5-large-turbo` | Large distilled with Adversarial Diffusion Distillation | 4 steps, guidance 0.0 [S2] |
| Medium | `stabilityai/stable-diffusion-3.5-medium` | MMDiT-X, about 2.5B parameters, 0.25 to 2MP | 40 steps, guidance 4.5; Skip Layer Guidance recommended [S3, S5] |

Don't merge these with nearby models:

- SD3 Medium (`stabilityai/stable-diffusion-3-medium`, June 2024) is the earlier 2B release. Stability's own announcement says it fell short of expectations, and the hosted `sd3-*` model names now re-route to 3.5 equivalents. Advice written for SD3 Medium isn't automatically valid here. [S5, S6]
- Medium has a different training distribution from Large, so the same prompt can respond differently. Don't promise identical results when switching variants. [S3]
- Stable Image Ultra is a hosted service described as based on SD3.5 Large; Stable Image Core is described as the successor to SDXL. Both are separate products with their own parameters. [S7]
- SD 3.5 Flash appears in Stability's hosted SD3.5 page as a distilled Medium. No open checkpoint was found and the API's own model enum omits it. Treat it as hosted-only and unverified; see [sources.md](sources.md). [S6]
- The `-tensorrt`, `_amdgpu` and `-amdnpu` repositories are optimised runtime ports of the same family, not new prompt dialects.

No newer Stability open image model was found on Hugging Face as of the check date; its recent releases there are audio and runtime ports.

## Text encoders and prompt length

| Concern | Prompt-writing consequence |
| --- | --- |
| CLIP limit | Both CLIP encoders use a 77-token context. Anything beyond that is truncated on the CLIP branch, so put the subject, medium and key text early. [S1, S4] |
| T5 length | T5 trained at 77 then 256 tokens. Diffusers defaults `max_sequence_length` to 256; upstream long-prompt examples raise it to 512. Longer settings cost time and memory. [S1, S4] |
| Long-prompt artefacts | The Medium card warns of edge artefacts when T5 tokens exceed 256. Shorten before blaming the prompt content. [S3] |
| Split prompts | Diffusers accepts `prompt`, `prompt_2` and `prompt_3` (CLIP-L, CLIP-G, T5). A short CLIP summary plus a fuller T5 description is a documented pattern, only useful where the surface exposes the fields. [S4] |
| Dropping T5 | Running without T5 saves memory with a small quality loss. Expect weaker long-prompt and text adherence; keep prompts short in that case. [S4] |

## Guidance and negatives

| Concern | Prompt-writing consequence |
| --- | --- |
| Large and Medium | Classifier-free guidance is active, so a negative prompt has an effect. The hosted API defaults `cfg_scale` to 4 for both. [S4, S6] |
| Large Turbo | The upstream baseline uses guidance 0.0. Diffusers ignores negative prompts when guidance is below 1, and the hosted API defaults Turbo to 1. Put requirements in the positive prompt instead. [S2, S4, S6] |
| Skip Layer Guidance | Recommended for Medium structure and anatomy. Diffusers notes layers 7, 8, 9 with scale 2.8, start 0.01, stop 0.2. A runtime option, not prompt text. [S3, S4] |
| Weights | The hosted API documents `(word:weight)` with weights from 0 to 1. Local Diffusers doesn't parse that syntax; ComfyUI and others have their own rules. Don't add it by default. [S6] |
| Style presets | The hosted API has a `style_preset` field (for example `photographic`, `line-art`, `pixel-art`). Mention it as a setting, not prompt text. [S6] |

## Canvas

The hosted SD3.5 endpoint returns about 1MP from fixed ratios: 21:9, 16:9, 3:2, 5:4, 1:1, 4:5, 2:3, 9:16 and 9:21. Locally, Large targets about 1MP and Medium was trained up to 1440 pixels, with a stated 0.25 to 2MP range. Author suggestion: stay near 1024x1024 or its 1MP siblings for Large and Turbo; use Medium for wider resolution experiments. [S3, S5, S6]

## What wording cannot guarantee

A prompt cannot attach an absent reference, enable a disabled tool, force factual correctness, guarantee exact typography or prove transparency. SD3.5 improves typography over earlier Stable Diffusion releases, but long passages, small type and dense layouts still need checking. Keep reference identity, settings and file requirements separate from visible content. If a user requires exact geometry or pixel-identical preservation, describe that need honestly rather than claiming stronger model guarantees.

Use the user's selected variant and installed frontend as the scope of any refinement. Fine-tunes, LoRAs and hosted wrappers can change behaviour; a variant-specific setting should not be promoted into a family-wide rule.
