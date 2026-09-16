"""Check built portfolio links, required pages, and content hygiene using stdlib."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else "_site").resolve()
required = ["index.html", "about/index.html", "cv/index.html", "philosophy/index.html",
            "resources/index.html", "projects/index.html", "projects/ai-tutor/index.html",
            "projects/mathspring/index.html", "projects/visual-explanations/index.html",
            "assets/pdf/Boming_Zhang_Resume.pdf"]
errors = []

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()
        self.nav = False
        self.nav_links = []
        self.meta = {}
        self.visible_text = []
        self.hidden_text_depth = 0
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style"):
            self.hidden_text_depth += 1
        if tag == "nav":
            self.nav = True
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "a" and self.nav:
            self.nav_links.append(a.get("href"))
        if tag == "meta":
            self.meta[a.get("property", a.get("name", ""))] = a.get("content", "")
        for key in ("href", "src", "poster"):
            if a.get(key):
                self.links.append(a[key])
    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.hidden_text_depth = max(0, self.hidden_text_depth - 1)
        if tag == "nav":
            self.nav = False
    def handle_data(self, data):
        if not self.hidden_text_depth:
            self.visible_text.append(data)

phone_pattern = re.compile(r"(?<!\w)(?:\+?1[\s.-]?)?(?:\(\d{3}\)|\d{3})[\s.-]?\d{3}[\s.-]?\d{4}(?!\d)")
postal_patterns = (
    re.compile(r"\b[A-Z]{2}\s+\d{5}(?:-\d{4})?\b"),
    re.compile(r"\b(?:ZIP|postal)\s*(?:code)?\s*[:\-]?\s*\d{5}(?:-\d{4})?\b", re.IGNORECASE),
)

for name in required:
    if not (root / name).is_file():
        errors.append(f"Missing {name}")
pages = {}
for path in root.rglob("*.html"):
    page = Page()
    text = path.read_text()
    page.feed(text)
    pages[path] = page
    for sample in ("Albert Einstein", "You R. Name", "you@example.com", "Lorem ipsum"):
        if sample in text:
            errors.append(f"Unexpected source/demo content in {path.relative_to(root)}: {sample}")
    visible_text = " ".join(page.visible_text)
    if phone_pattern.search(visible_text) or any(link.lower().startswith("tel:") for link in page.links):
        errors.append(f"Unexpected phone contact in {path.relative_to(root)}")
    if any(pattern.search(visible_text) for pattern in postal_patterns):
        errors.append(f"Unexpected postal address in {path.relative_to(root)}")
    if path.name == "index.html" and path.relative_to(root).parts[0] != "assets":
        if not page.meta.get("description") or not page.meta.get("og:title"):
            errors.append(f"Missing page metadata in {path.relative_to(root)}")

for path, page in pages.items():
    for link in page.links:
        url = urlsplit(link)
        if url.scheme or url.netloc:
            continue
        if not url.path:
            target = path
        elif url.path.startswith("/"):
            target = root / unquote(url.path.lstrip("/"))
        else:
            target = path.parent / unquote(url.path)
        if target.is_dir():
            target = target / "index.html"
        target = target.resolve()
        if not target.exists():
            errors.append(f"Broken link in {path.relative_to(root)}: {link}")
        elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
            errors.append(f"Missing fragment in {path.relative_to(root)}: {link}")

home = pages.get(root / "index.html")
if home and home.nav_links.count("/") != 1:
    errors.append("Homepage navigation should contain one Home link")
cv = (root / "cv/index.html").read_text() if (root / "cv/index.html").exists() else ""
if cv.count("Expected December 2026") != 2:
    errors.append("Both pending degrees must show Expected December 2026")
for name in ("CONTENT_SOURCES.md", "SETUP.md", "README.md", "scripts/check_site.py"):
    if (root / name).exists():
        errors.append(f"Internal documentation leaked into build: {name}")
if errors:
    print("\n".join(errors))
    raise SystemExit(1)
print(f"Validated {len(pages)} HTML pages: internal links, required content, metadata, and document exclusions passed.")
