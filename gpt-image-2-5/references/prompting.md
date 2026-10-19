# GPT Image 2.5: prompting and refinement

The prompts below are original writing examples, not copied vendor examples or rendered benchmarks. See [capabilities.md](capabilities.md) for version-specific limits and [sources.md](sources.md) for documented facts. The repair advice is author guidance to test against the actual output.

## Model-specific choices

1. Write the same clear visual brief for either variant; don't invent separate magic words for Flare and Sunburst.
2. For dense layouts, define reading order, region boundaries, exact copy and which decorative elements may overlap.
3. For repeated edits, keep a list of approved invariants and refer back to the original reference when drift appears.
4. For asset cutouts, describe the complete silhouette, edge materials and margin as well as the transparent background requirement.
5. When comparing prompt revisions, hold variant, dimensions and quality constant if the user has rendered examples. Distinguish a plausible rewrite from a measured improvement.

## Copy-ready examples

### Transparent asset

```text
Create an isolated embroidered patch shaped like a small mountain hut with a red roof, two cream windows and a dark pine tree beside it. Thick stitched border following the complete silhouette, visible thread texture and a simple readable shape. Centre the entire patch with clear space around every edge. Transparent background; no printed words.
```

### Dense information layout

```text
Create a clean portrait workshop poster with three horizontal regions. Top: the exact heading "REPAIR WEEKEND" in large dark-green sans-serif type. Middle: an original illustration of a workbench with one screwdriver, one lamp and one open toolbox. Bottom: the exact lines "Saturday 10 am" and "Bring one small item" on separate lines. Warm ivory paper, restrained orange accents, equal side margins and no overlapping lettering.
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
