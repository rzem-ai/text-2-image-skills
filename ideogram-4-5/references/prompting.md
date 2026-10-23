# Ideogram 4.5: prompting and refinement

The prompts below are original writing examples, not copied vendor examples or rendered benchmarks. See [capabilities.md](capabilities.md) for version-specific limits and [sources.md](sources.md) for documented facts. The repair advice is author guidance to test against the actual output.

## Model-specific choices

1. Write in sentences, main idea first. A useful order is image type and subject, subject details and any quoted text, pose or action, secondary elements, setting, light and atmosphere, framing, then finish. Omit parts the image doesn't need. [I3]
2. Describe what can be seen. Replace "beautiful" or "modern" with a medium, technique, material or colour. Tie abstract ideas to a visible pose, object or place. [I3, I13]
3. Phrase exclusions positively: "an empty platform with one bench" rather than "no people". There is no negative-prompt field on 4.5. [I13]
4. Keep settings out of the prose. Ratio, size, quality, background, seed and image count are controls; `--ar`, `::2` and bracket weights are just words. [I3]
5. Avoid contradictions such as "minimal but intricately detailed"; pick one direction. Move a neglected detail earlier or describe it more fully rather than repeating adjectives. [I13]
6. For an approved or exact-copy prompt, note "Magic Prompt off" outside the prompt so the wording isn't expanded. [I2, I5]

## Typography

Ideogram's strength is integrated lettering, but it is still generated, not typeset. [I4]

- Put the exact words in double quotation marks, with intended spelling and capitals, and mention them early.
- Say where each block sits and on what surface: "printed across the top of the tote bag", "neon tube lettering above the doorway".
- Describe letterforms by weight, shape and mood ("heavy condensed sans-serif capitals", "thin formal script with flourishes") rather than relying on a font name.
- With several blocks, give each its own words, style and position, in reading order from top to bottom.
- Keep copy short and the surrounding scene calm. Push body copy, legal text and long passages to a design tool or a Studio text layer.
- Non-Latin scripts and accented letters are less reliable; keep them to a word or two and warn the user.
- For logos: brand name in quotes, one icon, one or two lines of text, two or three named colours. "Flat vector" describes appearance; the output is still a raster. Note Background: Transparent separately when needed. [I19]

## Plain-language examples

### Exact-copy poster

```text
A screen-printed concert poster with the headline "LOW TIDE SOCIETY" in tall condensed cream sans-serif capitals across the top quarter. Beneath it, a flat illustration of a lone surfer carrying a longboard along a dark teal shoreline at dusk, with a large peach sun sitting on the horizon. Across the bottom edge, "FRIDAY 14 NOV · THE BOATSHED" in small cream capitals on one line. Two-tone ink with slight misregistration and visible paper grain. Generous margins around both text blocks and no other lettering.
```

### Product label

```text
A product photograph of a squat amber glass jar of honey on a weathered grey timber bench, eye level, centred. The jar has a plain kraft paper label that reads "BUSH HONEY" in bold black slab-serif capitals, with "Raw · Unfiltered" in small italic serif beneath. A wooden honey dipper rests against the jar, and a thin golden drip runs down one side. Soft morning light from the left, warm highlights in the glass and a short soft shadow to the right. Shallow depth of field with a blurred eucalyptus garden behind.
```

### Logo

```text
A flat minimal logo for a bicycle repair shop called "Spoke & Sprocket". A simple circular emblem of a single bicycle gear with a spanner crossing it, drawn in even bold lines, above the name in rounded geometric sans-serif letters. Two colours only: deep navy and warm orange on a plain off-white field. Clean edges, balanced spacing, nothing else in the frame.
```

Settings outside the prompt for the logo: 1:1, Magic Prompt off, Background Transparent if a cutout is wanted.

## Structured JSON prompts

Use JSON when several text blocks, a hex palette or explicit placement matter. The schema is shared with 4.0. [I5]

