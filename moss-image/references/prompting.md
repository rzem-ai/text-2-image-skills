# MOSS Image: captions, typography and layouts

The examples are original, unrendered prompt-writing recommendations. Documented formats come from the sources in [sources.md](sources.md).

## Caption mode

Build a coherent scene from subject and action, setting, framing, light, medium, materials and selected details. Use spatial language to resolve ownership and relationships. Preserve a minimalist brief instead of expanding it into a crowded illustration. Tags are supported, but a caption doesn't need a quality stack or an invented score vocabulary.

### Original caption example

```text
A documentary-style photograph of a small roadside plant stall after rain. Three terracotta pots stand on a weathered timber table in the foreground, each holding a different fern. A handwritten cream card leaning against the middle pot reads "FERNS FOR SHADE" on the first line and "Grown locally" on the second. The lettering is dark green, large enough to read and clear of the leaves. Soft cloudy daylight reveals wet leaf edges and the rough clay surfaces. A pale green fence recedes behind the table, with the background gently out of focus. Keep the three pots fully inside the frame and leave a little clear space above the tallest fern.
```

For lettering, keep the actual words distinct from instructions about their placement. Quote exact copy, give a physical surface and describe hierarchy. Literal newlines in prose or escaped `\n` inside JSON strings can express a requested line break. Don't replace the supplied language with a translation unless asked.

## Native layout format

Use a top-level object with `summary`, a flat `items` array, `bbox_coord_space: "abs_centralized"` and `bbox_format: "yxyx"`. `summary.caption` describes the complete composition. Each item has `label`, `caption` and `bbox`; text items also carry the exact string in `text`. [M3]

These are absolute pixel coordinates centred on the chosen canvas, not a normalised 0-1000 grid. For width W and height H, convert a top-left-origin box `[left, top, right, bottom]` to:

```text
[top - H/2, left - W/2, bottom - H/2, right - W/2]
```

Calculate the conversion before composing the final prompt. Require positive-area boxes, y coordinates within `[-H/2, H/2]`, x coordinates within `[-W/2, W/2]`, and dimensions divisible by 16. Don't silently clip a bad box or switch x and y. Overlap is valid for deliberate occlusion. A placement box doesn't ask the model to draw a border.

The formula block is a coordinate reference, not text to insert into an image prompt. Upstream's optional enhancer uses a separate top-left-pixel draft and compiler; that draft format is not the final model layout. This standalone skill supplies the final format directly and doesn't depend on that external compiler.

### Original ready-to-paste layout

Canvas outside the prompt: **1024 x 1536**. This example's top-left pixel regions are title `[96,128,928,288]`, illustration `[256,400,768,1184]` and footer `[128,1248,896,1376]`.

```json
{"summary":{"meta":["poster"],"canvas":"single","caption":"A portrait botanical poster on warm ivory paper. A large forest-green heading sits above a central painted glasshouse containing ferns. A small centred footer completes a quiet composition with broad margins."},"items":[{"label":"text","caption":"Large forest-green serif capitals, centred with generous spacing.","text":"GARDEN NOTES","bbox":[-640,-416,-480,416]},{"label":"object","caption":"A delicate painted glasshouse with a dark green frame, translucent panes and three lush ferns visible inside.","bbox":[-368,-256,416,256]},{"label":"text","caption":"Small dark-green lettering, centred on one line.","text":"Observe. Sketch. Grow.","bbox":[480,-384,608,384]}],"bbox_coord_space":"abs_centralized","bbox_format":"yxyx"}
```

Keep the same generation dimensions when reusing these centred coordinates. For a different canvas, recalculate boxes. Dimensions are a handoff note, not additional fields invented inside the final layout JSON.

## Refinement

| Observed failure | Revision to try |
| --- | --- |
| Wrong text or line breaks | Preserve the exact string and separate independently positioned text blocks. |
| Wrong placement | Check canvas, centred coordinates and yxyx order before adding adjectives. |
| Subject merges with text | Separate their regions and describe their intended relationship. |
| Unwanted visual clutter | Remove invented secondary items while retaining the supplied copy. |
| Visible watermark-like marks | A focused negative prompt may help; it isn't a guarantee. |

An optional negative candidate for an observed artefact is:

```text
watermark, jpeg artifact
```

Don't apply an exclusion that conflicts with the brief. Keep CFG, steps, shift, SLG and LoRA configuration outside the positive and negative text.
