# FLUX 3 Image: captions, text and layouts

The prompts below are original, unrendered examples. See [capabilities.md](capabilities.md) for settings and [sources.md](sources.md) for documented facts. Repair advice is author guidance to test against actual output.

## Write the scene

Describe subject, setting, light and framing in concrete prose. Name the light's source, quality, direction and colour temperature. For a style, name it and describe its visible traits; a camera, lens or film stock is useful only with the effect it should produce. Optional closing tags such as `Style: ...` and `Mood: ...` can hold a consistent treatment. [F3, F7]

Put a replacement description early in the sentence that sets the scene, rather than in a trailing clause. Make the content fit the frame: an ultra-wide ratio needs a scene that spans the width. [F7]

The service expands prompts automatically, so a short idea is acceptable. Write a fuller caption when exact composition, counts or relationships matter, then keep it free of contradictory alternatives.

### Original generation prompt

Settings note outside the prompt: `aspect_ratio` 3:2.

```text
A documentary-style colour photograph of a fishmonger's stall at dawn, seen at eye level from across a wet concrete market aisle. Crushed ice fills a stainless steel counter, holding three neat rows of silver whiting and one large snapper laid diagonally at the front. Behind the counter, a woman in a navy rubber apron and rolled sleeves lifts a crate of lemons onto a shelf. Cool blue daylight enters from an open roller door on the left, while a single warm tungsten bulb hangs above the stall, giving the ice a faint amber glint. Puddles on the floor reflect the bulb. Shot on 35mm colour negative film with fine grain and slightly lifted shadows. Style: candid market documentary. Mood: quiet, early, industrious.
```

## Exact lettering and colour

Quote every displayed string exactly, with its case and punctuation. Say where it appears, then describe weight, case, colour and type character. Use `\n` inside a quoted string for line breaks. Give a poster's separate text blocks separate boxes when placement matters, and proofread every rendered string before use. [F3, F7]

A hex code works best attached to one named object or text block, not as a loose palette list. [F7]

### Original text-heavy prompt

Settings note outside the prompt: `aspect_ratio` 4:5, `grounding` false because the venue is fictional.

```text
A portrait gig flyer printed on uncoated off-white card, photographed flat from directly above under soft even light. At the top, the exact words "THE LOW TIDES" in tall condensed black sans-serif capitals span almost the full width. Beneath it, a wide band of solid coral #FF6F59 holds a simple white line drawing of a breaking wave. Below the band, centred in smaller black capitals, the exact text "SATURDAY 14 NOVEMBER\nDOORS 8PM" on two lines. At the bottom, the exact words "Harbour Room, Wollongong" in a light black serif italic. Generous margins on all sides, no other lettering, faint paper fibre visible.
```

## Layout prompts

Choose `aspect_ratio` before placing boxes. Write a caption that describes the scene and cites each element as `<id>` next to its subject, then append one JSON array. Each generation row has a unique `id`, a `bbox` and an appearance `desc`. Also describe positions in words. [F5, F6]

Boxes are integers `[top, left, bottom, right]` on a 0-1000 grid from the top-left, y before x. The grid stretches per axis: on a 16:9 canvas, a visually square object needs about 56 horizontal units for every 100 vertical units. Overlap boxes where objects overlap. A box of roughly 40 x 25 pixels for a new element often fails to appear. [F5, F6]

### Original layout prompt

Settings note outside the prompt: `aspect_ratio` 16:9.

```text
A wide illustrated travel banner in flat gouache shapes. A pale sandstone sky fills the frame <sky_1>. On the right, a single red-roofed timber lighthouse <lighthouse_1> stands on a dark green headland <headland_1> that slopes down towards the lower right corner. On the left, the title <title_1> sits in the upper half above a short subtitle <subtitle_1>, leaving calm space around both. A small white sailing boat <boat_1> crosses the teal water in the lower left. [{"id":"sky_1","bbox":[0,0,1000,1000],"desc":"A flat pale sandstone sky fading slightly lighter towards the horizon, with soft gouache texture."},{"id":"headland_1","bbox":[600,560,1000,1000],"desc":"A dark green grassy headland with a gentle slope, painted in two flat tones."},{"id":"lighthouse_1","bbox":[220,700,700,820],"desc":"A slender white timber lighthouse with a red conical roof and one small lit window, standing on the headland."},{"id":"title_1","bbox":[160,60,360,520],"desc":"The exact text \"CAPE QUIET\" in large rounded navy capitals, left aligned on one line."},{"id":"subtitle_1","bbox":[390,60,460,460],"desc":"The exact text \"Walks, weather and one lighthouse\" in small navy sentence-case sans-serif, left aligned."},{"id":"boat_1","bbox":[700,180,860,300],"desc":"A small white sailing boat with a single triangular sail, heading right across teal water."}]
```

Before delivery, parse the array as JSON, check that IDs are unique and match caption tokens, and require `0 <= top < bottom <= 1000` and `0 <= left < right <= 1000`. Keep boxes large enough for their content.

## Repair the actual failure

| Observed problem | Useful revision | Keep outside the prompt |
| --- | --- | --- |
| Expansion added unrequested content | Compare `result.prompt` with the intent; state the wanted scene more fully and positively. | That no expansion switch exists. |
| Unwanted object persists | Describe what occupies that space instead of negating it. | None. |
| Real place or product rendered wrongly | Describe its visible features directly, or supply a reference. | Whether `grounding` is on. |
| Garbled or rewritten text | Quote the exact copy, reduce competing text, give it its own box. | Resolution tier for small print. |
| Element ignored or misplaced in a layout | Check the `<id>` token, y-first order, bounds and minimum size. | Ratio the boxes were designed for. |
| Composition changed after a resolution change | Expect a new generation; settle composition at a draft tier with explicit placement. | Resolution tier. |
| Square output when wide was wanted | No prompt fix; set the ratio. | `aspect_ratio`. |

Without supplied renders, label a diagnosis as a hypothesis. A longer prompt is not automatically better.
