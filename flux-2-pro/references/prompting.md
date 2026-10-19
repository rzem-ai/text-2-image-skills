# FLUX.2 Pro: prompting and refinement

The prompts below are original writing examples, not copied vendor examples or rendered benchmarks. See [capabilities.md](capabilities.md) for version-specific limits and [sources.md](sources.md) for documented facts. The repair advice is author guidance to test against the actual output.

## Model-specific choices

1. Write a visual brief with the important subject first and clear spatial relationships between the remaining elements.
2. For branded layouts, quote text, specify hierarchy and attach each requested colour to an object or text element.
3. If the prompt is already precise, mention the optional expansion control as a settings note, not as a sentence for the model to render.
4. For several references, declare the base image and which reference contributes identity, product, style or setting. Resolve conflicting requirements explicitly.
5. Keep fixed and preview endpoints separate in evaluation notes; matching seeds alone cannot establish identical outputs across different weights.

## Copy-ready examples

### Brand still life

```text
Create a clean still-life photograph of a matte forest-green refill bottle on a warm ivory shelf. The bottle colour target is hex #234D3C. A small cream label on its front reads "REFILL" in large dark lettering. A soft shadow falls rightwards from a window light on the left. Place the bottle in the right third and leave the left half clear for copy. Restrained premium design.
```

### Graphic layout

```text
Create a landscape event card with a large abstract orange sun occupying the right third. On the left, place the exact words "SLOW SUNDAY" in large dark-navy rounded lettering on two lines. Pale peach background, one olive-green leaf shape below the sun, and a generous border around the whole layout. The title is the only text.
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
