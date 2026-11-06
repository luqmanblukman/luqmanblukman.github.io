---
description: Add a paper to the reading list (metadata, BibTeX, your "why")
argument-hint: <url | arXiv id | DOI>
---
Follow `AGENTS.md`. Input: $ARGUMENTS

1. Resolve metadata (title, authors, year, venue, canonical link) from arXiv, DBLP or the publisher page. If the paper is ambiguous, show the candidates and ask which one.
2. Append a BibTeX entry to `references.bib` with key `<firstauthor><year><firstword>`. Skip if the key exists.
3. Ask Luqman: **why is this paper on the list?** Use his answer verbatim.
4. Add a row to `reviews/reading-list.md`: `Authors, *Title*, year ([link](link))`, his why, `queued`, empty Review column. If the paper is already listed, say so and stop.
5. Don't summarise or characterise the paper.

End with:
---
**Next step:** Read it in passes. When you're ready to write, run `/lit:new <same link>`.
