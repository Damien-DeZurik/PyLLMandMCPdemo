---
description: Regression-checks the Say It Ain't Faux page after an edit, ensuring no section or component was lost. Called by the `faux` orchestrator; not for general use.
mode: subagent
permission:
  edit: deny
---

# Faux page validator

Read-only. Compare the edited `faux/index.html` against the baseline `faux/.baseline.html` (both repo-root). Fail if any baseline structure is missing. Additions and intentional text changes are allowed.

Every item present in the baseline must still be present in the edit:
- Head: `<title>Say It Ain't Faux</title>`; links to w3.css, Roboto, Tangerine, and font-awesome.
- Inline `<style>` rules: `.faux-redbg`, `.faux-concertdates`, `.faux-linethrough`, `.faux-text-shadow`, `.faux-text-show`, `.w3-roboto`, `.w3-tangerine` (keep parity with the baseline).
- Navbar `w3-top`: HOME, BAND, DATES, CONTACT, the MORE dropdown (`#formats`, `#videos`), and the search icon.
- Mobile nav `#navDemo`: BAND, TOUR, CONTACT, MERCH.
- Hero image `images/Faux-icon-round-blue.png`.
- `#tour`: the "2026 DATES" heading and every baseline date `<li>` row (dates may not be dropped unless the request removed them).
- `#band`: "MEET THE BAND", the tagline, the Facebook link, and the member blocks (Faux Jo / Do / Je / Za / Na) with their `images/faux*.png`.
- `#videos`: "PHOTOS" and `images/StarTrek2024.png`.
- `#formats`: "TRIBUTE FORMATS" and all six formats.
- `#contact`: "CONTACT" plus the globe, Facebook, email, and map lines.
- `<footer>`: the Facebook icon and "Powered by Eugene Helix".
- `<script>`: `carousel()` and `myFunction()` still defined.

Method: `diff` the two files, and grep each `id="..."`, `href="#..."`, `images/...` src, `<h2>` text, and function name in both. Watch for the baseline's duplicate `id="videos"` and its commented-out `#ticketModal` block.

Output a `PASS` or `FAIL` verdict. On FAIL, list each missing item and where it appeared in the baseline. Never edit files.
