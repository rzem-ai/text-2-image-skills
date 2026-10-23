# Ideogram 4.5: evidence and maintenance

Checked on 2026-10-23. These embedded references are concise, original summaries with original prompt examples. They are not verbatim copies of vendor manuals and do not depend on sibling skill packages.

## Sources

1. [Ideogram help: Models](https://docs.ideogram.ai/create/models) [I1]

   Model comparison: 4.5 reference images, 10,000-character prompt, quality options and Background; 4.0 wide ratios and no references; 3.0 as the only model with style presets, style references, negative prompt and colour palette; Transparent, Auto, partner and legacy 2.0/2a models.

2. [Ideogram help: Image Settings](https://docs.ideogram.ai/create/image-settings) [I2]

   Aspect ratios and 1K/2K resolution, Size with references, quality per model, Magic Prompt behaviour and translation, Background, seed, and the 3.0-only style, preset, style-reference, negative-prompt and palette controls.

3. [Ideogram help: Prompting Basics](https://docs.ideogram.ai/prompting/prompting) and [Prompt Structure](https://docs.ideogram.ai/prompting/prompt-structure) [I3]

   Sentences over tag lists, main idea first, positive phrasing, no hidden weight or flag syntax, settings outside the prompt, part order, and the 3.0 length warning versus the 4.5 character limit.

4. [Ideogram help: Text in Images](https://docs.ideogram.ai/prompting/text-in-images) [I4]

   Quoted exact text, early placement, location, letterform description, multiple blocks in reading order, limits for long passages and non-Latin scripts, and text fixes.

5. [Ideogram help: JSON Prompting](https://docs.ideogram.ai/prompting/json-prompting) [I5]

   The shared 4.5/4.0 schema, field order, `photo` versus `art_style`, palette limits, 0-1000 y-first boxes, schema fallback to plain text and Magic Prompt interaction.

6. [Ideogram help: Reference Images](https://docs.ideogram.ai/create/reference-images) [I6]

   Reference limits per model, `@` mentions and reference roles, the 4.5 switch to edit-instruction mode, Size controls and consistent-character guidance.

7. [Ideogram help: Masks and Inpainting](https://docs.ideogram.ai/edit/masks-and-inpainting) and [Edit Images](https://docs.ideogram.ai/edit/edit) [I7]

   Precise Edit on 4.5, mask tools, reference limits with and without a mask, edit windows, Precise Edit settings and multi-turn editing.

8. [API: Generate with Ideogram 4.5](https://developer.ideogram.ai/v2/api-reference/images/generate/ideogram-4-5) [I8]

   Endpoint, `magic_prompt` values, `images`, mask polarity, `size` rules, `background`, `quality` defaults and the structured-prompt option.

9. [API: Precise edit with Ideogram 4.5](https://developer.ideogram.ai/v2/api-reference/images/precise-edit/ideogram-4-5) [I9]

   Source, up to four `reference_images` (three with a mask), mask polarity, `context_window`, output dimensions and exact copying of unchanged pixels.

10. [API overview](https://developer.ideogram.ai/v2/ideogram-api/api-overview) and [v2 documentation index](https://developer.ideogram.ai/v2/llms.txt) [I10]

    v2 path pattern, the 4.5/4.0/3.0 endpoint list including 3.0 inpaint and reframe, and the v1-to-v2 mapping (`ideogram-v4`, `ideogram-v3`).

11. [Ideogram 4.5 model page](https://ideogram.ai/models/4.5/) [I11]

    Precise-edit positioning, availability in the app, MCP and API, native 2K quality modes and edit types. It gives no release date and doesn't confirm 4.5 weights.

12. [Ideogram 4.0 announcement](https://ideogram.ai/blog/ideogram-4.0/) [I12]

    4.0 as the 9.3B open-weight model of 3 June 2026, trained on structured JSON captions.

13. [Ideogram help: Fix Common Problems](https://docs.ideogram.ai/prompting/fix-common-problems) [I13]

    No negative-prompt field on 4.5 or 4.0, positive rephrasing, Magic Prompt side effects, framing, contradiction and style fixes, and Studio Reframe/Extend.

14. [Ideogram help: Remix](https://docs.ideogram.ai/edit/remix) and [API: Remix with Ideogram 4.0](https://developer.ideogram.ai/v2/api-reference/images/remix/ideogram-4) [I14]

    Remix runs on Auto, 4.0 or 3.0 with a strength control; the API remix prompt is always an edit instruction.

15. [How to edit product photos with Ideogram 4.5](https://ideogram.ai/blog/ideogram-4-5-product-photo-editing/) [I15]

    Component naming, preservation phrasing, reference cropping and roles, branching in multi-turn edits and common product-edit failures.

16. [API v1: Ideogram 3.0 generate](https://developer.ideogram.ai/api-reference/api-reference/generate-v3) [I16]

    3.0 `style_type`, `style_codes`, `style_reference_images`, `negative_prompt` and `color_palette` fields, used only to mark the 3.0 boundary.

17. [API: Replace background with Ideogram 4.5](https://developer.ideogram.ai/v2/api-reference/tool/replace-background-ideogram-45) [I17]

    Image plus background reference, no prompt field.

18. [Ideogram help: Upscale](https://docs.ideogram.ai/edit/upscale) [I18]

    Upscale as a separate app with its own upscaler models and scale limits.

19. [Ideogram help: Make a Logo](https://docs.ideogram.ai/create/logos) and [Blog Posts](https://docs.ideogram.ai/about-ideogram/blog-posts) [I19]

    Logo prompting, transparency on 4.5 or 4.0 Transparent, raster output, and the help centre's description of 4.5 as the flagship model.

## Conflicts and unverified points

- **Release date.** The official model page and API docs give no 4.5 release date. Third-party coverage (for example [OrcaRouter](https://www.orcarouter.ai/zh-CN/blog/ideogram-4-5-launch-precise-edit-model)) reports 30 September 2026; treat that as unconfirmed.
- **Open weights.** The 4.5 page links the open-source 4.0 repository and collection but doesn't state that 4.5 weights exist. Third-party reports say none were published as of mid-October 2026. Don't describe 4.5 as open-weight.
- **Quality values.** The app and the model page list Very low, Low, Medium and High for 4.5. The generate API reference names only `very_low`, `medium` and `high`, and the Precise Edit reference lists `very_low` and `high`. Use the user's surface; don't assert `low` is accepted by every endpoint.
- **Reference counts.** "Up to 5" on generate counts the edited image; Precise Edit counts one source plus up to four references (three with a mask). The app describes the mask as using a reference slot. Keep the wording per surface.
- **Size limits.** Help and API agree on a 2048x2048 pixel area cap rather than a per-side cap; the model page shows zoom editing on a 24.2 MP source through an edit window, which is not generation resolution.

## Evidence boundaries

Model identity and documented controls come from the sources above. Suggested composition, example prompts and repair strategies are author recommendations. No image inference, Magic Prompt run, latency benchmark, commercial-licence review or account access test was performed while building this package. Price and rate limits are deliberately omitted because this is a prompt-writing package.

For a new or changed capability, revisit the exact model's primary documentation. If sources conflict, retain version and surface scope and disclose the uncertainty. Don't resolve a disagreement by silently substituting another model. Browse when asked for current verification or when the embedded facts don't answer a material question; ordinary prompt drafting can use these local references.
