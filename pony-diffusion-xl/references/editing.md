# Pony Diffusion XL: image-to-image briefs

## Source-image regeneration

Write the positive prompt as a description of the finished image. A diffusion image-to-image workflow typically uses the source image plus a denoising/strength setting; low transformation preserves more structure, while stronger transformation permits larger changes. Available controls and semantics depend on the frontend. A sentence such as "change only the coat" does not by itself establish a mask or protect all other pixels.

When the user wants a local edit, separate the desired-result prompt from the workflow requirement for a mask or structural conditioning. Don't claim a base checkpoint is a native instruction editor.


## Preserve the important details

Choose invariants relevant to the task: identity, product silhouette, label text, pose, camera position, layout or light direction. Don't require unchanged lighting when the user explicitly requests relighting. When moving an object to a new setting, preserve its intrinsic features while allowing shadows, reflections and perspective to fit the destination.

If a source image is absent, say what the user should attach outside the copy-ready prompt. Number only the actual or explicitly requested attachment slots. A product name is not a product reference image.

## Desired-result example for an established compatible workflow

```text
score_9, score_8_up, score_7_up, score_6_up, score_5_up, score_4_up, source_cartoon, rating_safe, the same adult anthropomorphic badger librarian in a burgundy waistcoat, standing beside a trolley of books, holding one closed red book against the chest, full body, original pose and framing, warm reading room, clean linework, soft cel shading
```

## Diagnose drift

| Failure | Prompt-level repair |
| --- | --- |
| Product shape changes | State the immutable silhouette and distinctive components; remove conflicting shape language. |
| Identity changes | Reassert supplied identity reference and distinctive visible features; don't invent them from a name. |
| Background changes during a local edit | Name the base image and unchanged composition; reduce the edit to one target. |
| Style contaminates identity | Separate which image controls appearance from which controls visual treatment. |
| Labels are rewritten | Quote exact existing copy to preserve and exact replacement copy separately. |

If the user requires pixel-identical surroundings, explain that prompt preservation is insufficient and that deterministic compositing may be needed in a later workflow. This skill only supplies the brief. Don't perform image processing or claim a verified edit.
