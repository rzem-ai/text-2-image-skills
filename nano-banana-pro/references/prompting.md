# Nano Banana Pro: prompting and refinement

The prompts below are original writing examples, not copied vendor examples or rendered benchmarks. See [capabilities.md](capabilities.md) for version-specific limits and [sources.md](sources.md) for documented facts. The repair advice is author guidance to test against the actual output.

## Model-specific choices

1. Write a visual brief with labelled sections when it helps separate content, layout, typography and preservation constraints.
2. For infographics, supply the actual labels and relationships. Never let attractive layout substitute for correct facts.
3. Assign each reference a function: identity, product geometry, colour, composition or style. Say which reference controls a conflict.
4. Quote every required text string exactly and specify reading order. Localisation must preserve meaning and layout, not merely replace words.
5. Describe reasoning outcomes as visible requirements. A request to think harder is less useful than a clear hierarchy and explicit spatial relationships.

## Copy-ready examples

### Exhibition graphic

```text
Create a restrained exhibition poster. A single suspended brass mobile occupies the right two-thirds against an off-white wall, casting a soft directional shadow. On the left, set the exact title "BALANCE" in large charcoal sans-serif type, with "Studies in motion" directly below in smaller type. Align both lines to the same left edge. Leave a wide outer margin and keep all lettering clear of the sculpture.
```

### Grounded diagram from supplied facts

```text
Create an educational diagram showing three labelled stages from left to right: "COLLECT", "FILTER", "STORE". Show rain entering a roof gutter, travelling through a filter, then entering a covered water tank. Use one blue arrow between each stage. Cream background, precise dark outlines and large labels. Show only the supplied three stages and their labels.
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
