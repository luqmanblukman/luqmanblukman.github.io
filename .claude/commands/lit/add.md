---
description: Add a paper to the reading list (metadata, BibTeX, your "why")
argument-hint: <url | arXiv id | DOI>
---
Follow `AGENTS.md`. Input: $ARGUMENTS

1. Resolve metadata (title, authors, year, venue, canonical link) from arXiv, DBLP or the publisher page. If the paper is ambiguous, show the candidates and ask which one.
2. Append a BibTeX entry to `references.bib` with key `<firstauthor><year><firstword>`. Skip if the key exists.
3. Ask Luqman whether he wants to say **why** this paper is on the list. It's optional. If he gives a reason, use it verbatim; if not, omit the `why` field.
4. Add an entry to the top of `reviews/reading-list.yml` with `title`, `authors` (e.g. "Jayaram et al."), `venue` (e.g. "arXiv 2026"), `path` (the paper link), `added` (today) and, only if he gave one, `why` (his words, verbatim). If the paper is already listed, say so and stop.
5. Don't summarise or characterise the paper.

End with:
---
**Next step:** Read it in passes. When you're ready to write, run `/lit:new <same link>`.
