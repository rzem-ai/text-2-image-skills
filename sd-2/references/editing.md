# Stable Diffusion 2: image-to-image briefs

Bracketed evidence labels resolve in [sources.md](sources.md). Strength, noise and mask values are workflow notes for the user, not part of the prompt text.

## Choose the right checkpoint

| Need | Checkpoint | Prompt-relevant consequence |
| --- | --- | --- |
| Restyle or rework a whole image | 2.1-v or 2.1-base with img2img | Describe the finished image. Strength controls how much changes. |
| Replace one region | `sd-2-inpainting` | Describe the filled region in the context of the whole scene. Requires a mask. [S5] |
| Keep layout and shape, change look | `sd-2-depth` | Describe new materials, lighting and style; geometry follows the depth estimate. [S6, S9] |
| Enlarge an image 4x | `stable-diffusion-x4-upscaler` | Describe what the image already shows. [S7] |
| Variations of a picture | `sd-2-1-unclip` | The image embedding carries most of the content; text nudges it. [S8] |

The inpainting and depth checkpoints derive from 2.0-base at 512x512, not from 2.1-v. Write for 512-scale detail and don't promise 2.1-v quality from them.

## Classic img2img

Write the positive prompt as a description of the finished image, not an instruction. The README notes classic img2img introduces significant semantic changes relative to the source. Author suggestion: strength around 0.3-0.5 keeps composition and colour; 0.6-0.8 allows restyling; near 1.0 the source barely survives. Match the source to the checkpoint's native canvas. A sentence such as "change only the coat" does not establish a mask or protect other pixels. [S9]

## Inpainting

The inpainting model takes the masked image as extra conditioning. In Diffusers, white mask pixels are repainted and black pixels are kept. [S5]

- Describe what should appear inside the mask and how it sits in the existing scene: lighting direction, surface and scale.
- Mention surrounding context briefly so the fill matches; the card's own example names both the fill and its setting. [S5]
- Use the negative prompt for the failure you want to avoid at the seam, such as "visible seam, mismatched lighting".
- Use the dedicated inpainting checkpoint for real fills. Masked img2img on a regular checkpoint blends less reliably; say so if the user has only that.

## Depth2img

The depth model estimates relative depth with MiDaS and conditions on it, so structure is preserved while appearance changes. At strength 1.0 all pixel information is removed and only the prompt and depth survive. The Diffusers default strength is 0.8. The README says it is particularly useful for photorealistic styles. [S6, S9, S11]

- Describe new materials, palette, lighting and medium. Don't describe a new layout; geometry follows the depth map.
- Keep object identity words consistent with what the depth shape implies. A depth silhouette of a chair won't become a dog.

## x4 upscaler

The upscaler is text-guided and takes a `noise_level`. The Diffusers default is 20; higher values add variation and reduce fidelity. The README recommends a higher level, such as 100, for synthesised inputs. [S7, S9, S12]

- Prompt with a short, accurate description of what the image already shows: "a white cat on a grey sofa, sharp fur detail". Don't add new objects.
- A negative prompt such as "blurry, jpeg artifacts, oversharpened" is supported. [S12]
- The model was trained on 512x512 crops; large inputs are memory-heavy. That is a workflow concern, not a prompt one. [S7]

## unCLIP variations

The unCLIP model accepts a noisy CLIP image embedding plus text. Noise level runs from 0, no noise, to 1000, full noise; more noise lets text steer further from the source. Use a short prompt naming the change in style or setting, or leave it empty for pure variations. [S8]

## Desired-result example for an inpainting fill

```text
a terracotta pot of red geraniums on the stone windowsill, soft morning light from the left matching the room, faint shadow on the sill, photograph
```

Negative prompt:

```text
visible seam, mismatched lighting, floating object, blurry, extra flowers outside the pot
```

## Preserve the important details

Choose invariants relevant to the task: identity, product silhouette, pose, camera position, layout or light direction. Don't require unchanged lighting when the user explicitly requests relighting. If a source image is absent, say what the user should attach outside the copy-ready prompt. A product name is not a product reference image.

## Diagnose drift

| Failure | Prompt-level repair | Workflow note |
| --- | --- | --- |
| Whole image changes during img2img | Restate the existing composition and subject in the prompt. | Lower strength. |
| Inpainted region ignores the prompt | Describe the fill more concretely and earlier. | Enlarge or soften the mask; check the inpainting checkpoint is loaded. |
| Fill looks pasted on | Describe matching light, shadow and surface. | Mask blur or padding. |
| Depth2img keeps the old look | Describe the new materials and palette more strongly. | Raise strength. |
| Upscale invents new detail | Make the prompt a plain description of existing content. | Lower `noise_level`. |
| Upscale stays soft | Add texture words that match the content ("sharp fur detail"). | Raise `noise_level` slightly for synthesised inputs. |

If the user requires pixel-identical surroundings, explain that prompt preservation is insufficient and that deterministic compositing may be needed later. This skill only supplies the brief. Don't perform image processing or claim a verified edit.
