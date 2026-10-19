# FLUX.2 Dev: prompting and refinement

The prompts below are original writing examples, not copied vendor examples or rendered benchmarks. See [capabilities.md](capabilities.md) for version-specific limits and [sources.md](sources.md) for documented facts. The repair advice is author guidance to test against the actual output.

## Model-specific choices

1. Prioritise subject and action, then visual style and context. Add detail only where it resolves an ambiguity.
2. For several inputs, name image 1 as the base scene and state the separate contribution of each remaining input.
3. When transferring a product, preserve geometry, silhouette, label text and material while allowing scene lighting to adapt.
4. Use object-bound colour targets, such as a cobalt-blue chair, rather than an unassigned palette list.
5. Use prose for a simple scene and optional structured sections for a complex layout; avoid inventing weighting or ControlNet syntax.

## Copy-ready examples

### Material and colour

```text
A cobalt-blue enamel camping mug sits on a rough grey stone table. The mug is the only object, placed slightly left of centre with its handle facing right. Its exterior colour target is hex #2457A7, with a cream interior and a thin dark rim. Cool diffuse daylight gives a broad soft reflection on the enamel. Close product photograph, full mug visible.
```

### Editorial composition

```text
A cyclist in a mustard raincoat pauses beside a bicycle at the edge of a small forest clearing. Wide composition, with cyclist and bicycle together in the left third and layers of misty trees across the right. Wet leaves catch subdued morning light. Natural documentary style, calm colours and believable scale.
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