- Top level, in this order: `high_level_description` (required), `style_description` (optional), `compositional_deconstruction` (required, with `background` and `elements`).
- `style_description` fields: `aesthetics`, `lighting`, `medium`, `color_palette`, and either `photo` (photographs) or `art_style` (everything else), not both.
- Elements are `{"type":"obj","desc":...}` or `{"type":"text","text":...,"desc":...}`, each with optional `bbox` and `color_palette`.
- `bbox` is `[y_min, x_min, y_max, x_max]` on a 0-1000 grid from the top-left, row first. Omit it to let the model place the element.
- Palettes: up to 16 full six-digit hex colours overall and 5 per element; a soft bias, not a lock. Include background, highlight and shadow colours for tonal control.
- JSON that doesn't match the schema (for example, missing `high_level_description`) is read as plain text. Paste it without Markdown fences in the app, and advise Magic Prompt off so it is used as written.

### Original layout prompt

Settings outside the prompt: portrait 2:3, Magic Prompt off.

```json
{
  "high_level_description": "A clean botanical workshop flyer with a large pressed-fern illustration and three lines of text.",
  "style_description": {
    "aesthetics": "calm, airy, handmade",
    "lighting": "flat even light with no cast shadows",
    "medium": "graphic design",
    "art_style": "risograph print, two inks, fine paper grain",
    "color_palette": ["#F4EFE4", "#2F5D50", "#C8553D"]
  },
  "compositional_deconstruction": {
    "background": "Warm off-white recycled paper with subtle fibres.",
    "elements": [
      {"type": "text", "bbox": [60, 80, 200, 920], "text": "PRESS & KEEP", "desc": "Large forest-green serif capitals, centred on one line.", "color_palette": ["#2F5D50"]},
      {"type": "obj", "bbox": [230, 200, 760, 800], "desc": "One large pressed fern frond in forest green, slightly curled at the tip, with fine vein detail."},
      {"type": "text", "bbox": [790, 120, 860, 880], "text": "A botanical pressing workshop", "desc": "Medium italic serif in forest green, centred."},
      {"type": "text", "bbox": [880, 250, 940, 750], "text": "SUNDAY 9AM · GLASSHOUSE", "desc": "Small terracotta sans-serif capitals, centred.", "color_palette": ["#C8553D"]}
    ]
  }
}
```

Before delivery, parse the JSON, check every box has `0 <= y_min < y_max <= 1000` and `0 <= x_min < x_max <= 1000`, leave room for each text block, avoid unintended overlaps and keep the most important elements first.

## Repair the actual failure

| Observed problem | Useful revision | Keep outside the prompt |
| --- | --- | --- |
| Misspelled or dropped letters | Quote the exact copy early, shorten it, give it a clear surface and space, simplify the scene. For one wrong word on a good image, use a targeted edit instead of regenerating. | Magic Prompt state; whether a Studio text layer is more appropriate. |
| Extra text or objects appear | Cut unneeded ideas, describe the main subject more fully, state "no other lettering" only once. | Turn Magic Prompt off if its expansion added them. |
| Excluded item appears | Rewrite as the positive visible state; remove words elsewhere that imply it. | No negative-prompt field on 4.5. |
| Text blocks in the wrong place | Describe blocks in reading order with positions, or move to JSON with `bbox` per block. | Aspect ratio; boxes guide rather than fix layout. |
| Colours drift | Name colours on the objects they belong to; in JSON add hex palettes globally and per element. | Palette is a soft bias. |
| Subject cropped or tiny | Name framing ("full body", "head and shoulders"), describe what is near the feet or edges, make the person or the setting the main subject. | Pick a suitable ratio, or reframe later. |
| Faces or hands distorted | Move closer with framing words and name the details that matter. | Fix a good image locally with Precise Edit and a mask. |
| Part of the prompt ignored | Move it earlier, describe it concretely, remove conflicting cues. | Prompt length; very long JSON can lose trailing elements. |
| Style or mood off | Replace vague adjectives with medium, technique and visible traits. | 3.0-only presets and style references aren't available on 4.5. |

## Working from an existing prompt

Extract what already works before changing anything. Preserve exact text and identity constraints, remove contradictions, then rewrite only the weak parts. Don't port 3.0 syntax (style preset names, style codes, negative prompts) or other models' weighting syntax into a 4.5 prompt. When asked for alternatives, hold the copy and layout fixed and vary one visual choice at a time.

Treat supplied output images as evidence of failure; without them, label a diagnosis as a hypothesis. A longer prompt is not automatically a better prompt.
