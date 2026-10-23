# Stable Diffusion 3.5: evidence and maintenance

Checked on 2026-10-23. These embedded references are concise, original summaries with original prompt examples. They are not verbatim copies of vendor manuals and do not depend on sibling skill packages.

## Sources

1. [SD3.5 Large model card](https://huggingface.co/stabilityai/stable-diffusion-3.5-large) [S1]

   Supports: MMDiT identity, three encoders, the 77-token CLIP context, T5 training at 77/256 tokens, 28-step examples with guidance 3.5 or 4.5 and `max_sequence_length` 512 for a long prompt.

2. [SD3.5 Large Turbo model card](https://huggingface.co/stabilityai/stable-diffusion-3.5-large-turbo) [S2]

   Supports: ADD distillation, the 4-step baseline at guidance 0.0 and shared encoder details.

3. [SD3.5 Medium model card](https://huggingface.co/stabilityai/stable-diffusion-3.5-medium) [S3]

   Supports: MMDiT-X, progressive training up to 1440 pixels, the 40-step/4.5 baseline, the warning about edge artefacts past 256 T5 tokens, a different data distribution from Large and the Skip Layer Guidance recommendation.

4. [Diffusers Stable Diffusion 3 pipeline documentation](https://huggingface.co/docs/diffusers/main/en/api/pipelines/stable_diffusion/stable_diffusion_3) and [Diffusers SD3 pipeline source](https://github.com/huggingface/diffusers/tree/main/src/diffusers/pipelines/stable_diffusion_3) [S4]

   Supports: per-encoder `prompt`/`prompt_2`/`prompt_3`, `max_sequence_length` default 256, negatives ignored below guidance 1, dropping T5, Skip Layer Guidance values for Medium, IP-Adapter use, and the img2img and inpaint pipelines (strength default 0.6, white-repaint mask).

5. [Stability AI SD3.5 announcement](https://stability.ai/news-updates/introducing-stable-diffusion-3-5) [S5]

   Supports: parameter counts, the about-1MP Large target, the 0.25-2MP Medium range, release dates (22 and 29 October 2024), diversity across seeds and the SD3 Medium context.

6. [Stability API SD3.5 reference](https://docs.stability.ai/api-reference/generate/stable-diffusion-35) and [API release notes](https://docs.stability.ai/release-notes) [S6]

   Supports: `sd3.5-large`/`-large-turbo`/`-medium` model values, text-to-image and image-to-image modes with `strength`, `cfg_scale` defaults (4 for Large and Medium, 1 for Turbo and Flash), aspect ratios, 1MP output, `style_preset`, `(word:weight)` syntax, the 10,000-character prompt field and SD3.0 re-routing from 17 April 2025.

7. [Stability API documentation index](https://docs.stability.ai/llms.txt) [S7]

   Supports: Stable Image Ultra and Core descriptions and the list of hosted edit and control services.

8. [Stability SD3.5 prompt guide (archived copy)](https://web.archive.org/web/20260302001715/https://stability.ai/learning-hub/stable-diffusion-3-5-prompt-guide) [S8]

   Supports: style, subject and action, composition, lighting and colour, technical terms, quoted short text and negative prompt advice. The live page returned 404 on the check date; the summary is based on the March 2026 archive.

9. ControlNet cards: [Canny](https://huggingface.co/stabilityai/stable-diffusion-3.5-large-controlnet-canny), [Depth](https://huggingface.co/stabilityai/stable-diffusion-3.5-large-controlnet-depth) and [Blur](https://huggingface.co/stabilityai/stable-diffusion-3.5-large-controlnet-blur) [S9]

   Supports: Large-only ControlNets, suggested starting strengths, Euler with 50-60 steps, external preprocessing and the Blur model's Tile ControlNet lineage. Stability's ControlNet announcement wasn't fetched, so any stronger claim about Blur's intended use is unverified here.

## Conflicts and unverified points

- **SD 3.5 Flash.** The hosted SD3.5 page describes Flash as a 4-step distilled Medium and lists a price and a `cfg_scale` default, but the same page's `model` enum lists only the three main variants. No release note or open checkpoint was found. Treat Flash as hosted-only and unconfirmed; this package doesn't give Flash-specific advice.
- **Medium architecture wording.** The Medium card says dual attention blocks in the first 12 layers in one section and self-attention modules in the first 13 layers in another. This doesn't affect prompt writing.
- **Diffusers defaults.** The `__call__` signature defaults to 28 steps and guidance 7.0 while a docstring says 50 steps. Both are pipeline defaults, not SD3.5 recommendations; prefer the model-card baselines.
- **Diffusers family list.** The Diffusers page lists SD3 Medium, 3.5 Large and Large Turbo as the official SD3 family and leaves out 3.5 Medium, though the Medium card uses the same pipeline.
- **Turbo negatives on the API.** The API doesn't say whether Turbo's default `cfg_scale` of 1 disables the negative prompt. The local behaviour (ignored below 1) is documented; the hosted behaviour is inferred.
- **Hosted edit services.** Their underlying model isn't stated, so this package doesn't call them SD3.5 features.

## Evidence boundaries

Model identity and documented controls come from the sources above. Suggested composition, example prompts and repair strategies are author recommendations. No image inference, latency benchmark, commercial-licence review or provider-account access test was performed while building this package. A model page establishes documentation, not access in a particular account.

For a new or changed capability, revisit the exact model's primary documentation. If sources conflict, retain version and provider scope and disclose the uncertainty. Don't resolve a disagreement by silently substituting another model. Price and rate limits are deliberately omitted because this is a prompt-writing package.

For local checkpoints, preserve the exact variant and frontend supplied by the user. For hosted use, preserve the exact `model` value and distinguish the SD3.5 endpoint from Stable Image Ultra or Core. Browse when asked for current verification or when the embedded facts don't answer a material question; ordinary prompt drafting can use these local references.
