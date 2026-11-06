---
description: Final checks, then publish a review (remove draft, update reading list, commit)
argument-hint: <review path>
---
Follow `AGENTS.md`. Input: $ARGUMENTS

1. Check, and report each as pass/fail:
   - Frontmatter complete: `title`, `paper_title`, `authors`, `venue`, `link`, `area`, `date`.
   - No `TODO` and no HTML comments left in the body. Quarto publishes HTML comments in the page source.
   - `/lit:verify` has been run in this conversation with no "not found" or "misread" left. If it hasn't, offer to run it now.
   - Every `[@key]` citation exists in `references.bib`.
2. If anything fails, stop and list what to fix.
3. If all pass, ask for confirmation. Then:
   - remove `draft: true`
   - set the reading-list status to `reviewed`
   - run `quarto render` to confirm it builds
   - commit `content: review <short title>` and push
4. Remind him that the deploy waits for his approval in GitHub Actions.
