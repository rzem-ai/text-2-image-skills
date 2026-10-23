# NoobAI-XL: evidence and maintenance

Checked on 2026-10-23. These embedded references are concise, original summaries with original prompt examples. They are not verbatim copies of creator documentation and do not depend on sibling skill packages.

## Sources

1. [Laxhar NoobAI XL 1.1 model card](https://huggingface.co/Laxhar/noobai-XL-1.1)

   Supports: Epsilon 1.1 identity, Illustrious lineage, Danbooru and e621 training, CFG 5-6, 25-30 steps, Euler a, resolution list, prefix, negative, caption order, quality and period tags. [N1] The 1.0 card ([Laxhar/noobai-XL-1.0](https://huggingface.co/Laxhar/noobai-XL-1.0)) gives the same settings and names Illustrious-xl early release v0 as the fine-tune source.

2. [Laxhar NoobAI XL V-Pred 1.0 model card](https://huggingface.co/Laxhar/noobai-XL-Vpred-1.0)

   Supports: V-Pred identity, Diffusers scheduler override, CFG 4-5, 28-35 steps, Euler-only warning, aesthetic and year tags, `artist:` example syntax, ControlNet pointer, licence terms. [N2]

3. [Civitai creator listing for NoobAI-XL (NAI-XL)](https://civitai.com/models/833294), read through the public API search endpoint `https://civitai.com/api/v1/models?query=NoobAI-XL` because the direct model endpoint was region-blocked

   Supports: Version history and release notes, including Epsilon 1.1 details, V-Pred 1.0 sampler and CFG-rescale advice, 0.9R cosplay branch and roughly-80-image concept threshold for 1.0. [N3]

4. [NoobAI-XL ControlNet collection](https://civitai.com/models/929685) via [its public API record](https://civitai.com/api/v1/models/929685)

   Supports: ControlNet version list, naming scheme and prediction-type matching advice. [N4]

5. [Euge's NoobAI ControlNet repositories on Hugging Face](https://huggingface.co/Eugeoter/noob-sdxl-controlnet-canny)

   Supports: Hugging Face distribution of the canny, depth, normal, lineart, manga line, softedge, scribble and tile ControlNets. Cards are metadata-only. [N5]

6. [NoobAI-XL ControlNet OpenPose listing](https://civitai.com/models/962537) and [Laxhar/noob_openpose](https://huggingface.co/Laxhar/noob_openpose)

   Supports: Separate OpenPose ControlNet. [N6]

## Conflicts and unverified points

- V-Pred 1.0 sampler: the model card says only Euler works properly; the later 1.0 release note says most samplers work except Karras schedules and suggests Euler or DDIM. This package treats Euler as the safe default and reports the conflict rather than choosing.
- CFG rescale 0.2 appears only in the V-Pred 1.0 release note, not on the model card.
- Period tags: both cards list 2014 under both `early` (2011-2014) and `mid` (2014-2017).
- Rating tags: the cards only use `safe` (prefix) and `nsfw` (negative). Additional rating tags (`general`, `sensitive`, `explicit`) are commonly attributed to the creator guidebook (https://civitai.com/articles/8962), which returned HTTP 403 and wasn't verified.
- Artist syntax: the caption template lists `<artists>` without a prefix, while the creator example uses `artist:name`. Both appear in community use; neither is proven superior here.
- No `v-` ControlNet versions were listed at this check, so V-Pred ControlNet compatibility is unverified.
- The Diffusers-format V-Pred repo's bundled scheduler config declares `epsilon`; the card's own example overrides it.
- The IP-Adapter mentioned in release notes was found only in community mirrors, not a Laxhar repo.

## Evidence boundaries

Model identity and documented settings come from the sources above. Suggested tag choices, example prompts and repair strategies are author recommendations. No image inference, latency benchmark or commercial-licence review was performed. Note that the licence (fair-ai-public-license-1.0-sd plus Laxhar terms) prohibits commercial use and requires derivatives to be open; flag this when a user describes commercial work, without giving legal advice.

For a new or changed capability, revisit the exact checkpoint's primary documentation. If sources conflict, retain version scope and disclose the uncertainty. Don't resolve a disagreement by silently substituting another model. Price and rate limits are deliberately omitted because this is a prompt-writing package.

For local checkpoints, preserve the exact version, prediction type and frontend supplied by the user. Browse when asked for current verification or when the embedded facts don't answer a material question; ordinary prompt drafting can use these local references.
