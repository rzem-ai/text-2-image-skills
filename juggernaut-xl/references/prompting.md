# Juggernaut XL: prompting and refinement

The prompts below are original writing examples, not copied vendor examples or rendered benchmarks. See [capabilities.md](capabilities.md) for version-specific limits and [sources.md](sources.md) for documented facts. The repair advice is author guidance to test against the actual output.

## Model-specific choices

1. Use concrete photographic language for photo briefs: subject, viewpoint, one plausible light source, materials and background depth.
2. Describe visible skin or fabric texture when needed; avoid adding beauty-retouching terms to a documentary request.
3. For an illustration request, preserve that medium instead of forcing the family photorealistic bias into the prompt.
4. Keep negative prompts short and tied to observed failures. A copied list of dozens of defects can change an otherwise successful result.
5. If a supplied prompt performs poorly, check the exact XL checkpoint and frontend before rewriting all of its content.

## Copy-ready examples

### Portrait

```text
Candid waist-up photograph of an adult ceramic artist in a working studio, charcoal apron over a faded blue shirt, hands resting naturally on a workbench, clay dust on the apron, soft side light from a large north-facing window, shelves of unfinished bowls softly out of focus, natural skin texture, understated colours
```

### Interior

```text
Interior photograph of a small timber reading room, low oak shelves along the left wall, one olive armchair beside a tall window on the right, folded cream throw on the chair, overcast daylight, soft shadow detail, visible wood grain and woven fabric, level camera, quiet lived-in atmosphere
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

## Negative prompt use

Keep exclusions separate when the selected surface supports a negative field. Start empty unless there is a concrete reason to add one. For an observed unwanted border, a focused candidate is:

```text
decorative frame, border
```

Do not use that example when a border is part of the brief. Never add exclusions that contradict requested text, subject anatomy or stylistic features.

## Working from an existing prompt

Extract what is already correct before changing anything. Preserve exact text and identity constraints, remove contradictions, then rewrite only the weak parts. Do not add an unsolicited aesthetic merely to make the prompt longer. When asked for alternatives, vary framing, illumination or medium one at a time so the user can compare meaningful choices.

Use exact-copy checks for lettering and names. Treat supplied output images as evidence of failure; if no result is available, label a diagnosis as a hypothesis. A longer prompt is not automatically a better prompt.
