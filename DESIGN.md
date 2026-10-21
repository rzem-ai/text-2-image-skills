---
name: Text / Image
description: A technical field guide to model-specific image-prompt skills.
colors:
  paper: "#f7f6f0"
  ink: "#1e3029"
  muted: "#536258"
  rule: "#ccd3c6"
  accent: "#dce8b7"
  action: "#285b42"
  field: "#fffef9"
  panel: "#1e3029"
  panel-ink: "#f3f5e9"
  panel-muted: "#c5d1c1"
  focus: "#276347"
  dark-paper: "#121e19"
  dark-ink: "#e8eee2"
  dark-muted: "#b2c1b2"
  dark-rule: "#3f5345"
  dark-action: "#c2d8a3"
  dark-field: "#1b2b23"
  dark-panel: "#243a2d"
  dark-focus: "#dce8b7"
typography:
  display:
    fontFamily: '"Source Serif 4", Georgia, serif'
    fontSize: "clamp(2.9rem, 5.5vw, 4.75rem)"
    fontWeight: 500
    lineHeight: 1.08
    letterSpacing: "-.035em"
  headline:
    fontFamily: '"Source Serif 4", Georgia, serif'
    fontSize: "clamp(1.9rem, 3vw, 2.6rem)"
    fontWeight: 500
    lineHeight: 1.18
    letterSpacing: "-.02em"
  title:
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'
    fontSize: "1.2rem"
    fontWeight: 700
    lineHeight: 1.4
  body:
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif'
    fontSize: ".86rem"
    fontWeight: 550
    lineHeight: 1.6
  code:
    fontFamily: '"SFMono-Regular", Consolas, "Liberation Mono", monospace'
    fontSize: ".86em"
rounded:
  control: "7px"
  status: "9px"
  panel: "16px"
spacing:
  step-4: "4px"
  step-8: "8px"
  step-12: "12px"
  step-16: "16px"
  step-20: "20px"
  step-24: "24px"
  step-26: "26px"
  step-28: "28px"
  step-32: "32px"
  step-36: "36px"
  step-44: "44px"
  step-70: "70px"
components:
  copy-button:
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: "9px 15px"
    typography: "{typography.label}"
  copy-button-hover:
    backgroundColor: "{colors.accent}"
    textColor: "#1e3029"
  download-link:
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: "10px 18px"
  search:
    backgroundColor: "{colors.field}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: "10px 16px"
  family-filter-selected:
    backgroundColor: "{colors.accent}"
    textColor: "#1e3029"
    rounded: "{rounded.control}"
    padding: "9px 15px"
  installation-panel:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.panel-ink}"
    rounded: "{rounded.panel}"
    padding: "32px"
---

# Design System: Text / Image

## Overview

A quiet technical field guide for finding and installing model-specific image-prompt skills. Serif headings introduce the content; compact sans-serif labels and monospace commands keep the catalogue practical.

The page uses open space, fine rules and one contrasting installation panel. Its visual character comes from the warm paper and green palette, with the same hierarchy adapted to the reader's system dark-mode preference.

**Key Characteristics:**
- Serif headings paired with system sans-serif text.
- A ruled catalogue with compact, legible actions.
- Automatic light and dark colours; wrapping command text on small screens.

## Colors

The frontmatter records the literal light-theme colours and the changed dark-theme roles. CSS custom properties in `site/assets/site.css` remain the implementation source; the `dark-` entries apply only under `prefers-color-scheme: dark`.

The primary action colour is a subdued green for links, caret and the wordmark dot. The pale accent marks selected filters, control hover states and text selection. Paper, ink, muted text, rules and fields provide the neutral structure. The installation panel has its own background, text and secondary text; its text colours remain unchanged in dark mode. Focus has a separate high-visibility role.

**The Theme Pairing Rule.** Use the corresponding dark role when the system selects dark mode; preserve the existing contrast relationships.

## Typography

Source Serif 4 is self-hosted at weight 500 for the main heading and section headings, with Georgia as fallback. The platform sans-serif stack supplies body text, navigation, model titles and controls. Monospace distinguishes commands and inline code.

The display and section heading scales are fluid. Model titles use the title role; ordinary paragraphs inherit the body role, with smaller supporting descriptions and metadata. Control labels use the label role. Code is relative to its surrounding text; the installation panel sets its command explicitly to .93rem. Paragraphs normally stop at 70ch, with narrower introductory copy and slightly wider model descriptions.

## Layout

The centred page container is at most 1200px wide with 48px side gutters. At 900px and below the gutters become 28px; at 680px and below they become 20px. The introduction and installation guidance use two columns above the smaller breakpoint, then stack. The catalogue has ruled rows with text on the left and actions on the right; at the smaller breakpoint each row stacks its actions below the description.

Search is at most 560px wide. Family controls wrap. Interactive navigation, links and buttons generally have a minimum 44px height; search has a 50px minimum height. Commands wrap within available width using overflow wrapping, including long package names and options, so they don't widen the page on phones. Section spacing is deliberately broader than control spacing; the frontmatter lists repeated observed spacing values rather than imposing a new scale.

## Elevation & Depth

The interface is flat and has no shadows. Fine borders separate sections and catalogue entries; the installation panel uses a contrasting fill. The copy status sits above content through fixed positioning and stacking order, without a shadow. Smooth anchor scrolling is disabled for reduced-motion preferences; controls have no decorative animation.

## Shapes

Controls have gently rounded corners using the control radius. The installation panel is more rounded, and the transient copy status uses its own intermediate radius. Catalogue entries and the overall page remain open, without card outlines. Borders are one pixel. Keyboard focus uses a three-pixel outline offset four pixels from the control, coloured with the focus role.

## Components

Copy and reset buttons use transparent fills, fine borders and a pale accent on hover. Copy buttons inside the installation panel inherit the panel text and border colours. The download link uses an ink border and reverses its foreground and background on hover.

The search field has a distinct field surface, a visible label and muted placeholder. Family filters use transparent resting states, a fine hover border and a filled selected state tied to `aria-pressed`. Navigation is plain text, underlined on hover, with reduced spacing and type size at the phone breakpoint.

Model rows combine a title, family label, description, documentation/download links and an expandable installation command. JavaScript progressively adds search, family filtering and copy controls; the base catalogue remains readable without it. Empty results expose a clear-filter control, and copy feedback uses an accessible status region.

## Do's and Don'ts

- Do use the existing colour roles in both system themes.
- Do keep model rows separated with fine rules and open space.
- Do preserve visible keyboard focus and the implemented minimum control heights.
- Do let command text wrap and keep catalogue actions usable at phone widths.

- Don't replace the catalogue rows with an unrelated card system.
- Don't introduce shadows or decorative motion into the existing flat interface.
- Don't hide install commands or essential catalogue links behind JavaScript.
