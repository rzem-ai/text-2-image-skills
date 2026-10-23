# NoobAI-XL: image-to-image briefs

## Source-image regeneration

Write the positive prompt as tags describing the finished image, using the same prefix, tag order and negative as text-to-image. NoobAI-XL is a base checkpoint, not an instruction editor: "change only the jacket" in a prompt doesn't create a mask or protect other pixels. Denoising strength, masks and conditioning belong in workflow notes outside the prompt. Keep the checkpoint's prediction type consistent through the whole img2img or inpaint workflow; a V-Pred checkpoint still needs its v-prediction scheduler settings. [N2]

For inpainting, write tags for the masked region in context (subject count, the edited item, surrounding lighting) rather than the whole original scene. Repeat colour and lighting tags that must match the unmasked area.

## Official ControlNets and adapters

Laxhar Lab publishes NoobAI-XL ControlNets through Euge's Civitai collection and Hugging Face repos: canny, depth (midas and midas v1.1), normal, lineart anime, lineart realistic, manga line, softedge HED, scribble HED and PiDiNet, tile and blur, plus a separate OpenPose model. [N4, N5, N6] Version names follow `<prediction_type>-<preprocessor>`. The creator says the preprocessor must match the ControlNet and the prediction type may need to match the base checkpoint. At this check every listed version was `eps`, so ControlNet use with V-Pred 1.0 is unverified compatibility, not a documented pairing. [N4]

Prompt consequences:

- The control image fixes structure, so drop pose and composition tags that contradict it and keep tags for identity, outfit, colour, lighting and style.
- With lineart or manga-line control, describe colouring and shading (`flat color`, `cel shading`, `soft shading`); the lines already exist.
- With tile control for upscaling, keep the original prompt largely unchanged so detail isn't reinterpreted.

Laxhar also mentioned an IP-Adapter ("IPA") for NoobAI in release notes; only community mirrors of it were located, so don't assume an official reference-image slot. [N3]

## Preserve the important details

Choose invariants relevant to the task: character identity tags, outfit pieces, pose, camera angle, palette or lighting. Don't require unchanged lighting when the user asks for relighting. If a source image is absent, say what the user should attach outside the copy-ready prompt. A character tag is not a reference image.

## Desired-result example for an established inpaint workflow

Masked region: the jacket only.

```text
masterpiece, best quality, newest, absurdres, highres, safe, 1girl, solo, adult, red leather jacket, open jacket, white shirt, same pose, indoor lighting, soft shadows
```

```text
nsfw, worst quality, old, early, low quality, lowres, signature, username, logo, bad hands, mutated hands, mammal, anthro, furry, ambiguous form, feral, semi-anthro
```

## Diagnose drift

| Failure | Prompt-level repair |
| --- | --- |
| Face or character changes | Keep the exact character tags and visible traits; lower strength or narrow the mask in workflow notes. |
| ControlNet pose ignored | Remove conflicting pose tags; check preprocessor and model type match. |
| Colour shift between masked and unmasked areas | Repeat lighting and palette tags from the original; avoid new colour cues. |
| Lines doubled over lineart control | Remove `lineart`, `sketch` and heavy outline tags from the positive. |
| Grey or noisy inpaint on V-Pred | Configuration, not wording: check v-prediction scheduler and CFG rescale. |

If the user requires pixel-identical surroundings, explain that prompt preservation is insufficient and deterministic compositing may be needed. This skill only supplies the brief. Don't perform image processing or claim a verified edit.
