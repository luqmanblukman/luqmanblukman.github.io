---
description: Substance review of a written paper review (gaps, challenges, overreach)
argument-hint: <review path>
---
Delegate to the `paper-critic` subagent with this brief:

> Critique the review at `$ARGUMENTS` against the paper in its frontmatter `link`. Read `AGENTS.md` first.
> 1. **Coverage gaps:** walk the coverage checklist and Pass 1–5 questions. For each area the review omits or treats thinly, write one question. Never supply the missing content.
> 2. **Interpretation:** where the review's reading of the paper differs from what the paper says, quote both and ask what reconciles them.
> 3. **Alternative explanations and overreach:** where the review accepts a result the paper's evidence doesn't fully support, or misses an alternative explanation, raise it as a question with a location.
> Numbered, major/minor, each with a location in the paper. Return the report only.

Show the report to Luqman verbatim. Then ask which points he accepts, rejects (and why) or defers. Don't edit the review.

End with:
---
**Next step:** Revise it yourself. Use `/lit:probe <path> <area>` to dig into an area, or `/lit:verify <path>` once the claims are settled.
