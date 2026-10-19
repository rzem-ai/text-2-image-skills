# FLUX.1 Dev: prompting and refinement

The prompts below are original writing examples, not copied vendor examples or rendered benchmarks. See [capabilities.md](capabilities.md) for version-specific limits and [sources.md](sources.md) for documented facts. The repair advice is author guidance to test against the actual output.

## Model-specific choices

1. Lead with the main subject and action, then anchor composition, materials and light in connected sentences.
2. Use a clear noun for each object and describe relationships explicitly when more than one subject appears.
3. Keep the essential content near the beginning to reduce damage from text truncation in a constrained workflow.
4. Quote short signage and assign it to a visible surface. Leave long exact typography for a later design stage when fidelity is critical.
5. For source-image regeneration, describe the desired finished scene; preserve structure through the workflow rather than assuming instruction-following editing.

## Copy-ready examples

### Environmental photograph

```text
A weathered green rowboat rests on damp sand beside a tidal creek. The boat fills the lower third, angled from the bottom left towards the centre. Reeds frame the right bank and low morning mist softens the distant trees. Overcast light reveals peeling paint, wet wood and shallow ripples in the creek. Quiet documentary photograph with natural colours.
```

### Short sign

```text
A small timber bookshop on a rainy evening, viewed straight on from across the narrow street. A warm lamp lights the doorway. Above it, a single dark-blue sign reads "NIGHT BOOKS" in large cream capitals. Rain on the pavement reflects the window light. Two potted ferns sit beside the door, one on each side.
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
