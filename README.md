# luqmanblukman.github.io

Personal blog and paper reviews, built with [Quarto](https://quarto.org) and deployed to GitHub Pages by `.github/workflows/publish.yml`. Every deploy waits for approval on the `github-pages` environment; the rendered site is attached to each run as `site-preview`.

| Path | What's in it |
|---|---|
| `posts/` | Essays: `posts/<YYYY-MM-DD>-<slug>/index.md` |
| `reviews/` | Paper reviews, one folder each: `reviews/<YYYY-MM-DD>-<slug>/index.md`, plus any code or experiments |
| `reviews/reading-list.md` | Papers queued for review, and why |
| `references.bib` | BibTeX for citations (`[@key]`) |
| `AGENTS.md` | How AI assistants may help with this repo, and the review checklist |

## Local preview

```sh
quarto preview
```

Drafts (`draft: true`) appear in the preview but not on the live site.

## Reviewing a paper with Claude Code

Run `/lit:help` for the commands. In short: `/lit:add` a paper, read it in passes on your own, `/lit:new` to scaffold the post, write it, then `/lit:critique`, `/lit:probe`, `/lit:verify` and `/lit:style` before `/lit:publish`.
