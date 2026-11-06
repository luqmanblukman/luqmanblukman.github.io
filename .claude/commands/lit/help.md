---
description: List the /lit:* commands and where each fits in the review workflow
---
Print the following exactly. It's read-only, so don't run anything.

**Workflow:** pick a paper → read it in passes on your own → write the review → get it challenged → publish.

| Step | Command | What it's for |
|---|---|---|
| Pick | `/lit:add <url \| arXiv id>` | Adds a paper to the reading list with metadata and BibTeX. You give the "why". |
| Start | `/lit:new <url \| arXiv id>` | Scaffolds `reviews/<date>-<slug>/index.md` (frontmatter only, draft) and marks the paper "reviewing". |
| Read | `/lit:explain <paper> <section or term>` | Explains a concept or section you're stuck on, cites where it appears, hands it back to you. |
| Challenge | `/lit:critique <review>` | Coverage gaps (as questions), challenges to your interpretation, alternative explanations, overreach. Every point cites the paper. |
| Challenge | `/lit:probe <review> [area]` | Socratic questions on one area (e.g. method, evidence, context), starting with open questions only. |
| Challenge | `/lit:hint` | Moves the current probe question one rung up the hint ladder: open question → where to look → the concern. |
| Check | `/lit:verify <review>` | Checks every factual claim your review makes about the paper: found (with location), not found, or misread. |
| Polish | `/lit:style <review>` | Feedback on structure, flow, clarity and openings, without rewriting. Typo fixes only if you ask. |
| Publish | `/lit:publish <review>` | Final checks, removes `draft: true`, marks the paper "reviewed", commits. |
| Help | `/lit:help` | This list. |

Rules for all of them are in `AGENTS.md`: you write 90%+ of every review, and the AI critiques but never writes it.
