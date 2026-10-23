# Stable Diffusion 2: identity and constraints

Reference check: 2026-10-23. Bracketed evidence labels resolve in [sources.md](sources.md). Tables mix documented facts with explicitly labelled author suggestions. Settings are context for writing prompts, not instructions to execute a generation workflow.

## Model identity

The reference here is Stable Diffusion 2.1-v (`stabilityai/stable-diffusion-2-1`, `v2-1_768-ema-pruned.ckpt`): a latent diffusion model with an 865M UNet, a downsampling-factor-8 autoencoder and a frozen OpenCLIP ViT-H/14 text encoder, conditioned on the penultimate text-encoder layer. It was fine-tuned from 2.0-v with a looser NSFW filter. [S1, S9]

The official Stable Diffusion 2.x Hugging Face repositories, apart from the x4 upscaler, and the Stability-AI/stablediffusion GitHub repository were no longer publicly available on the check date. Facts below come from archived copies of those pages plus live Diffusers documentation. A user may still hold local weights or a mirror; preserve whatever exact file they name. See [sources.md](sources.md).

## Variant map

| Checkpoint | Native canvas | Objective | Role |
| --- | --- | --- | --- |
| 2.1-v (`stable-diffusion-2-1`) | 768x768 | v-prediction | Default text-to-image reference. [S1] |
| 2.1-base (`stable-diffusion-2-1-base`) | 512x512 | Epsilon (noise) prediction | Fine-tuned from 2.0-base with the looser filter. [S2] |
| 2.0-v (`stable-diffusion-2`) | 768x768 | v-prediction | Original November 2022 release; stricter dataset filter than 2.1. [S3, S9] |
| 2.0-base (`stable-diffusion-2-base`) | 512x512 | Epsilon prediction | Parent of 2.0-v and of the inpainting and depth checkpoints. [S4] |
| Inpainting (`stable-diffusion-2-inpainting`) | 512x512 | Epsilon prediction | Resumed from 2.0-base, not 2.1; takes the masked image as extra conditioning. [S5] |
| Depth (`stable-diffusion-2-depth`) | 512x512 | Epsilon prediction | Resumed from 2.0-base; conditioned on a MiDaS relative depth estimate. [S6] |
| x4 upscaler (`stable-diffusion-x4-upscaler`) | Trained on 512x512 crops | v-prediction scheduler config | Text-guided 4x latent upscaler with a `noise_level` input. [S7, S12] |
| unCLIP (`stable-diffusion-2-1-unclip`, `-unclip-small`) | 768x768 | Based on 2.1-v | Takes a noisy CLIP image embedding plus text, for image variations. H and L variants. [S8, S9] |

Community fine-tunes built on 2.x can change vocabulary, resolution and negative-prompt habits. Don't treat them as the base checkpoint.

## Text encoder consequences

| Concern | Prompt-writing consequence |
| --- | --- |
| Encoder | OpenCLIP ViT-H/14, trained on LAION data, replaces the OpenAI CLIP ViT-L/14 used by SD 1.x. Prompt vocabulary tuned for 1.5 often transfers poorly. [S9, S15] |
| Names | Stability's 2.1 release says 2.1 "brings back many of the old prompts", but no primary source quantifies artist or celebrity recognition. Author guidance: assume weak or unpredictable name recall and describe the medium, technique, era, palette and lighting instead. [S14] |
| Dataset filter | 2.0 was trained on LAION-5B filtered with the LAION NSFW classifier at `punsafe=0.1`; Stability says this sharply reduced people in the data. 2.1 continued at `punsafe=0.98`, which Stability describes as less aggressive. [S1, S3, S14] |
| Negatives | Stability says negative prompts "work even better in 2.1". Author guidance: 2.x outputs often look flat or unfinished without a focused negative prompt, so write one by default. [S14] |
| Length | The tokenizer's `model_max_length` is 77, including start and end tokens, so about 75 usable tokens. Diffusers truncates; some frontends chunk longer prompts. Put essentials first. [S7, S13] |
| Clip skip | Conditioning already uses the penultimate layer. Don't carry an SD 1.x clip-skip habit across without checking the frontend's convention. [S9] |
| Weighting | `(word:1.2)` and similar syntax is parsed by particular frontends such as AUTOMATIC1111 or ComfyUI, or by add-on libraries such as Compel or sd_embed in Diffusers. Plain Diffusers passes the brackets as literal text. Stability's old DreamStudio interface used `| text: -1.0` for negatives. [S13, S14] |
| Language | Trained mainly on English captions; other languages work noticeably worse. [S1] |

## Resolution and objective

| Concern | Prompt-writing consequence |
| --- | --- |
| 768-v canvas | 768x768 is the trained size. Author suggestion: keep the shorter side near 768 for other ratios, such as 1024x768 or 768x1024, and in multiples of 64. |
| 512-base canvas | 512x512 is the trained size. Author suggestion: 768x512 or 512x768 for landscape or portrait. |
| Off-resolution | Author guidance: well below native size, outputs degrade into mush; well above it, subjects duplicate or compositions repeat. Stability's 2.1 post says the model can render non-standard and extreme aspect ratios, which is a capability claim, not a quality guarantee. [S14] |
| Objective mismatch | A v-prediction checkpoint needs a v-prediction config, such as `v2-inference-v.yaml`. A wrong config produces noise or garbage that no prompt can fix. Check the config before rewriting the prompt. [S9] |
| Precision | The 2.1 README warns that fp16 vanilla attention can be numerically unstable on 2.1. Black or blank images point to a runtime issue, not a prompt issue. [S9] |
| Guidance and steps | The README notes v-models can be sampled at higher guidance scales. Diffusers recommends DPMSolverMultistep at about 20-25 steps. Author baseline: CFG 7-9 for 768-v and 6-8 for 512-base; experiment, don't treat as limits. [S9, S10] |

## Documented limitations

The 2.1 model card lists imperfect photorealism, no legible text, weak compositionality (its example: "A red cube on top of a blue sphere"), unreliable faces and people, and a lossy autoencoder. Plan around these rather than promising them away. [S1]

## What wording cannot guarantee

A prompt cannot attach an absent reference, enable a disabled tool, force factual correctness, guarantee exact typography or prove transparency. Keep reference identity, settings and file requirements separate from visible content. If a user requires exact geometry, legible lettering or pixel-identical preservation, describe that need honestly rather than claiming stronger model guarantees.

Use the user's selected checkpoint and installed frontend as the scope of any refinement. A version-specific parameter should not be promoted into a family-wide rule.
