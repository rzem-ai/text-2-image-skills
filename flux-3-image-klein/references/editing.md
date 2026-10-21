# FLUX 3 Image Klein: references and localised edits

## Expanded source-aware instructions

Identify the base scene and what each extra reference contributes. For a bounded edit, describe the changed object, its new appearance and the important composition to preserve. For a new composition, describe the completed scene and assign source identity or appearance explicitly. Up to ten references are documented, but a named person or product isn't a substitute for supplying an actual image. [F1, F2]

The model expects an expanded edit brief, not an isolated command such as changing a colour. Conversely, don't overwrite an unrelated source detail by adding a new descriptive flourish. Inspect references before naming exact features; if they're absent, provide a conditional template and ask for the necessary source only when it blocks useful refinement.

### Original edit example

This example assumes a supplied photograph matching the lunchbox scene in [prompting.md](prompting.md).

```text
In the first reference photograph, change the lunchbox body from muted cobalt blue to forest-green enamel while keeping the cream lid, folded handle, two closed metal clasps and the lunchbox proportions unchanged. Retain the eye-level viewpoint, the lunchbox position in the right half of the pale timber table and the comfortable margin around the complete object. Preserve the quiet empty space on the left and the softly blurred ivory plaster wall behind it. The new green enamel should follow the existing broad highlight from the window light on the left, with the same short contact shadow beneath the box. Keep all other objects, framing and background details consistent with the source photograph.
```

## Editing with boxes

Final edit rows use `id`, `from`, `src_bbox`, `tgt_bbox` and `desc`, rather than generation's `bbox`. In the current local Klein reference code and PUP system prompts, the first reference is `ref_image_0`, the second `ref_image_1`. Cite references with tokens such as `<ref_image_0>` in the accompanying expanded instruction. [F5]

| Operation | Local Klein row convention |
| --- | --- |
| Preserve an anchor | `from: "ref_image_0"`; source and target boxes are equal. |
| Move/resize | Source reference and source box remain; provide the desired target box. |
| Remove | Retain source reference and box; set `tgt_bbox` to null. |
| Create new content | `from: "target"`, `src_bbox: null`, and a valid target box. |

All final boxes use the same integer 0-1000 y-first grid. The current hosted FLUX 3 box guide instead documents `from: null` for new content. Don't mix that hosted convention with local Klein's `"target"` convention. Preserve a supplied valid schema and check the actual surface before converting it. [F4, F5]

For example, a local row can move an existing pot without redefining its appearance:

```json
{"id":"pot_1","from":"ref_image_0","src_bbox":[500,100,900,350],"tgt_bbox":[500,600,900,850],"desc":"The same small matte terracotta pot containing an olive tree."}
```

This row is a schema illustration, not a complete image prompt. Deliver it only as part of an expanded instruction with consistent element IDs and any necessary anchors. Don't pretend to have measured these coordinates in an unseen image.

## Preservation limits

Boxes guide placement and scale, not hard masks. Even when a hosted tutorial describes unchanged surroundings, the Klein card explicitly warns that edits can affect content outside the requested region. Don't guarantee pixel-identical results from either prose or boxes. Tiny text or details missed in a reference can also drift; reassert only features that are actually visible or supplied by the user.
