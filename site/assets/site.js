"use strict";

const rows = [...document.querySelectorAll(".skill-row")];
const search = document.querySelector("#model-search");
const filterButtons = [...document.querySelectorAll("[data-family-filter]")];
const results = document.querySelector("#results");
let family = "all";

function filterModels() {
  const query = search.value.trim().toLocaleLowerCase();
  let count = 0;
  for (const row of rows) {
    const matches = (family === "all" || row.dataset.family === family)
      && row.dataset.search.includes(query);
    row.hidden = !matches;
    count += Number(matches);
  }
  for (const button of filterButtons) {
    button.setAttribute("aria-pressed", String(button.dataset.familyFilter === family));
  }
  results.textContent = `Showing ${count} of ${rows.length} skills`;
  document.querySelector("#empty-state").hidden = count !== 0;
}

document.querySelector(".catalogue-tools").hidden = false;
search.addEventListener("input", filterModels);
for (const button of filterButtons) {
  button.addEventListener("click", () => {
    family = button.dataset.familyFilter;
    filterModels();
  });
}
document.querySelector("#reset-filters").addEventListener("click", () => {
  search.value = "";
  family = "all";
  filterModels();
  search.focus();
});

let statusTimer;
function announce(message) {
  const status = document.querySelector("#copy-status");
  window.clearTimeout(statusTimer);
  status.textContent = message;
  statusTimer = window.setTimeout(() => { status.textContent = ""; }, 4500);
}

async function copyCommand(button) {
  const command = button.dataset.copy;
  let copied = false;
  try {
    await navigator.clipboard.writeText(command);
    copied = true;
  } catch {
    const field = document.createElement("textarea");
    field.value = command;
    field.setAttribute("readonly", "");
    field.style.position = "fixed";
    field.style.left = "-9999px";
    document.body.append(field);
    field.select();
    try { copied = document.execCommand("copy"); } catch { copied = false; }
    field.remove();
    button.focus({ preventScroll: true });
  }
  if (copied) {
    announce(`Copied install command for ${button.dataset.label}.`);
  } else {
    const details = button.closest(".skill-row")?.querySelector("details");
    if (details) details.open = true;
    announce("Copy unavailable. Select and copy the displayed command instead.");
  }
}

for (const button of document.querySelectorAll("[data-copy]")) {
  button.hidden = false;
  button.addEventListener("click", () => copyCommand(button));
}
