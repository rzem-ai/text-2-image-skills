# NoobAI-XL: identity and constraints

Reference check: 2026-10-23. Bracketed evidence labels resolve in [sources.md](sources.md). Tables mix documented facts with explicitly labelled author suggestions. Settings are context for writing prompts, not instructions to execute a generation workflow.

## Model identity

NoobAI-XL is Laxhar Lab's SDXL-architecture anime fine-tune, trained from Illustrious-xl early release v0 on the full Danbooru and e621 datasets (Danbooru to roughly 2024-10-23) with native tag captions. [N1, N3] Two lines exist and are not interchangeable:

| Variant | Identifier | Prediction | Notes |
| --- | --- | --- | --- |
| Epsilon-pred 1.1 (baseline here) | `Laxhar/noobai-XL-1.1` | Epsilon | Continued 1.0 for two epochs; strengthened natural-language training. Works with standard SDXL tooling. [N1, N3] |
| V-Pred 1.0 | `Laxhar/noobai-XL-Vpred-1.0` | V-prediction, zero terminal SNR | Fine-tuned from the epsilon 1.0 line; adds natural-language captions. Needs a v-prediction-aware frontend. [N2, N3] |

Earlier epsilon (0.5-1.0) and v-pred (test, 0.5-0.9R) checkpoints, the 0.9R cosplay-leaning branch and community merges behave differently; preserve whichever the user names. Illustrious base, Pony Diffusion and generic SDXL use different tag conventions. [N3]

## Prompt-relevant settings

| Concern | Epsilon-pred 1.1 | V-Pred 1.0 |
| --- | --- | --- |
| Sampler | Euler a. [N1] | Model card: Euler, other samplers "will not work properly". Release note: most samplers work except Karras schedules; Euler or DDIM suggested. See conflicts in [sources.md](sources.md). [N2, N3] |
| CFG | 5-6. [N1] | 4-5. [N2] |
| CFG rescale | Not documented as needed. | Release note recommends dynamic CFG / CFG rescale around 0.2 against over-saturation or greyness. [N3] |
| Steps | 25-30. [N1] | 28-35. [N2] |
| Canvas | Total area near 1024x1024: 768x1344, 832x1216 (preferred), 896x1152, 1024x1024, 1152x896, 1216x832, 1344x768. [N1, N2] | Same list. [N1, N2] |
| Scheduler config | Standard. | The Diffusers folder's bundled scheduler config reads `epsilon`; the card's example overrides it with `prediction_type="v_prediction"` and `rescale_betas_zero_snr=True`. A muddy or grey result often means this override is missing, not that the prompt is weak. [N2] |

Both cards give the same prompt prefix and negative prompt; see [prompting.md](prompting.md). Quality tags are popularity percentiles with recency decay, not technical-quality labels: masterpiece (>95th), best quality (85th-95th), good quality, normal quality, worst quality (<=30th). Aesthetic tags `very awa` (top 5% by waifu-scorer) and `worst aesthetic` (bottom 5%) are documented on the V-Pred card only, which truncates the rest of the list; `very awa` is an optional addition to the prefix, not part of it. [N1, N2]

Date tags: `year 2021` style year tags, plus period tags old (2005-2010), early (2011-2014), mid (2014-2017), recent (2018-2020), newest (2021-2024). [N1, N2]

## What wording cannot guarantee

A prompt cannot switch prediction type, fix a missing v-prediction scheduler, attach an absent ControlNet input, guarantee exact typography or guarantee a character the dataset barely contains. Laxhar describes 1.0 as supporting characters and styles with roughly 80 or more Danbooru solo images; rarer concepts may need a LoRA. [N3] Rating tags express a content preference, not a safety filter.

Use the user's selected checkpoint and installed frontend as the scope of any refinement. Merges and LoRAs can change tag response; a version-specific setting should not be promoted into a family-wide rule.
