# K-CURE Data Documentation

Source for an unofficial documentation site for the cancer and health data released through the Korean K-CURE portal (케이큐어). The site is built with [MkDocs](https://www.mkdocs.org) and the [Material](https://squidfunk.github.io/mkdocs-material/) theme, on the same pattern as the [NHIS Data Documentation](https://siho-park.github.io/nhis-documentation/).

The address in `mkdocs.yml` follows that pattern (`siho-park/kcure-documentation`). Change `site_url`, `repo_url`, and `repo_name` if the repository name differs.

## Repository layout

```text
docs/                 hand-written pages
docs/assets/          styles
overrides/            theme overrides
database/             official manuals, not committed (see .gitignore)
mkdocs.yml            site configuration and navigation
```

Variable pages are not generated yet. They should be built from the official data dictionary (자료설명서), the way the NHIS site builds its Variables section from layout files, once that dictionary is available locally. Place manuals in `database/` and do not commit them.

## Previewing locally

```bash
pip install -r requirements.txt
mkdocs serve
```

The site is then served at `http://127.0.0.1:8000` and rebuilds when a file changes. Because this folder sits in Dropbox, create any virtual environment outside it so that Dropbox does not sync the installed packages.

## Publishing

Pushing to the `main` branch runs `.github/workflows/deploy.yml`, which builds the site in strict mode and publishes it to the `gh-pages` branch. The repository settings need GitHub Pages set to deploy from that branch.
