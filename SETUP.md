# Publish on GitHub Pages

The site is configured for `https://tuotuoz.github.io`, based on the GitHub username in the source résumé. No remote repository has been created and no site has been published by this setup.

1. Review the local preview, especially current roles, expected degree dates, the professional contact email, and the downloadable résumé.
2. In GitHub, create a public repository named `tuotuoz.github.io`. If that repository already exists, inspect it first and merge this work deliberately; do not overwrite an existing site.
3. Publish **only this `portfolio` directory**, excluding ignored development files. The parent folder contains job-search documents and must not be uploaded.
4. Push the site source to the repository's `main` branch.
5. In the repository, select **Settings → Pages → Build and deployment → Source → GitHub Actions**. This custom site uses the supplied `Build and deploy portfolio` workflow, not GitHub's default Jekyll builder.
6. Run that workflow from the Actions tab, or push a new change to `main`.
7. When deployment succeeds, open the URL shown by the workflow and verify the résumé download and links.

## Alternative repository name

For a project repository such as `portfolio`, set `url: https://tuotuoz.github.io` and `baseurl: /portfolio` in `_config.yml`. The site then lives at `https://tuotuoz.github.io/portfolio/`. All authored internal links use Jekyll's `relative_url` filter.

The included automated checks currently target the root personal-site configuration. If using a project prefix, adapt the checker before changing the deployment configuration.

## Keep it free

GitHub Pages is free for a public repository. The `github.io` address needs no domain purchase. Keep the theme's MIT license in the repository.

Reference: [GitHub's custom Pages workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).
