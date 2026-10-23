# Stable Diffusion 3.5: image-to-image briefs

SD3.5 isn't a native instruction editor. Every edit route below is a diffusion workflow guided by a description of the finished image, plus a source image, mask or control map. Write the prompt as the target picture, not as a command such as "change the coat". See [capabilities.md](capabilities.md) for variant scope and [sources.md](sources.md) for evidence.

## Choose the route

| Route | What the prompt does | Workflow notes outside the prompt |
| --- | --- | --- |
| Img2img | Describes the whole finished image. | Strength: 0 keeps the input, 1 ignores it. Diffusers defaults to 0.6; the hosted `image-to-image` mode requires an explicit value. [S4, S6] |
| Inpainting | Describes the whole image, with most detail on the masked region. | Diffusers mask: white is repainted, black is kept; strength default 0.6. Optional crop padding around the mask. [S4] |
| ControlNet (Large only) | Describes content, style and light while the map fixes structure. | Canny, Depth and Blur for 3.5 Large. Upstream suggests control strength around 0.8, 0.7 and 0.9 respectively, Euler, 50-60 steps; examples use `max_sequence_length` 77. [S9] |
| Hosted edit and control | Each service has its own fields. | Inpaint, Erase, Outpaint, Search and Replace, Search and Recolor, Sketch, Structure and Style. The docs don't say these run on SD3.5, so don't present them as SD3.5 features. [S7] |
| IP-Adapter | Text plus a reference image for look and concept. | Third-party adapter for 3.5 Large in Diffusers; scale around 0.5-0.6. Not an identity guarantee. [S4] |

The ControlNet cards also say preprocessing (edge detection, depth estimation, blur) happens outside SD3.5, so a control map has to be prepared before generation. The Blur card credits the Tile ControlNet as its inspiration, which points to detail re-rendering and tiled upscaling; that is a workflow choice, not something to describe in the prompt. [S9]

## Preserve the important details

Choose invariants relevant to the task: identity, product silhouette, label text, pose, camera position, layout or light direction. In img2img and inpainting, the prompt should still describe the kept parts, because a prompt that only mentions the change pulls the whole image towards that one item. Don't require unchanged lighting when the user explicitly asks for relighting. When moving an object into a new setting, preserve its intrinsic features while letting shadows, reflections and perspective fit the destination.

If a source image is absent, say what the user should attach outside the copy-ready prompt. A product name is not a product reference image.

## Desired-result inpainting example

Mask covers only the jacket in an existing street portrait:

```text
Street portrait of a young man standing at a tram stop on a rainy evening, wearing a mustard-yellow waxed cotton jacket with a corduroy collar and brass snaps, hands in pockets. Wet pavement reflects shop lights, soft neon glow from the left, shallow depth of field, natural skin texture, 35mm documentary photograph.
```

## Depth ControlNet example

Depth map taken from a photo of an empty living room:

```text
Mid-century living room in warm late-afternoon light. A low walnut sideboard runs along the back wall under a wide window, a mustard wool armchair sits in the left foreground beside a brass floor lamp, and a round jute rug covers the timber floor. Long soft shadows across the floor, plants on the windowsill, calm editorial interior photograph.
```

## Diagnose drift

| Failure | Prompt-level repair | Workflow note |
| --- | --- | --- |
| Too little change in img2img | Describe the new state more concretely and drop wording that restates the old state. | Raise strength. |
| Composition or identity lost | Reassert the subject, pose and layout that must remain. | Lower strength, or move to a mask or ControlNet. |
| Inpainted area doesn't blend | Describe light direction, colour temperature and texture matching the surroundings. | Feather or expand the mask; use crop padding. |
| ControlNet output ignores prompt style | State the medium and palette first; avoid content that contradicts the map. | Lower the control strength. |
| Structure ignores the map | Remove prompt details that conflict with the map's shapes. | Raise the control strength; check the map polarity and preprocessing. |
| Labels are rewritten | Quote exact existing copy separately from any replacement copy; keep labels outside the mask if they must survive. | Composite the original label afterwards if it must be exact. |

If the user requires pixel-identical surroundings, explain that prompt preservation isn't enough and that masking plus deterministic compositing may be needed in a later workflow. This skill only supplies the brief. Don't perform image processing or claim a verified edit.
