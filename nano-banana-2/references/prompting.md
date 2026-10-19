# Nano Banana 2: prompting and refinement

The prompts below are original writing examples, not copied vendor examples or rendered benchmarks. See [capabilities.md](capabilities.md) for version-specific limits and [sources.md](sources.md) for documented facts. The repair advice is author guidance to test against the actual output.

## Model-specific choices

1. Prioritise the scene and its composition, then use precise sentences for type, colour and reference roles.
2. For an extreme panorama, describe foreground spacing and left-to-right progression; avoid squeezing a square composition into a banner.
3. Keep subject features stable across variants and vary one visual axis, such as lighting or setting.
4. Supply exact translated copy where correctness matters. Keep language instructions separate from instructions about the visual style.
5. Use the requested resolution as context for detail density; a smaller draft should carry fewer labels and larger type.

## Copy-ready examples

### Panoramic banner

```text
Create an extremely wide coastal banner. At the far left, a small white lighthouse stands on a low headland. Long horizontal bands of dark teal water lead across the middle to pale morning mist at the right. A single coral fishing boat sits just right of centre. Flat screen-printed shapes, subtle paper grain and a calm horizon. Leave the upper third visually quiet.
```

### Localised shop graphic

```text
Design a portrait bakery sign with a hand-painted illustration of three golden croissants on a blue plate. Above the plate, the exact words "FRESH EACH MORNING" appear in large cream lettering. Below it, place "Baked here" in a smaller handwritten style. Warm brown background, clear separation between illustration and text, and comfortable margins.
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
