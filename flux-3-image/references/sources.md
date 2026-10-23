# FLUX 3 Image: evidence and maintenance

Checked on 2026-10-23. These are original summaries and examples for offline prompt writing. They don't execute the model and don't depend on sibling packages.

## Sources

1. [BFL FLUX 3 Image overview](https://docs.bfl.ai/flux_3/flux3_image_overview) [F1]

   Supports: hosted identity, single endpoint for generation and editing, up to ten references, box grid and grounding default.

2. [BFL FLUX 3 Image API reference](https://docs.bfl.ai/api-reference/utility/generate-an-image-with-flux-3) [F2]

   Supports: request schema (`prompt`, `images`, `aspect_ratio`, `resolution`, `width`/`height`, `safety_tolerance`, `grounding`, `user`, `version`), rejection of unknown fields, aspect-ratio list and `version: latest`.

3. [BFL FLUX 3 Text to Image](https://docs.bfl.ai/flux_3/flux3_image_generate) [F3]

   Supports: endpoint, reference size limits, quoted-text guidance, statuses including Reasoning and moderation, and `result.prompt`.

4. [BFL FLUX 3 Image Editing](https://docs.bfl.ai/flux_3/flux3_image_layout) [F4]

   Supports: instruction style, automatic expansion with added boxes, `auto` aspect ratio and preservation caveats.

5. [BFL FLUX 3 Image bounding-box guide](https://docs.bfl.ai/flux_3/flux3_image_bounding_boxes) [F5]

   Supports: y-first 0-1000 grid, generation and edit row fields, `ref_image_0` indexing, `from: null` for new content and the small-box failure note.

6. [BFL layout prompts guide](https://docs.bfl.ai/guides/prompting_layout) [F6]

   Supports: caption with `<id>` tokens, per-axis grid stretching and text elements.

7. [BFL style, aesthetics and text guide](https://docs.bfl.ai/guides/prompting_unified_style) and [technical parameters guide](https://docs.bfl.ai/guides/prompting_unified_technical) [F7]

   Supports: quoted lettering, `\n` line breaks, object-bound hex codes, Style/Mood tags, absence of negative-prompt and upsampling fields, positive replacement wording, aspect and resolution behaviour. Some style examples in the first guide were produced with FLUX.2.

8. [BFL multi-reference editing guide](https://docs.bfl.ai/guides/prompting_editing_multi_reference) [F8]

   Supports: positional references, roles, base-image-first ordering and placement as a strong hint.

9. [BFL release notes](https://docs.bfl.ml/release-notes) [F9]

   Supports: 2026-10-01 launch, single endpoint without `mode`, resolution tiers and absence of named variants.

10. [Announcing FLUX 3](https://bfl.ai/blog/flux-3) [F10]

    Supports: one multimodal model family, phased early access, image access through APIs and private weights, and FLUX 3 Dev as the named open-weight backbone.

11. [BFL FLUX 3 Image Klein](https://docs.bfl.ai/flux_3/flux3_image_klein) and [Klein model card](https://huggingface.co/black-forest-labs/flux-3-image-klein) [F11]

    Supports: Klein as a separate compact open-weights model with its own endpoint, used here only to draw the boundary.

## Conflicts and unverified points

- Resolution tiers: the API reference also lists `1.5k` and an edit-only `match_input`; the release notes and technical guide list only `768sq`, `1k`, `2k` and `4k`. This package mentions only the common four.
- Prompt expansion: the editing guide describes automatic expansion and returned `result.prompt`, while the technical guide says no `prompt_upsampling` field exists. Read together, expansion is always on and not user-switchable; the Reasoning status isn't explained in the docs.
- Grounding: the API schema and overview document it for FLUX 3 Image; the release notes only mention grounding for FLUX.2 [max].
- No reference-count limit is stated on the bounding-box page; ten comes from the overview, generation, editing and API pages.
- Hex codes, JSON-only structured prompts, seeds, transparency and prompt length limits aren't documented for this endpoint. The hex guidance relies on one FLUX 3 style-guide example.
- No public non-Klein FLUX 3 image weights were found on the Black Forest Labs Hugging Face organisation at the check date.

## Evidence boundaries

Example prompts, coordinates and repair strategies are author recommendations. No generation, latency test, licence review or account-access check was performed. Prices are omitted. Recheck the API reference before claiming a new parameter, variant, dated version or preservation guarantee; keep settings outside the copy-ready prompt.
