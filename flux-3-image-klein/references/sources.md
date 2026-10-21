# FLUX 3 Image Klein: evidence and maintenance

Checked on 2026-10-22. These authored summaries and examples are embedded for offline prompt writing; they don't execute the model or copy its official rewriter.

1. [FLUX 3 Image Klein model card](https://huggingface.co/black-forest-labs/flux-3-image-klein) [F1]

   Establishes distilled identity, component distinction, 16-step/no-CFG baseline, reference count and the need for expanded captions. It explicitly limits box-based preservation claims.

2. [Official prompt-upsampler model card](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup) [F2]

   Establishes the separate Qwen3.5-9B rewriter, LLM substitution, generation/edit/layout modes and reference-aware expansion. Its weights aren't run by this skill.

3. [BFL layout prompting guide](https://docs.bfl.ai/guides/prompting_layout) [F3]

   Establishes caption IDs, element descriptions, generation rows and placement guidance.

4. [BFL FLUX 3 bounding-box guide](https://docs.bfl.ai/flux_3/flux3_image_bounding_boxes) [F4]

   Establishes the final integer top-left 0-1000 y-first grid and hosted edit-row fields. Its hosted API examples use `from: null` for new elements; that isn't the local Klein PUP convention.

5. [Klein PUP system prompts](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup/blob/main/system_prompts.json) and [local box validation code](https://github.com/black-forest-labs/flux-3-image-klein/blob/main/src/flux3/bbox.py) [F5]

   Establish zero-based reference IDs and `from: "target"` for newly generated content in the local workflow. These are inspected format definitions, not instructions to impersonate or run the upstream system.

6. [Official Klein inference repository](https://github.com/black-forest-labs/flux-3-image-klein) [F6]

   Primary refresh source for the distilled/Base distinction, separate input-box conveniences and pre-expanded-prompt handoff. Base CFG examples differ from the model card; this package doesn't prescribe Base settings.

## Boundaries

No generation, PUP execution, latency benchmark, licence assessment or fidelity test was performed. Original captions and repair strategies are author recommendations. Documentation from the wider hosted FLUX 3 family must not override a local Klein implementation's schema without verification. In particular, preserve the separate first-reference index and new-content conventions described above.

Recheck the exact checkpoint and surface before claiming a new parameter, alpha output or strict preservation capability. Settings and tool invocation belong outside the copy-ready visual prompt.
