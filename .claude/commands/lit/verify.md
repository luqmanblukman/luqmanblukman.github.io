---
description: Check every factual claim a review makes about the paper against the source
argument-hint: <review path>
---
Delegate to the `paper-critic` subagent with this brief:

> Verify the review at `$ARGUMENTS` against the paper in its frontmatter `link`. Read `AGENTS.md` first.
> List every factual claim the review makes **about the paper** (what it says, did, measured, reported, assumed). Skip the reviewer's own opinions.
> For each claim give: the review's sentence (quoted), a verdict of **found**, **not found** or **misread**, and the paper location (with a short quote) supporting the verdict. For "misread", state what the paper actually says.
> Don't comment on anything else. Return the table only.

Show the table verbatim. Summarise the counts in one line. Don't edit the review.

End with:
---
**Next step:** Fix any "not found" or "misread" claims yourself. When everything is "found", run `/lit:style <path>` or `/lit:publish <path>`.
