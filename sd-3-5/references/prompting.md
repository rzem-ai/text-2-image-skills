# Stable Diffusion 3.5: prompting and refinement

The prompts below are original writing examples, not copied vendor examples or rendered benchmarks. See [capabilities.md](capabilities.md) for variant limits and [sources.md](sources.md) for documented facts. The repair advice is author guidance to test against the actual output.

## Stability's own structure, summarised

Stability's SD3.5 guide treats the model as a partner that reads ordinary descriptive language. It suggests building a prompt from these parts: [S8]

1. **Style**: the medium or aesthetic, such as watercolour, line art, oil painting, product photography or a blend.
2. **Subject and action**: establish the subject first, then what it is doing.
3. **Composition and framing**: close-up, wide view and so on.
4. **Lighting and colour**: named light behaviour such as backlight, hard rim light or dynamic shadows.
5. **Technical terms**: camera and cinematic vocabulary such as bird's-eye view, crane shot, wide-angle or fish-eye lens.
6. **Text**: put the words in double quotes and keep them short.
7. **Negative prompt**: use it to filter unwanted elements, textures or colours.

Stability's launch notes also say vague prompts give less predictable results and that seeds vary on purpose. Be specific where it matters and expect diversity elsewhere. [S5]

## Model-specific choices

1. Write full sentences rather than tag strings. Keep the first one or two sentences self-sufficient, because CLIP drops everything after 77 tokens.
2. Bind every attribute to its noun: "a red kite above a grey pier", not "red, grey, kite, pier".
3. Quote exact lettering, name the surface it sits on and keep each string short. Split a headline and a subline into two quoted strings with their positions.
4. For Large or Medium, add a negative prompt only for an observed or very likely problem. For Turbo, move every requirement into the positive prompt.
5. Long T5 detail is fine for Large; for Medium keep it under roughly 256 T5 tokens to avoid edge artefacts.
6. For img2img or ControlNet work, describe the finished image. Strength, control scale and masks belong in workflow notes.

## Copy-ready examples

### Typography poster

```text
Screen-printed travel poster in a flat three-colour style. A lone sea kayak glides across a calm turquoise bay at sunrise, small in the lower third, with layered sandstone headlands behind it. The large headline "SALT COAST" runs across the top in bold condensed sans-serif lettering, and the smaller line "Paddle season opens" sits beneath the kayak. Warm coral sky, deep teal water, cream paper texture, clean margins.
```

### Photographic portrait

```text
Documentary photograph of an older beekeeper in a white veil jacket holding a honeycomb frame up to the light in a backyard apiary. Waist-up framing, frame held in both gloved hands at chest height, bees visible on the comb. Late-afternoon backlight makes the wax glow amber, soft rim light on the veil, shallow depth of field with blurred wooden hives behind. Natural colour, fine film grain.
```

### Split prompt for a surface with separate encoder fields

CLIP fields (`prompt`, `prompt_2`):

```text
Isometric 3D illustration of a tiny rooftop greenhouse cafe at dusk, warm window light, soft clay render
```

T5 field (`prompt_3`):

```text
Isometric 3D illustration of a tiny rooftop greenhouse cafe at dusk, rendered in soft matte clay with rounded edges. The glass greenhouse sits on a flat brick roof, with two small round tables inside, hanging fern baskets and a chalkboard on the door reading "OPEN". Strings of warm bulbs run from the greenhouse to a chimney. The surrounding rooftops fall away into a lilac and peach sky. Gentle ambient occlusion, pastel palette, centred composition with even margins.
```

## Repair the actual failure

| Observed problem | Useful revision | Keep outside the prompt |
| --- | --- | --- |
| Key detail ignored | Move it into the first sentence; cut the prompt below the CLIP limit or use a split prompt. | Whether T5 is loaded and the `max_sequence_length` value. |
| Wrong or garbled text | Quote the exact words, shorten them, name the surface and position, remove competing signage. | Canvas size; whether the variant or a dropped T5 is limiting typography. |
| Attributes swap between subjects | One sentence per subject with explicit position and ownership; use distinct nouns. | ControlNet or layout input if placement must be exact. |
| Anatomy or structure breaks (Medium) | Simplify the pose, name visible limbs and hand positions, reduce crowding. | Skip Layer Guidance and step count. |
| Negative prompt has no effect | On Turbo it is ignored at the baseline; rewrite as positive description. | Guidance value for the chosen variant. |
| Flat or synthetic look | Name a plausible light source, its direction and the material response; add a medium cue such as film grain or brush texture. | Guidance scale; lower values often look more natural on guided variants (author suggestion). |
| Edge artefacts on a long prompt (Medium) | Shorten the prompt, especially past 256 T5 tokens. | `max_sequence_length`. |
| Unexpected style drift between seeds | Name the medium and palette explicitly; the family varies by design across seeds. | Seed, style preset. |
| Cropped subject | Request the full silhouette, named extremities and comfortable margins. | Aspect ratio and source crop. |

## Negative prompt use

For Large or Medium, start empty unless there is a concrete reason. Keep it short and specific. For an observed unwanted watermark-like corner mark, a focused candidate is:

```text
watermark, corner logo, signature
```

Don't use that when the brief asks for a signature or logo. Never put "text" in the negative prompt when the image needs lettering, and don't add exclusions that contradict the requested subject or style. For Turbo, don't supply one at all at the documented baseline.

## Working from an existing prompt

Extract what is already correct before changing anything. Preserve exact text and identity constraints, remove contradictions, then rewrite only the weak parts. Convert SD1.5 or SDXL tag stacks ("masterpiece, best quality, 8k") into concrete visual description; they cost CLIP tokens without stating anything visible. Strip frontend-specific weights, BREAK tokens and LoRA tags unless the user's surface uses them. When asked for alternatives, vary framing, illumination or medium one at a time.

Use exact-copy checks for lettering and names. Treat supplied output images as evidence of failure; if no result is available, label a diagnosis as a hypothesis. A longer prompt is not automatically a better prompt.
