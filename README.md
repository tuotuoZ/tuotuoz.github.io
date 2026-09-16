# Boming Zhang — digital portfolio

An education and professional portfolio built from [al-folio v1.2](https://github.com/alshedivat/al-folio/releases/tag/v1.2).

## Preview locally

With Docker running:

```sh
docker compose -p boming-portfolio up -d
```

Open <http://localhost:4173/>. Edits to content reload automatically. The preview is bound to your computer only.

To stop it:

```sh
docker compose -p boming-portfolio down
```

Alternatively, preview with Ruby 3.3 and Node 20 installed locally. On this Mac:

```sh
export PATH="/opt/homebrew/opt/ruby@3.3/bin:/opt/homebrew/opt/node@20/bin:$PATH"
export BUNDLE_PATH=vendor/bundle
bundle install
bundle exec jekyll serve --host 127.0.0.1 --port 4173
```

Stop the local server with Ctrl+C before starting the Docker preview on the same port.

## Edit content

| Content                                 | File                                 |
| --------------------------------------- | ------------------------------------ |
| Homepage                                | `_pages/home.md`                     |
| About                                   | `_pages/about.md`                    |
| Teaching philosophy                     | `_pages/philosophy.md`               |
| Inspiration and resources               | `_pages/resources.md`                |
| Résumé facts                            | `_data/cv.yml`                       |
| Downloadable résumé                     | `assets/pdf/Boming_Zhang_Resume.pdf` |
| Project overview pages                  | `_projects/*.md`                     |
| Name, URL, feature settings             | `_config.yml`                        |
| Contact links                           | `_data/socials.yml`                  |
| Visualization videos and teaching notes | `_data/visualizations.yml`           |

The homepage is automatically included in al-folio's navigation; leave `nav: false` on `_pages/home.md` to avoid duplicating it.

This site uses an empty `baseurl` for a personal `github.io` address. Upstream examples using `/al-folio` refer to the template demo, not this site.

No local theme overrides are needed. The layout, dark mode, search, and responsive navigation use al-folio's pinned plugins.

### Add another visualization

1. Add a browser-compatible MP4 to `assets/video/` and a representative poster image to `assets/img/visualizations/`.
2. Add an entry in `_data/visualizations.yml`, using the first entry as a model. Give it a unique `id`, title, video and poster paths, duration, summary, learning goal, classroom prompt, and written description of the visuals.
3. It appears automatically on **Selected work → Visual explanations**. The player leaves playback to the visitor and loads only metadata until played.

For videos with spoken audio, provide an accurate caption track and update the player to include it. The first uploaded animation has no audio track; its written visual explanation provides a text alternative.

See [publishing instructions](SETUP.md) and [content provenance](CONTENT_SOURCES.md). Both files are excluded from the generated website.

## Validation

```sh
npm ci
npm run lint:prettier
npm run lint:style-contract
docker compose -p boming-portfolio exec -T jekyll bundle exec al-folio upgrade audit
docker compose -p boming-portfolio exec -T -e JEKYLL_ENV=production jekyll bundle exec jekyll build --destination /tmp/portfolio-production
docker cp boming-portfolio-jekyll-1:/tmp/portfolio-production/. _site
python3 scripts/check_site.py _site
```

The publishing workflow builds and validates the site before deploying it. The upstream theme code retains its [MIT license](LICENSE).
