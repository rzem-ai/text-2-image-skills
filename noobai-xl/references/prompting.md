# NoobAI-XL: prompting and refinement

The prompts below are original writing examples, not copied creator examples or rendered benchmarks. See [capabilities.md](capabilities.md) for variant-specific limits and [sources.md](sources.md) for documented facts. The repair advice is author guidance to test against the actual output.

## Creator conventions

Caption order from the model cards: `<1girl/1boy/1other/...>, <character>, <series>, <artists>, <special tags>, <general tags>, <other tags>`. [N1, N2] Creator prompt prefix: `masterpiece, best quality, newest, absurdres, highres, safe,`. [N1, N2] The cards don't fix where the prefix sits relative to the caption; the creator's own example puts quality tags first. Keeping the prefix at the start is a convention, not a documented rule.

Creator negative prompt, identical for both variants: [N1, N2]

```text
nsfw, worst quality, old, early, low quality, lowres, signature, username, logo, bad hands, mutated hands, mammal, anthro, furry, ambiguous form, feral, semi-anthro
```

## Model-specific choices

1. Use Danbooru tag spelling with spaces rather than underscores for general tags, and escape literal parentheses in A1111-style frontends: `hu tao \(genshin impact\)`. The creator example writes artists as `artist:name`. [N2]
2. Use a subject-count tag (`1girl`, `1boy`, `1other`, `2girls`, `solo`) first; it anchors composition more reliably than prose.
3. Use canonical character and series tags only when the user names them. For original characters, describe visible traits with general tags and add `original` if helpful.
4. Short natural-language phrases can follow the tags; V-Pred 1.0 and Epsilon 1.1 were trained with more natural language, but tags remain the primary vocabulary. [N1, N2, N3]
5. The negative's `mammal, anthro, furry, feral, semi-anthro` terms suppress e621-style content. Remove them when the brief asks for an animal, anthro or creature subject, or they will fight the prompt.
6. `newest` and `old`/`early` steer era style. Swap `newest` for `recent`, `mid` or a `year 2016` tag when the user wants an older look, and remove the matching negative term.
7. Keep `safe` in the prefix and `nsfw` in the negative for general-audience work. Laxhar's Civitai guidebook reportedly documents further rating tags (`general`, `sensitive`, `nsfw`, `explicit`); that guide wasn't retrievable, so treat those as unverified and rely on `safe`.

## Copy-ready examples

### Original character, Epsilon 1.1 or V-Pred 1.0

```text
masterpiece, best quality, newest, absurdres, highres, safe, 1girl, solo, original, adult, mature female, long black hair, low ponytail, green eyes, white lab coat over navy sweater, holding clipboard, standing, greenhouse, potted plants, sunlight through glass roof, looking at viewer, slight smile, cowboy shot, depth of field
```

### Two adults, scene with clear ownership

```text
masterpiece, best quality, newest, absurdres, highres, safe, 1boy, 1girl, adult, train station platform, evening, rain, the man has short brown hair and a grey trench coat and holds a black umbrella, the woman has short silver hair and a yellow raincoat and holds a paper ticket, standing side by side, wide shot, reflections on wet ground, city lights, bokeh
```

### Era-style landscape, no characters

```text
masterpiece, best quality, mid, year 2016, absurdres, highres, safe, no humans, scenery, mountain village, terraced fields, stone stairs, cherry blossoms, morning mist, blue sky, clouds, wide shot, detailed background
```

The era example uses `mid`, which doesn't conflict with the creator negative's `old, early`. Remove `early` from the negative only when the user wants a 2011-2014 look, and `old` for 2005-2010.

## Repair the actual failure

| Observed problem | Useful revision | Keep outside the prompt |
| --- | --- | --- |
| Grey, washed-out or noisy output on V-Pred | Don't add quality tags; this is usually configuration. | Confirm v-prediction and zero-SNR scheduler, non-Karras sampler, CFG 4-5, CFG rescale near 0.2. [N2, N3] |
| Over-saturated or burnt colours | Remove stacked colour and contrast tags; keep one palette cue. | Lower CFG; on V-Pred apply CFG rescale. [N3] |
| Wrong character or blended costume | Use the exact Danbooru character and series tags, then list the outfit pieces explicitly. | Whether the character has enough training images; a LoRA may be needed. [N3] |
| Attributes swap between two subjects | Use count tags, then one clause per subject with explicit possession. | Regional prompting or inpainting if prompt binding stays unreliable. |
| Unwanted anthro or animal features | Keep the creator's furry-suppression negatives and describe human features (skin, ears) explicitly. | Whether a LoRA introduces e621 bias. |
| Requested animal subject suppressed | Remove `mammal, anthro, furry, feral` from the negative. | Nothing; this is a prompt conflict. |
| Dated art style | Ensure `newest` is present and `old, early` are in the negative. | Merges trained on older data. |
| Signature or watermark | Keep `signature, username, logo` negatives; add `watermark, artist name` if still visible. | Inpaint the corner afterwards. |
| Cropped subject | Add `full body` and named extremities (`shoes`, `feet out of frame` in the negative). | Canvas ratio; use a portrait resolution such as 832x1216. |

## Working from an existing prompt

Extract the tags that already work before changing anything. Preserve character, series and artist tags exactly as supplied, remove contradictions (two hair colours, `solo` with `2girls`), then rewrite only the weak parts. Don't add unsolicited artist tags to push a style. When asked for alternatives, vary framing, lighting or era tag one at a time.

Treat supplied outputs as evidence of failure; if no result is available, label a diagnosis as a hypothesis. A longer tag list is not automatically better, and SDXL CLIP context is limited, so put essential tags early.
