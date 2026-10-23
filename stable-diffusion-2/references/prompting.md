# Stable Diffusion 2: prompting and refinement

The prompts below are original writing examples, not copied vendor examples or rendered benchmarks. See [capabilities.md](capabilities.md) for variant limits and [sources.md](sources.md) for documented facts. The repair advice is author guidance to test against the actual output.

## Model-specific choices

1. Lead with the subject and its key attributes, then setting, framing, medium, lighting and materials. Keep the essentials inside the first 75 tokens.
2. Describe style in concrete visual terms: "gouache on textured paper", "35mm film photograph, shallow depth of field". Don't rely on an artist or celebrity name to carry the look; OpenCLIP recall of names is unreliable.
3. Use comma-separated descriptive phrases or short sentences. A few targeted quality terms ("highly detailed", "sharp focus") are reasonable on 2.x; a long stack of overlapping ones wastes tokens.
4. Write a negative prompt by default and tailor it to the medium. Keep it shorter than the positive prompt and free of anything the brief needs.
5. Match the canvas to the checkpoint: 768-based for 2.1-v and 2.0-v, 512-based for the base, inpainting and depth checkpoints. State the canvas outside the prompt.
6. Use weighting syntax only when the user's frontend parses it. Otherwise express emphasis through word order and repetition of the key noun in context.
7. The model cannot render legible text. Reserve a clean area for later typesetting rather than asking for exact lettering.

## Copy-ready examples

### Photographic scene (2.1-v, 768x768 or 1024x768)

```text
photograph of a weathered fishing boat moored at a timber jetty at dawn, low mist over flat water, coiled ropes and orange buoys on the deck, distant headland, soft side light from the left, muted blue and amber palette, 35mm film photograph, shallow depth of field, sharp focus on the hull, fine film grain
```

Negative prompt:

```text
blurry, out of focus, low detail, overexposed, oversaturated, cartoon, illustration, 3d render, duplicate boat, watermark, text, signature, jpeg artifacts
```

### Illustration (2.1-v or 2.1-base)

```text
gouache illustration of an adult beekeeper inspecting a honeycomb frame beside a white hive, waist-up, rolled shirt sleeves, veiled hat pushed back, frame held in both hands, summer meadow background with soft focus, warm afternoon light, visible brush texture on textured paper, restrained ochre and sage palette
```

Negative prompt:

```text
photograph, photorealistic, 3d render, harsh outlines, muddy colors, extra hands, extra fingers, deformed hands, watermark, signature, text
```

### Portrait with people (2.1-v)

```text
head-and-shoulders portrait of an elderly man with a short white beard and deep smile lines, navy wool jumper, seated by a rain-streaked window, soft overcast window light, neutral grey background, natural skin texture, 85mm portrait photograph, eyes in sharp focus
```

Negative prompt:

```text
deformed face, asymmetrical eyes, extra limbs, disfigured, plastic skin, airbrushed, cartoon, painting, blurry, watermark, text
```

Negative prompts are written with the spelling most common in English captions where it matters ("jpeg artifacts"). Spelling variants are a small effect; keep whichever the user already uses.

## Repair the actual failure

| Observed problem | Useful revision | Keep outside the prompt |
| --- | --- | --- |
| Pure noise, garbage or brown mush | None at prompt level; this points to a config mismatch. | Check the v-prediction or epsilon config matches the checkpoint. |
| Black or blank image | None at prompt level. | fp16 attention instability on 2.1 or a safety checker; check runtime precision. |
| Duplicated subject or repeated composition | Name one subject explicitly ("a single", "one") and describe its placement. | Canvas well above native size; return to native size and upscale later. |
| Soft, smeared or unfinished detail | Add a concrete material and lighting description; add "blurry, low detail" to the negative prompt. | Canvas below native size, step count or guidance. |
| Flat, washed-out look | Name the light source, contrast and palette. Strengthen the negative prompt with "flat lighting, washed out". | Guidance scale and scheduler. |
| Style ignored after an artist name | Replace the name with medium, technique, era and palette description. | Whether a 2.x fine-tune or embedding is expected. |
| Missing object or wrong count | State the exact count and anchor each object in the scene. Move it earlier in the prompt. | Whether the frontend truncated past 75 tokens. |
| Attributes swap between subjects | Use distinct nouns, positions and ownership. Simplify to two subjects or fewer. | Compositional limits documented for the model. |
| Malformed faces or hands | Frame closer, reduce the number of people, add focused anatomy terms to the negative prompt. | A later inpainting pass at 512 for the face or hand region. |
| Wrong or garbled text | Remove the lettering request and reserve a blank sign or panel. | Typesetting in a separate tool. |
| Unwanted restyling | Reassert the intended medium and put the competing medium in the negative prompt. | Whether a LoRA or embedding is dominating. |
| Cropped subject | Request the complete silhouette, named extremities and comfortable margins. | Canvas ratio. |

## Negative prompt discipline

Start from the medium-specific baselines above, then add only what an observed failure justifies. Never put something the brief needs into the negative prompt: drop "text" when a sign must carry lettering, drop "illustration" when the brief is an illustration and drop "border" when a frame is requested. Don't add exclusions for subject matter the user hasn't raised.

## Working from an existing prompt

Extract what is already correct before changing anything. Preserve exact text and identity constraints, remove contradictions, then rewrite only the weak parts. A prompt ported from SD 1.5 usually needs artist names and long quality stacks replaced by concrete description, plus a negative prompt if it had none. When asked for alternatives, vary framing, illumination or medium one at a time so the user can compare meaningful choices.

Treat supplied output images as evidence of failure; if no result is available, label a diagnosis as a hypothesis. A longer prompt is not automatically a better prompt.
