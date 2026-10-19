#!/usr/bin/env bash
# Publish verified assets to an existing version tag. GitHub mutations happen here only.
set -euo pipefail

: "${GH_REPO:?Set GH_REPO to owner/repository}"
: "${GH_TOKEN:?Set GH_TOKEN to a token with contents:write}"
: "${RELEASE_TAG:?Set RELEASE_TAG to the existing version tag}"
: "${PRERELEASE:?Set PRERELEASE to true or false}"
[[ "$PRERELEASE" == 'true' || "$PRERELEASE" == 'false' ]] || exit 1
assets="${1:?Pass the release assets directory}"

# Verify locally before any API writes. A missing directory or bad hash stops publication.
(
  cd "$assets"
  sha256sum --check SHA256SUMS
)

release_list="$(mktemp)"
trap 'rm -f "$release_list"' EXIT
# List failures must stop publication rather than masquerade as a missing release.
gh api --paginate "repos/$GH_REPO/releases?per_page=100" \
  --jq '.[] | [.tag_name, .draft] | @tsv' > "$release_list"
existing_draft="$(awk -F '\t' -v tag="$RELEASE_TAG" '$1 == tag { print $2 }' "$release_list")"
if [[ "$existing_draft" == 'false' ]]; then
  echo "Release $RELEASE_TAG is already published; refusing to overwrite it."
  exit 1
fi
if [[ -z "$existing_draft" ]]; then
  gh release create "$RELEASE_TAG" \
    --verify-tag --draft --prerelease="$PRERELEASE" \
    --title "Text-to-image skills $RELEASE_TAG" --generate-notes
fi
# A failed upload leaves a draft. Rerunning safely replaces draft assets.
gh release upload "$RELEASE_TAG" "$assets"/* --clobber
gh release edit "$RELEASE_TAG" --verify-tag --draft=false \
  --prerelease="$PRERELEASE"
