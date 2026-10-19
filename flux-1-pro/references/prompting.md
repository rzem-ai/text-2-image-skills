# FLUX.1 Pro: prompting and refinement

The prompts below are original writing examples, not copied vendor examples or rendered benchmarks. See [capabilities.md](capabilities.md) for version-specific limits and [sources.md](sources.md) for documented facts. The repair advice is author guidance to test against the actual output.

## Model-specific choices

1. Write a self-contained description of the finished image with concrete subject, action, composition and illumination.
2. Avoid using later FLUX features as a reason to promise exact colour reproduction, multi-reference editing or reliable long text.
3. If the user supplies a provider screenshot or settings, record that scope and use only the controls actually shown.
4. For a request described as image-to-image, establish whether the user actually means original Pro, Ultra, Kontext or a provider wrapper before claiming reference preservation.
5. If only a text prompt is wanted, deliver it immediately with the model-availability caveat kept outside the copy-ready block.

## Copy-ready examples

### Architectural concept

```text
A compact timber reading room cantilevers above a rocky inlet. Three-quarter exterior view from the water, showing the long horizontal window and the entrance on the right. Pale timber cladding, a dark metal roof and warm interior light at blue hour. The rock shelf remains clearly visible beneath the structure. Restrained architectural visualisation with believable materials.
```

### Material study

```text
A close product photograph of a brushed aluminium desk lamp with a deep-red fabric cable. The lamp stands on a charcoal surface, with the shade turned slightly down and left. One broad softbox reflection defines the metal curve. The red cable makes a single loose loop in the foreground. Clean dark background and precise material contrast.
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
