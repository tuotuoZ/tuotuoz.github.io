# Publish on GitHub Pages

The public source repository is [tuotuoZ/tuotuoz.github.io](https://github.com/tuotuoZ/tuotuoz.github.io). The publishing target is [https://tuotuoz.github.io](https://tuotuoz.github.io). Check the repository's Actions tab for the current deployment status.

1. Review the local preview, especially current roles, expected degree dates, the professional contact email, and the downloadable résumé.
2. Work **only in this `portfolio` directory**, excluding ignored development files. The parent folder contains job-search documents and must not be uploaded.
3. Review and commit the intended changes, then run `git push origin main` from this directory.
4. The supplied `Build and deploy portfolio` workflow runs on pushes to `main`. You can also run it manually from the repository's Actions tab.
5. When deployment succeeds, open the published site and verify the résumé download, visualization playback, and links.

The repository's **Settings → Pages → Build and deployment → Source** should be **GitHub Actions**. This custom site uses the supplied workflow, not GitHub's default Jekyll builder. Keep `url: https://tuotuoz.github.io` and an empty `baseurl` in `_config.yml` for the root personal-site address.

## Keep it free

GitHub Pages is free for a public repository. The `github.io` address needs no domain purchase. Keep the theme's MIT license in the repository.

Reference: [GitHub's custom Pages workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).
