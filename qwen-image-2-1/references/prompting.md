# Qwen Image 2.1: prompting and refinement

The prompts below are original writing examples, not copied vendor examples or rendered benchmarks. See [capabilities.md](capabilities.md) for version-specific limits and [sources.md](sources.md) for documented facts. The repair advice is author guidance to test against the actual output.

## Model-specific choices

1. Write natural-language relationships with explicit counts, positions and ownership of objects.
2. For lettering, quote exact copy and specify the physical surface, hierarchy and reading order. Preserve diacritics and the user language.
3. For alpha assets, use the native RGBA wording and describe the complete silhouette, clear margins and any semitransparent materials.
4. For references, identify which image supplies subject identity, product geometry, pose or style. Don't fabricate unseen appearance from a name.
5. Avoid phrases pretending to tune the VAE or encoder. Steps, quantisation and resolution are runtime notes, not visual instructions.

## Copy-ready examples

### RGBA asset

```text
This is an RGBA image with transparency. A small hand-painted ceramic owl ornament, front view, warm cream glaze with dark blue wing markings and two tiny ochre feet. The complete ornament is centred with clear space around its silhouette. Preserve fine glazed edges and a gentle highlight on the curved body. The image has alpha channel and the background is transparent.
```

### Typography

```text
Create a portrait book-fair poster with a detailed illustration of a tiny bookshop inside an open book. Cream paper, forest-green ink and restrained red accents. Across the top, set the exact words "SMALL PRESS FAIR" in large readable serif capitals. Beneath the illustration, centre the exact line "Independent books, shared stories" in smaller type. Keep both text regions separate from the illustration.
```

## Repair the actual failure

| Observed problem | Useful revision | Keep outside the prompt |
| --- | --- | --- |
| Missing object or wrong count | State the exact count and anchor each object in the scene. Reduce competing secondary detail. | Whether the frontend truncated the prompt. |
| Attributes swap between subjects | Use distinct nouns and one sentence per subject, with explicit position and ownership. | Reference ordering and any structural controls. |
| Wrong text | Reassert exact copy, its surface, hierarchy and reading order. Simplify competing lettering. | Whether the current output resolution can carry the required density. |
| Flat or synthetic appearance | Specify a plausible light source, material response and selective natural texture. | Model/checkpoint, guidance and any enhancement settings. |
| Unwanted restyling | Reassert the intended medium and remove conflicting style cues. | Whether a style LoRA or reference is dominating. |
| Cropped subject | Request the complete silhouette, named extremities and comfortable margins. | Canvas ratio and source crop. |

## Working from an existing prompt

Extract what is already correct before changing anything. Preserve exact text and identity constraints, remove contradictions, then rewrite only the weak parts. Do not add an unsolicited aesthetic merely to make the prompt longer. When asked for alternatives, vary framing, illumination or medium one at a time so the user can compare meaningful choices.

Use exact-copy checks for lettering and names. Treat supplied output images as evidence of failure; if no result is available, label a diagnosis as a hypothesis. A longer prompt is not automatically a better prompt.
