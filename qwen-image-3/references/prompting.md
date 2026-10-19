# Qwen Image 3: prompting and refinement

The prompts below are original writing examples, not copied vendor examples or rendered benchmarks. See [capabilities.md](capabilities.md) for version-specific limits and [sources.md](sources.md) for documented facts. The repair advice is author guidance to test against the actual output.

## Model-specific choices

1. For complex images, organise the brief into spatial regions with exact content and reading order for each.
2. Use supplied source text and data verbatim for newspapers, posters or diagrams. Rich world knowledge is not proof of factual accuracy.
3. For multilingual layouts, retain exact characters and specify each text region separately. Don't translate labels unless asked.
4. Keep optional negative text separate from the positive prompt and limit it to material exclusions.
5. When a precise brief gains unwanted additions, identify automatic prompt enhancement as a possible source and suggest reviewing that setting outside the prompt.

## Copy-ready examples

### Information-rich poster

```text
Create a portrait community garden poster on warm ivory paper with three clearly separated regions. Top: the exact heading "GROW TOGETHER" in large forest-green lettering. Middle: a clean illustration of two raised beds containing tomatoes, lettuce and marigolds, with a watering can beside the left bed. Bottom: the exact lines "Seed swap" and "Sunday 9 am" on separate lines. Use generous margins and a small terracotta accent. Keep all text readable and do not add other words.
```

### Multilingual graphic

```text
Create a square reading-club card with a small original illustration of an open book in the centre. At the top, place the exact Chinese text "一起读书" in large dark-blue characters. At the bottom, place the exact English text "READ TOGETHER" in smaller dark-blue capitals. Pale cream background, one red bookmark and broad margins. Keep both languages on their specified lines, separate from the illustration.
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
