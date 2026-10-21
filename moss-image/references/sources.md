# MOSS Image: evidence and maintenance

Checked on 2026-10-22. These are concise authored summaries and original examples, not a copy of the upstream skill or a bundled inference runtime.

1. [MOSS-Image-SFT model card](https://huggingface.co/OpenMOSS-Team/MOSS-Image-SFT) [M1]

   Establishes the SFT checkpoint, supported prompt forms, sampling baseline and pipeline scope. SFT inherits the Base architecture; it isn't a separately established native reference editor.

2. [MOSS-Image-Base model card](https://huggingface.co/OpenMOSS-Team/MOSS-Image-Base) [M2]

   Establishes the Base checkpoint. The [OpenMOSS organisation](https://huggingface.co/OpenMOSS-Team) also lists unrelated language, vision-understanding, audio and video models; the user's MOS label is resolved to the image family here.

3. [Official MOSS Image user guide](https://github.com/OpenMOSS/MOSS-Image/blob/main/USERGUIDE.md) [M3]

   Establishes caption/tag/layout support, text handling, canvas conventions, centred yxyx layout coordinates and the distinction between current text-to-image and further reference-generation post-training. The separate captioning-for-training section uses different coordinates; don't import its watermark annotations into a generation layout.

4. [Official project repository](https://github.com/OpenMOSS/MOSS-Image) [M4]

   Primary refresh source for Base/SFT releases, implementation and model-specific guidance.

5. [Upstream prompt-enhancer skill](https://github.com/OpenMOSS/MOSS-Image/blob/main/skills/moss-image-prompt-enhancer/SKILL.md) [M5]

   Documents an optional draft/compiler workflow. Its top-left xyxy draft and final centred yxyx layout are separate representations. This package doesn't invoke, copy or require that helper.

## Boundaries

Settings and schema claims are version-scoped to these sources. Prompt examples and repair choices are author recommendations. No image inference or output-fidelity measurement was performed. The original organisation URL doesn't itself select a checkpoint; preserve an explicit Base, SFT or derivative name.

Refresh primary documentation before claiming new native editing, transparency or few-step support. An upstream skill's instructions describe that skill's own workflow; they don't grant permission to execute models, install dependencies or publish anything here.
