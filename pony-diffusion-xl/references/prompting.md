# Pony Diffusion XL: prompting and refinement

The prompts below are original writing examples, not copied vendor examples or rendered benchmarks. See [capabilities.md](capabilities.md) for version-specific limits and [sources.md](sources.md) for documented facts. The repair advice is author guidance to test against the actual output.

## Model-specific choices

1. Keep the full creator quality prefix as the baseline, then write the actual scene in natural language with a few discriminating tags.
2. Choose one source tag matching the requested aesthetic. Pony is not a reason to turn every character into a pony.
3. Use rating_safe for ordinary safe-content examples; preserve the user brief rather than adding sexual or violent content.
4. Use a clear species and anatomy description for anthro versus feral subjects, and state who holds each object.
5. If the result is muddy, check the checkpoint and text-encoder configuration before inflating the prompt or negative list.

## Copy-ready examples

### Cartoon character

```text
score_9, score_8_up, score_7_up, score_6_up, score_5_up, score_4_up, source_cartoon, rating_safe, an adult anthropomorphic badger librarian in a green waistcoat, standing beside a trolley of books, holding one closed red book against the chest, full body, friendly alert expression, warm reading room, clean linework, soft cel shading
```

### Anime scene

```text
score_9, score_8_up, score_7_up, score_6_up, score_5_up, score_4_up, source_anime, rating_safe, an adult courier resting beside a blue bicycle under a station awning, yellow rain jacket, one hand on the handlebars, rainy evening street in the background, three-quarter view, crisp linework, subtle reflections, quiet mood
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

Do not use that example when a border is part of the brief. For Pony V6 XL, keep the creator's empty-negative baseline first. Never add exclusions that contradict requested text, subject anatomy or stylistic features.

## Working from an existing prompt

Extract what is already correct before changing anything. Preserve exact text and identity constraints, remove contradictions, then rewrite only the weak parts. Do not add an unsolicited aesthetic merely to make the prompt longer. When asked for alternatives, vary framing, illumination or medium one at a time so the user can compare meaningful choices.

Use exact-copy checks for lettering and names. Treat supplied output images as evidence of failure; if no result is available, label a diagnosis as a hypothesis. A longer prompt is not automatically a better prompt.
