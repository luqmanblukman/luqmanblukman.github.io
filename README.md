# luqmanblukman.github.io

Personal blog, built with [Quarto](https://quarto.org) and deployed to GitHub Pages by `.github/workflows/publish.yml`.

The **Literature review** section is pulled from [luqmanblukman/lit-review](https://github.com/luqmanblukman/lit-review) at build time. A push to lit-review triggers a rebuild through `repository_dispatch`.

## Local preview

```sh
./prepare-lit-review.sh ../lit-review   # re-run after lit-review changes
quarto preview
```

## New post

Create `posts/<YYYY-MM-DD>-<slug>/index.qmd` with `title`, `date` and `categories` in its frontmatter.
