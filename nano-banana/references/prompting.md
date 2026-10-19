# Nano Banana: prompting and refinement

The prompts below are original writing examples, not copied vendor examples or rendered benchmarks. See [capabilities.md](capabilities.md) for version-specific limits and [sources.md](sources.md) for documented facts. The repair advice is author guidance to test against the actual output.

## Model-specific choices

1. Use a compact scene description with one clear focal subject before adding secondary objects.
2. For a reference-based request, say which input supplies the subject and which supplies the setting. Avoid making all references compete for the same role.
3. For complex lettering, settle the exact copy first, then specify its position, scale and contrast in the image prompt.
4. Keep follow-up edits small. Reintroduce critical identity and product features if the conversation drifts.
5. Treat claims about current events or accurate diagrams as supplied content to verify, rather than assuming Search grounding.

## Copy-ready examples

### Product photograph

```text
A studio photograph of a small ochre ceramic teapot on a pale stone plinth. Three-quarter view, with the spout pointing left and the full handle visible. Soft daylight from the upper left reveals the uneven glaze and a short contact shadow. Quiet warm-grey background and generous space above the lid.
```

### Simple illustrated poster

```text
Create a portrait-format linocut-style poster of a coastal lighthouse at dusk. Navy sea, cream paper and one vermilion accent on the lighthouse door. Place the exact words "COASTAL NIGHTS" in large cream block lettering across the top. Keep the lettering separate from the lighthouse silhouette. The title is the only visible text.
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
