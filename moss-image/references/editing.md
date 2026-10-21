# MOSS Image: layout revisions and source-image briefs

## Establish the mode

The consulted official Base/SFT materials document text-to-image and layout-to-image. They don't establish a general native image-to-image or masked editing interface. Reference-conditioned community variants and further post-training are distinct workflows. [M1, M3]

When the user asks to edit a generated image, first distinguish a change to the prompt/layout from an operation on the existing image. Don't promise image preservation from a prompt-only revision. If an established compatible image-conditioned workflow is supplied, tailor a desired-result brief to its documented controls without inventing an image input for the official pipeline.

## Revise a layout

Keep the approved overall scene, exact visible strings and unaffected item descriptions. Change only the intended item fields. Retain the original canvas when reusing centred boxes; if the user changes dimensions, recalculate every affected coordinate. A same-seed rerender can still change details and isn't a pixel-preserving edit.

For the botanical layout in [prompting.md](prompting.md), a footer revision means replacing its `text` value with the user's exact new wording, then checking that the original box still fits it. If the new line is too long, adjust type hierarchy or the box coherently rather than dropping words. Deliver the complete updated JSON, not a fragment that must be guessed into place.

## Source-based regeneration example

This is a conditional desired-result caption for a separately established image-conditioned workflow, not a claim that MOSS-Image-SFT accepts an image attachment:

```text
A documentary-style photograph matching the supplied plant-stall composition: three terracotta pots of ferns stand on the same weathered timber table, with the cream sign leaning against the middle pot. Replace the sign lettering with the exact words "LOCAL FERNS" in large dark-green capitals. Preserve the relative pot positions, leaf shapes, camera viewpoint, pale green fence and soft post-rain daylight. Keep the complete table arrangement in frame, with no additional lettering.
```

If the image hasn't been supplied, don't claim to have inspected its leaves, sign or viewpoint. Request the needed source or clearly label the description as an assumption. Exact product identity and pixel-identical surroundings need more than a regeneration caption.
