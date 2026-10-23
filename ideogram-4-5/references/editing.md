# Ideogram 4.5: image-to-image briefs

Evidence labels resolve in [sources.md](sources.md). Surface limits are context for the brief, not instructions to run an edit.

## Choose the edit mode

| Need | Mode | Prompt-writing consequence |
| --- | --- | --- |
| A described change across an image, or combining images | 4.5 generate with references (app: Ideogram 4.5 with reference images; API: `images`) | Up to 5 images; the first is edited, others are references. The prompt becomes an edit instruction and Magic Prompt is hidden. [I6, I8] |
| A bounded change with the rest kept | Precise Edit (app **Edit** button; API `precise-edit`) | One source plus up to 4 references, or 3 with a mask. Output keeps the source's width and height; unchanged pixels are copied from the source. [I7, I9] |
| One region only | Precise Edit with a mask, optionally an edit window | API mask polarity: black is the area to edit, white is kept, same size as the source, containing both. The instruction must still describe the replacement. [I7, I9] |
| A new take keeping rough layout | Remix (app and API run 4.0 or 3.0, not 4.5) | Describe the complete result; image strength is a separate control. Out of 4.5 scope; say so if the user expects 4.5. [I14] |
| New backdrop from a photo of a setting | Replace background (4.5 tool) | Takes the image and a background reference, no prompt; people in the reference aren't copied. No prompt to write. [I17] |
| Wider canvas or new ratio | Studio Extend/Reframe, or 3.0 Reframe in the API | A 3.0 or Studio workflow, not a 4.5 prompt. [I10, I13] |
| Larger file | Upscale app (Topaz, Nano Banana Pro or Auto) | A separate upscaler; no 4.5 prompt is involved. [I18] |
| Wrong word in good lettering | Precise Edit with a mask on the word, or a Studio text layer | Quote the old and new wording separately. [I4] |

## Write the edit instruction

Name the exact component and its current state, say what it becomes, then say what stays. Useful preservation phrasing names shape, size, proportions, position, camera and framing, plus fragile details such as logos, labels and small text; a general "keep the product" is weaker. When replacing an item, say what leaves and what arrives and anchor it to its container or surface. [I15]

- Keep the instruction short. Don't re-describe the whole image when references are attached; the prompt is an edit, not a scene caption. [I6]
- Assign each reference a role: which supplies the subject, which the material or setting, which the light. In the app, use the actual `@` pills rather than guessed file names; in the API, name references by order. [I6]
- Crop references to the relevant detail and check that their lighting or background doesn't leak into the subject. [I15]
- Don't require unchanged lighting when the user explicitly asks to relight. When moving an object to a new setting, preserve its intrinsic features while letting shadows, reflections and perspective fit the destination.
- If a source image is absent, say what to attach outside the copy-ready prompt. A product name is not a product reference image.

## Targeted edit examples

### Unmasked colour change

```text
Change only the ceramic mug from glossy white to matte sage green. Keep its exact shape, size, handle, position and the small "Saturday" lettering on its side unchanged. The camera, framing, table, steam and everything not mentioned stay exactly the same.
```

### Masked replacement

Mask outside the prompt: the painted area covers the fruit bowl's contents only.

```text
Replace the apples with a loose pile of fresh lemons, some with leaves, filling the same blue bowl. Keep the bowl, the tablecloth folds and the window light from the right unchanged.
```

### Text correction

Mask outside the prompt: the sign's lower line only.

```text
Change the lower line of the shop sign from "OPEN DIALY" to "OPEN DAILY", matching the existing gold serif capitals, size, spacing and weathering. Keep the upper line "THE CORNER LARDER" and the rest of the shopfront unchanged.
```

## Multi-turn editing

Change one thing per turn and use the accepted result as the next source. Restate attributes approved in earlier turns when they are at risk. Branch alternatives from a shared approved version rather than stacking edits on the latest variant, and save a branch before a viewpoint or material change. If a turn drifts, make the next instruction smaller and return to the last good version. [I7, I15]

## Diagnose drift

| Failure | Prompt-level repair |
| --- | --- |
| Whole product changes colour | Name the component and current state; mask it if wording isn't enough. |
| Product shape changes | State the immutable silhouette and distinctive parts; remove conflicting shape language. |
| Background or scene shifts | Reduce the edit to one target, state the unchanged camera and framing, or add a mask or edit window. |
| Product appears to float | Name the supporting surface and the contact shadow; check light direction. |
| Reference light or background leaks in | Crop the reference and say which component takes only its material or detail. |
| Labels or small text rewritten | Quote the exact existing copy to preserve and any replacement separately; inspect at full size. |
| Identity changes | Use one to five clear references of the same character; refer to them by role and keep the scene instruction short. |

Precise Edit copies pixels it didn't meaningfully change, but an instruction to preserve text doesn't prove it survived, and "pure white background" in a prompt doesn't certify exported pixels. Use Background Remover for a true transparent cutout. If the user needs pixel-identical surroundings beyond what the surface provides, say that deterministic compositing may be needed later. This skill only supplies the brief; don't perform image processing or claim a verified edit. [I9, I15]
