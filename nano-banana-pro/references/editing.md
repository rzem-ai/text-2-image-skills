# Nano Banana Pro: image-to-image briefs

## Native edit instructions

Identify the base image, the target change and the important invariants. Use explicit reference order when combining inputs. Say which image supplies identity, geometry, style or setting and which source wins if they conflict. Avoid re-describing the whole image when a short targeted instruction will preserve the user's intent more clearly.

A mask, scribble or annotation is a distinct input. State its intended role and whether the annotation should disappear from the result; don't assume a dedicated mask API or a universal mask polarity. If the selected interface doesn't expose that control, provide a text-localised edit brief without claiming stronger guarantees.


## Preserve the important details

Choose invariants relevant to the task: identity, product silhouette, label text, pose, camera position, layout or light direction. Don't require unchanged lighting when the user explicitly requests relighting. When moving an object to a new setting, preserve its intrinsic features while allowing shadows, reflections and perspective to fit the destination.

If a source image is absent, say what the user should attach outside the copy-ready prompt. Number only the actual or explicitly requested attachment slots. A product name is not a product reference image.

## Targeted edit example

```text
Use image 1 as the source poster. Replace only the title "BALANCE" with "EQUILIBRIUM", keeping it on one line if space permits without crowding the sculpture. Preserve the brass mobile, its shadow, background, subtitle and overall left-aligned typography. Match the original title colour and visual weight.
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
