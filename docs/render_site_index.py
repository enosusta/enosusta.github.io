"""Render the root GitHub Pages index with optional verification metadata."""

import os
import sys
from html import escape
from pathlib import Path


VERIFICATION_MARKER = "  <!-- google-site-verification -->"


def render(source: Path, destination: Path) -> None:
    html = source.read_text(encoding="utf-8")
    if html.count(VERIFICATION_MARKER) != 1:
        raise RuntimeError(
            f"Expected exactly one verification marker in {source}"
        )

    token = os.environ.get("GOOGLE_SITE_VERIFICATION", "").strip()
    replacement = ""
    if token:
        escaped_token = escape(token, quote=True)
        replacement = (
            '  <meta name="google-site-verification" '
            f'content="{escaped_token}">'
        )

    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        html.replace(VERIFICATION_MARKER, replacement),
        encoding="utf-8",
    )


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("usage: render_site_index.py SOURCE DESTINATION")
    render(Path(sys.argv[1]), Path(sys.argv[2]))


if __name__ == "__main__":
    main()
