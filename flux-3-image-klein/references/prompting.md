# FLUX 3 Image Klein: expanded captions and layouts

The following examples are original, unrendered prompts. See [sources.md](sources.md) for the documented conditioning and layout formats.

## Write a complete visual plan

Start with medium and framing, establish the setting and light, then describe each important subject with its appearance, position and action. Connect material and colour cues to their objects. Preserve exact counts and relationships; adding more secondary objects isn't a substitute for resolving them.

An expanded prompt can remain concise for a minimalist scene, but it must decide the composition. Avoid vague alternatives and strings of quality judgements. Camera terms are optional visual cues, not a guarantee of physical simulation. Keep all requested lettering verbatim, in quotes, with a surface and readable hierarchy.

### Original expanded photograph

```text
A quiet editorial product photograph, framed as an eye-level medium close-up of a small enamel lunchbox on a pale timber kitchen table. The lunchbox sits in the right half of the image, with its long edge almost parallel to the bottom of the frame and its handle folded neatly against the lid. Its body is muted cobalt blue, the lid is warm cream and the two metal clasps are closed. Soft overcast daylight enters from a window to the left, creating a broad gentle highlight on the enamel and a short contact shadow beneath the box. Behind it, an ivory plaster wall has a subtle uneven texture and falls softly out of focus. The left half of the table and wall remain visually quiet, with no extra objects or lettering. The complete lunchbox is visible with comfortable space around its edges.
```

## Generation layout

For a layout, place a coherent caption first, followed by one JSON array. Each element uses a unique `id`, a `bbox` and an appearance `desc`. Cite each table ID as `<id>` next to the corresponding subject in the caption. Put displayed wording in a text element's description. [F3, F4]

The final boxes are integers `[top, left, bottom, right]`, each from 0 to 1000, measured from the top-left corner. Y comes before X. A 0-1000 grid stretches independently along the two canvas axes, so a visually square object on a portrait canvas doesn't necessarily have equal grid width and height. These coordinates aren't MOSS's centred pixels or the reference CLI's separate 0-1 input-box convenience format.

### Original layout prompt

Canvas outside the prompt: **portrait 2:3**. The caption and array below belong together in the same positive prompt.

```text
A portrait screen-printed garden poster on warm ivory paper <background_1>. The forest-green title "GROW SLOWLY" <title_1> is centred across the upper portion, with broad side margins and clear space beneath it. A single terracotta pot holding a young olive tree <tree_1> occupies the lower centre. The tree has a slim trunk and a small irregular crown of grey-green leaves. Flat ink colours and restrained paper grain give the design a calm handmade appearance. [{"id":"background_1","bbox":[0,0,1000,1000],"desc":"A warm ivory paper background with subtle grain."},{"id":"title_1","bbox":[80,100,220,900],"desc":"The exact text \"GROW SLOWLY\" in large forest-green serif capitals, centred on one line."},{"id":"tree_1","bbox":[330,260,900,740],"desc":"One young olive tree with grey-green leaves, a slim trunk and a matte terracotta pot, rendered in simple screen-printed shapes."}]
```

Before delivery, parse the array as JSON, check unique IDs and their caption references, and require `0 <= top < bottom <= 1000` and `0 <= left < right <= 1000`. Keep boxes large enough to carry the requested content. Don't invent separate box parameters when the user only needs the final model prompt.

## Repair specific failures

| Observed issue | Useful revision |
| --- | --- |
| Generic scene | Replace an unexpanded idea with a concrete visual plan. |
| Wrong framing | State scale, viewpoint, subject position and margins explicitly. |
| Layout ignores an element | Check ID matching, box order, bounds and whether the element is too small. |
| Garbled lettering | Preserve exact wording, reduce competing text and give the text adequate space. |
| A style name changes content | Describe the desired palette, marks, texture and shading directly. |
| Extra content appears after rewriting | Compare the approved expanded prompt with the surface's actual rewritten prompt if available. |

Hold seed and settings constant when the user supplies comparable renders. Without renders, describe a rewrite as a recommendation rather than a measured gain.
