# FLUX 3 Image: identity and constraints

Reference check: 2026-10-23. Evidence labels resolve in [sources.md](sources.md). Settings are prompt-writing context, not instructions to run inference.

## Model identity

FLUX 3 Image is Black Forest Labs' hosted image generation and editing model, served at `https://api.bfl.ai/v1/flux-3-image`. It launched on 2026-10-01 as a single endpoint: the prompt and the presence of references decide whether a request generates or edits. There is no `mode` field. [F1, F2, F9]

No `pro`, `flex`, `max` or `dev` image variants are documented for FLUX 3. The only `version` value accepted is `latest`; dated release tags are announced as planned. Treat "FLUX 3 Image" as one moving target and record the check date when comparing prompts over time. [F2, F9]

The July 2026 FLUX 3 announcement describes one underlying multimodal model for image, video and audio, with image access through APIs and private weights. It names a future open-weight backbone, FLUX 3 Dev; no such image checkpoint was found on the Black Forest Labs Hugging Face organisation at the check date. Don't write prompts for it. [F10]

## Distinguish the siblings

| Model | Identity | Prompt-writing consequence |
| --- | --- | --- |
| FLUX 3 Image | Hosted flagship, `flux-3-image`. | This skill. The service expands prompts itself. |
| FLUX 3 Image Klein | 5.6B open-weights version, hosted at `flux-3-image-klein` and runnable locally with Distilled and Base checkpoints. | Use the separate Klein skill. Local Klein expects a pre-expanded caption and uses `from: "target"` for new box content. [F11] |
| FLUX.2 / FLUX.1 | Earlier generations with different endpoints and parameters. | Don't reuse their `prompt_upsampling`, `seed`, `input_image` or step guidance here. |

## Prompt-relevant behaviour

| Concern | Prompt-writing consequence |
| --- | --- |
| Automatic expansion | Before generating, the service expands the prompt into a detailed one and, for many edits, locates the named element and adds a box. The used prompt returns in `result.prompt`. A short request is valid; a precise brief can still be reinterpreted. [F4] |
| No expansion switch | No `prompt_upsampling` or `negative_prompt` field exists, and unknown fields are rejected with HTTP 422. Control intent through wording, not invented parameters. [F2, F7] |
| Grounding | `grounding` defaults to true, allowing web and image search on the prompt. Real-world names may be looked up; false uses only the prompt. Keep the setting outside the prompt. [F1, F2] |
| References | Up to ten `images`, each at least 256 x 256 and at most 16 MP, cited by position. [F3, F8] |
| Aspect ratio | `auto` by default: it follows the first reference, or 1:1 without one. Fifteen fixed ratios run from 21:9 to 9:21. Set the ratio for non-square generation and before designing boxes. [F2, F7] |
| Resolution | Tiers include `768sq`, `1k` (default), `2k` and `4k`; changing tier makes a new composition, not an upscale of the draft. [F2, F7] |
| Negative prompts | Describe what fills the space instead, such as "an empty promenade" rather than "no crowds". [F7] |
| Safety tolerance | `safety_tolerance` (0-7, default 2) is a route setting. Moderated requests or outputs return distinct statuses; don't promise wording that evades moderation. [F2, F3] |

## What wording cannot guarantee

A prompt cannot attach an absent reference, change the aspect ratio, toggle grounding or force pixel-identical preservation. Boxes guide placement rather than clipping. Native transparency, seeds and JSON-only prompts aren't documented for this endpoint; don't promise them.
