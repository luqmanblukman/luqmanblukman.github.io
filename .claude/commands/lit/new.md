---
description: Scaffold a review post (frontmatter only, draft) for a paper
argument-hint: <url | arXiv id>
---
Follow `AGENTS.md`. Input: $ARGUMENTS

1. If the paper isn't on `reviews/reading-list.md`, run the `/lit:add` steps first.
2. Create `reviews/<today YYYY-MM-DD>-<short-slug>/index.md` containing **only** this frontmatter, filled from the metadata:
   ```yaml
   ---
   title: ""                 # Luqman's title for the review; leave empty
   paper_title: ""
   authors: []
   venue: ""                 # e.g. "arXiv 2026" or "NeurIPS 2025"
   link: ""
   code_data: ""             # repo/dataset links if the paper gives them; else empty
   area: ""
   date: <today>             # date reviewed
   categories: [paper-review]
   draft: true
   ---
   ```
   Leave the body empty: no headings, no template, no prompts. The structure is his.
3. Set the paper's status in the reading list to `reviewing` and link the Review column to the new file.
4. Ask whether he wants the paper saved to `.papers/` for offline reading (gitignored). Only download it if he says yes.

End with:
---
**Next step:** Write the review. When you have a full draft, run `/lit:critique <path>`.
