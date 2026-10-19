# SDXL: prompting and refinement

The prompts below are original writing examples, not copied vendor examples or rendered benchmarks. See [capabilities.md](capabilities.md) for version-specific limits and [sources.md](sources.md) for documented facts. The repair advice is author guidance to test against the actual output.

## Model-specific choices

1. Build a compact positive prompt: subject, action, framing, medium, lighting and important materials.
2. Use either concise phrases or short natural sentences. Avoid a large stack of overlapping quality adjectives.
3. Keep actual exclusions in a separate negative prompt. Don't add text to the negative prompt when the image needs lettering.
4. When exact wording or geometric diagrams are essential, describe the limitation and reserve a clean region for later typesetting if acceptable.
5. For I2I, describe the desired final image. Denoise strength, masks and structural controls belong to the workflow notes.

## Copy-ready examples

### Photographic scene

```text
Environmental photograph of a small timber cabin beside a still alpine lake, cabin in the left third, distant dark pines, early morning mist, soft cool light, warm glow through one window, realistic weathered wood, calm reflections, wide composition
```

### Illustration

```text
Gouache illustration of an adult botanist examining a fern in a glasshouse, waist-up composition, short dark hair, olive work jacket, fern held clearly in one hand, soft green glasshouse background, diffused daylight, textured brushwork, restrained earthy palette
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
