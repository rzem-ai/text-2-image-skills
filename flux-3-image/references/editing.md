# FLUX 3 Image: references and edits

## Instruction edits

Editing uses the same endpoint as generation, with references in `images`. Write a natural-language change that names the target precisely enough that only one element matches, for example "only the middle bird". For several images, state how they relate. [F4]

Refer to references by position and use the same wording every time: "image 1" is the first entry in `images`. Give each image a role (subject, product, setting or style) and name the features it supplies, since one image can contribute several. Put the base image first: with `aspect_ratio` on `auto`, the output follows image 1's shape. [F8]

Phrase removal as an instruction ("Remove the mug from the desk"), not a negation. The service expands edit instructions and often adds its own box for the named element, so a concise, unambiguous instruction is appropriate. [F4, F7]

### Original instruction edit

This assumes image 1 is a supplied photograph of a café counter and image 2 a supplied product shot of a ceramic cup.

```text
Image 1 is the base café counter photograph and image 2 is the product reference. Replace the white paper cup beside the till in image 1 with the speckled sage-green ceramic cup from image 2, keeping its handle, glaze speckle and proportions. Match the cup's reflections and short contact shadow to the existing window light from the right. Keep the till, menu board, barista and the rest of the counter unchanged.
```

## Editing with boxes

Edit rows replace generation's `bbox` with `from`, `src_bbox` and `tgt_bbox`, plus `id` and `desc`. The first image is `ref_image_0`, the second `ref_image_1`; cite them as `<ref_image_0>` in the instruction and cite elements as `<id>`. All boxes use the same 0-1000 y-first grid. [F5]

| Operation | Hosted FLUX 3 Image row |
| --- | --- |
| Keep (anchor) | `from` set to a reference; `src_bbox` equals `tgt_bbox`. |
| Move or resize | `from` set; `tgt_bbox` differs from `src_bbox`. |
| Add new content | `from: null`, `src_bbox: null`, `tgt_bbox` set. |
| Remove | `from` set; `tgt_bbox: null`. |

New content uses `from: null`. Local FLUX 3 Image Klein instead uses `from: "target"`; don't mix the conventions. State additions and removals in the instruction as well as the rows. [F4, F5]

### Original box edit

Assumes `<ref_image_0>` is a supplied 3:2 photograph of a reading nook; coordinates are placeholders to measure against the actual image.

```text
In <ref_image_0>, keep the grey linen armchair <chair_1> exactly where it is. Move the brass floor lamp <lamp_1> from the left of the chair to its right side, at the same scale. Remove the coffee mug <mug_1> from the side table. Add a tall potted fiddle-leaf fig <fig_1> in a matte white pot to the left of the chair, lit by the same afternoon window light. Keep the rest of the room unchanged. [{"id":"chair_1","from":"ref_image_0","src_bbox":[380,330,900,660],"tgt_bbox":[380,330,900,660],"desc":"The same grey linen armchair with rounded arms and timber legs."},{"id":"lamp_1","from":"ref_image_0","src_bbox":[120,180,880,300],"tgt_bbox":[120,690,880,810],"desc":"The same brass floor lamp with a cream drum shade."},{"id":"mug_1","from":"ref_image_0","src_bbox":[560,820,660,880],"tgt_bbox":null,"desc":"A white coffee mug on the side table, to be removed."},{"id":"fig_1","from":null,"src_bbox":null,"tgt_bbox":[160,90,900,300],"desc":"A tall fiddle-leaf fig with broad glossy leaves in a matte white pot."}]
```

Don't present illustrative coordinates as measured. If the user supplies valid boxes, preserve them.

## Preservation limits

The documentation says pixels outside boxes usually stay the same, but shadows, reflections and nearby light can change; placement is a strong hint, not a hard constraint. Don't promise pixel-identical results. If exact surroundings are required, say deterministic compositing may be needed later. [F4, F8]

| Failure | Prompt-level repair |
| --- | --- |
| Wrong element changed | Name the target uniquely by position or feature; add a box for it. |
| Background drifts | Add anchor rows for key objects and reassert the unchanged scene. |
| Identity or product shape changes | Assign the reference role explicitly and list its visible distinctive features. |
| Style bleeds into content | Separate the image supplying style from the one supplying content. |
| Output has the wrong shape | Reorder images or set `aspect_ratio` outside the prompt. |
| New element missing | Enlarge its target box and mention the addition in the instruction. |
