# Stable Diffusion 2: evidence and maintenance

Checked on 2026-10-23. These embedded references are concise, original summaries with original prompt examples. They are not verbatim copies of vendor manuals and do not depend on sibling skill packages.

## Availability note

On the check date the official Stability AI Hugging Face repositories for 2.0, 2.0-base, 2.1, 2.1-base, inpainting, depth and unCLIP returned "repository not found" or an authorisation error, and the Stability-AI/stablediffusion GitHub repository returned 404. Only `stabilityai/stable-diffusion-x4-upscaler` was still live. Those model cards and the README were read from Internet Archive Wayback Machine copies, linked below. Live Diffusers documentation still names the original repository IDs. Treat any current download location as unverified, and preserve the exact checkpoint or mirror the user supplies.

## Sources

1. [Stable Diffusion v2-1 model card (archived)](https://web.archive.org/web/2024/https://huggingface.co/stabilityai/stable-diffusion-2-1)

   Supports: 2.1-v identity, fine-tune from 2.0-v, `punsafe` schedule, OpenCLIP ViT-H encoder, v-objective, training history of all 2.x checkpoints, English-caption limitation and the documented limitations list. [S1]

2. [Stable Diffusion v2-1-base model card (archived)](https://web.archive.org/web/2024/https://huggingface.co/stabilityai/stable-diffusion-2-1-base)

   Supports: 2.1-base identity, 512 checkpoint and fine-tune from 2.0-base at `punsafe=0.98`. [S2]

3. [Stable Diffusion v2 model card (archived)](https://web.archive.org/web/2024/https://huggingface.co/stabilityai/stable-diffusion-2)

   Supports: 2.0-v identity, v-objective training resumed from 2.0-base and 768x768 fine-tuning. [S3]

4. [Stable Diffusion v2-base model card (archived)](https://web.archive.org/web/2024/https://huggingface.co/stabilityai/stable-diffusion-2-base)

   Supports: 2.0-base training at 256 then 512, LAION-5B NSFW filter at `punsafe=0.1` and aesthetic score threshold. [S4]

5. [Stable Diffusion v2 inpainting model card (archived)](https://web.archive.org/web/2024/https://huggingface.co/stabilityai/stable-diffusion-2-inpainting)

   Supports: Inpainting checkpoint resumed from 2.0-base, LaMa mask strategy, masked-image conditioning, white-to-repaint mask convention and example prompt shape. [S5]

6. [Stable Diffusion v2 depth model card (archived)](https://web.archive.org/web/2024/https://huggingface.co/stabilityai/stable-diffusion-2-depth)

   Supports: Depth checkpoint resumed from 2.0-base with MiDaS `dpt_hybrid` relative depth conditioning; example use of a negative prompt and strength. [S6]

7. [Stable Diffusion x4 upscaler model card](https://huggingface.co/stabilityai/stable-diffusion-x4-upscaler)

   Supports: Upscaler training on 512x512 crops, `noise_level` input, OpenCLIP ViT-H encoder; tokenizer `model_max_length` of 77 in the live repository files. [S7]

8. [Stable Diffusion v2-1-unclip model card (archived)](https://web.archive.org/web/2024/https://huggingface.co/stabilityai/stable-diffusion-2-1-unclip)

   Supports: unCLIP identity, CLIP image-embedding conditioning and the 0-1000 noise level range. [S8]

9. [Stability-AI/stablediffusion README (archived)](https://web.archive.org/web/2024/https://github.com/Stability-AI/stablediffusion)

   Supports: Release history, 865M UNet and penultimate-layer OpenCLIP conditioning, 768-v and 512-base configs, higher guidance for v-models, fp16 attention instability on 2.1, depth2img and img2img behaviour, upscaler `noise_level` advice and the unCLIP H and L variants. [S9]

10. [Diffusers Stable Diffusion 2 documentation](https://huggingface.co/docs/diffusers/main/en/api/pipelines/stable_diffusion/stable_diffusion_2)

    Supports: Task-to-repository map, 512 and 768 default resolutions, DPMSolverMultistep recommendation at about 20 steps. [S10]

11. [Diffusers depth-to-image pipeline API](https://huggingface.co/docs/diffusers/main/en/api/pipelines/stable_diffusion/depth2img)

    Supports: Depth2img strength semantics and default of 0.8, optional supplied depth map, negative prompt support. [S11]

12. [Diffusers super-resolution pipeline API](https://huggingface.co/docs/diffusers/main/en/api/pipelines/stable_diffusion/upscale)

    Supports: Upscaler `noise_level` default of 20 and its fidelity trade-off, negative prompt support. [S12]

13. [Diffusers prompting guide](https://huggingface.co/docs/diffusers/main/en/using-diffusers/weighted_prompts)

    Supports: Weighting through `prompt_embeds` with sd_embed or Compel rather than native bracket parsing. [S13]

14. [Stability AI Stable Diffusion 2.1 release post](https://stability.ai/news-updates/stablediffusion2-1-release7-dec-2022)

    Supports: Looser 2.1 filter after 2.0's filter cut people from the data, negative prompts working better in 2.1, return of many old prompts, non-standard resolution claim and the DreamStudio negative syntax. [S14]

15. [Stability AI Stable Diffusion 2.0 release post](https://stability.ai/news-updates/stable-diffusion-v2-release)

    Supports: OpenCLIP encoder announcement, NSFW filtering, 512 and 768 default resolutions, depth2img, upscaler and inpainting releases. [S15]

## Conflicts and unverified points

- The Diffusers upscaler `__call__` signature shows defaults of 75 steps and guidance 9.0, while its own parameter docstring says 50 and 7.5. This package states neither as fact; check the installed version. [S12]
- Diffusers API pages describe the generic Stable Diffusion text encoder as `clip-vit-large-patch14`. That is shared boilerplate; the SD 2.x model cards and README specify OpenCLIP ViT-H/14, which this package follows. [S1, S9]
- No primary source measures artist-name or celebrity recognition in 2.x versus SD 1.5. The weakness is a widely reported community observation and appears here only as labelled author guidance.
- That negative prompts matter more on 2.x than on 1.5 rests on Stability's qualitative statement about 2.1 plus community practice, not a published comparison. [S14]
- Off-resolution behaviour (mush below native size, duplication above it) is author guidance, not a documented specification.

## Evidence boundaries

Model identity and documented controls come from the sources above. Suggested canvases, guidance baselines, example prompts and repair strategies are author recommendations. No image inference, latency benchmark, commercial-licence review or provider-account access test was performed while building this package. A model page establishes documentation, not access in a particular account.

For a new or changed capability, revisit the exact model's primary documentation or its archived copy. If sources conflict, retain version and provider scope and disclose the uncertainty. Don't resolve a disagreement by silently substituting another model. Price and rate limits are deliberately omitted because this is a prompt-writing package.

For local checkpoints, preserve the exact version, config and frontend supplied by the user. Browse when asked for current verification or when the embedded facts don't answer a material question; ordinary prompt drafting can use these local references.
