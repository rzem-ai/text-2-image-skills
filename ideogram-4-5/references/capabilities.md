# Ideogram 4.5: identity and constraints

Reference check: 2026-10-23. Bracketed evidence labels resolve in [sources.md](sources.md). Tables mix documented facts with explicitly labelled author suggestions. Settings are context for writing prompts, not instructions to execute a generation workflow.

## Model identity

Ideogram 4.5 is the current flagship Ideogram model: the help centre lists it as "our flagship model" and its model page positions it as the most precise edit model. It is hosted only: the Ideogram app (Image app, Precise Edit app, Studio), the Ideogram MCP and the v2 API. [I1, I10, I11]

| Surface | Identifier |
| --- | --- |
| API generate | `POST /v2/image/generate/ideogram-4-5` [I8] |
| API precise edit | `POST /v2/image/precise-edit/ideogram-4-5` [I9] |
| API replace background | A separate tool endpoint built on 4.5; takes an image and a background reference, no prompt field. [I17] |
| App | **Ideogram 4.5** in the Model picker; the **Edit** button opens Precise Edit, which runs 4.5. [I1, I7] |

No official release date appears on the model page; third-party coverage dates it to 30 September 2026. No 4.5 weights are confirmed as published. [I11, sources.md]

### Distinguish nearby versions

| Model | What differs for prompt writing |
| --- | --- |
| Ideogram 4.0 (`ideogram-4`, v1 `ideogram-v4`) | The open-weight 9.3B model released 3 June 2026. Text or JSON prompts, no reference images, quality as turbo/default/quality, very wide ratios. Remix in the API and app runs on 4.0 or 3.0, not 4.5. [I1, I12, I14] |
| Ideogram 4.0 Transparent | Separate prompt-only transparent model with its own prompt-upsampling control. [I1] |
| Ideogram 3.0 (`ideogram-3`, v1 `ideogram-v3`) | Plain text only, about 150 words effective. The only Ideogram model with style type (Auto/General/Realistic/Design), 62 style presets, style codes, up to 10 style reference images, negative prompt and colour-palette presets. Inpaint, Reframe and the 3.0 Replace Background endpoints are 3.0 tools. [I1, I2, I3, I16] |
| Ideogram 2.0, 2a and older | Legacy; may still appear in the picker. Don't carry their style or speed tiers forward. [I1] |
| Auto | Picks a model at run time; no Magic Prompt or Quality control. A prompt written for Auto may not run on 4.5. [I1] |
| Partner models in the app | GPT Image, Nano Banana, Z-Image, P-Image-Ideogram are other vendors' models with their own rules. [I1] |

## Prompt-relevant settings

| Concern | Prompt-writing consequence |
| --- | --- |
| Prompt format | Natural language or a structured Ideogram JSON prompt (same schema as 4.0). Up to 10,000 characters in the app; very long JSON can lose trailing elements, so list important elements first. [I3, I5, I8] |
| Magic Prompt | API `magic_prompt`: `auto` (default) and `on` rewrite and expand; `off` keeps wording and only converts it to the structured format. Valid JSON skips Magic Prompt unless it is `on`, which rewrites the JSON too. With source images every mode converts the instruction into a structured edit prompt; the app hides the toggle. [I2, I5, I8] |
| When to advise off | Exact copy, hand-written JSON, an approved brief, or a result where Magic Prompt added unwanted objects or text. Author suggestion: leave it on for short exploratory ideas or non-English input (it can translate to English). [I2, I13] |
| Negative prompt | None on 4.5 or 4.0. Rephrase exclusions positively or edit the result. Don't add a negative block. [I13] |
| Style controls | No style presets, style codes, style references or palette presets. Describe style in words, or use JSON `color_palette` hex lists as a soft bias. [I1, I5] |
| Size | Without sources: `auto` or a supported 1K/2K preset; app offers Auto or a ratio then 1K/2K, with 3:1 and 1:3 at 2K only. With sources: `auto`, `source` or custom `WIDTHxHEIGHT`, multiples of 32, at least 256px, area at most 2048x2048, ratio at most 6:1. A mask fixes output to the source size. [I2, I8] |
| Quality | App: Very low (references only), Low, Medium, High; High is the paid default. API default `high` without sources, `medium` with. [I2, I8] |
| Background | `transparent`, `opaque` or `auto`. Writing "transparent PNG" in the prompt does not set it; download PNG or WebP to keep alpha. [I2, I3, I8] |
| Seed | Helps compare prompt edits; doesn't guarantee identical output across settings or models. [I2] |

## What wording cannot guarantee

A prompt cannot set aspect ratio, image count, quality or transparency; flags such as `--ar` or weights such as `::1` and `(important)` are read as ordinary words. Hex colours steer rather than lock pixels, bounding boxes guide rather than fix layout, and quoted copy improves but doesn't guarantee spelling. Long passages, non-Latin scripts and accented letters remain less reliable than short English copy. [I3, I4, I5]

Use the user's selected surface as the scope of any refinement. Third-party wrappers of `ideogram-4-5` may expose different field names or defaults; preserve the user's interface and don't promote one surface's parameter into a model-wide rule.
