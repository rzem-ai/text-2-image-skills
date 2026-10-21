# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Product Purpose

A basic GitHub Pages site for the text-2-image-skills repository. The user confirmed the focus: a searchable catalogue, copyable installation commands and individual downloads.

## Users

Readers choosing a model-specific prompt-writing skill and installing it into an agent or downloading a standalone package. This audience is inferred from the repository's existing README and skills.sh support.

## Capabilities and Constraints

The catalogue currently contains 17 independent prompt-writing skills, each with embedded references. The site must use catalog.json as its source of truth, distinguish current-source downloads from tagged releases, and preserve individual packages. It must not imply that the skills execute image generation or that examples were rendered and benchmarked.

Hosting is GitHub Pages, as explicitly requested. Plain static HTML, CSS and JavaScript with a Python build step are the implementation choice for this basic site; no application server is needed.

## Evidence on Hand

catalog.json, each model's SKILL.md and references, README.md, the MIT licence and the deterministic packaging script. GitHub releases exist, but the latest release can lag the current catalogue.

## Product Principles

- Make the model and installation command easy to find.
- Keep documentation and downloads useful without JavaScript.
- Generate catalogue content and packages together to avoid stale download links.
- Use the project's real content and avoid invented output samples or performance claims.
