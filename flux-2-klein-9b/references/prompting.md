# FLUX.2 Klein 9B: prompting and refinement

The prompts below are original writing examples, not copied vendor examples or rendered benchmarks. See [capabilities.md](capabilities.md) for version-specific limits and [sources.md](sources.md) for documented facts. The repair advice is author guidance to test against the actual output.

## Model-specific choices

1. Use one strong subject/action sentence followed by a small number of decisive visual constraints.
2. For fast iteration, vary a single axis and keep identity, palette and framing constant.
3. For reference edits, name the changed object and the visual features that must survive; don't describe every unchanged pixel.
4. Put lettered content on a clearly defined surface and avoid adding several competing tiny text regions.
5. If a user is actually running Klein Base 9B, flag the variant difference before prescribing distilled-model settings.

## Copy-ready examples

### Fast visual concept

```text
A small orange robot waters a single potted fern on a sunny balcony. Full robot visible, watering can tilted towards the soil, fern on the right. Rounded ceramic body, simple expressive eyes and a pale blue sky. Soft painted illustration with clean shapes and warm shadows.
```

### Compact product scene

```text
A cream bicycle helmet rests on a dark-green bench beside a folded navy raincoat. Side view with the helmet straps clearly visible. Soft cloudy daylight, fine water droplets on the bench and a quiet blurred park background. Natural product photograph.
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
