"""Post-process lychee --format json output to add file:line locations."""

import json
import re
import sys
from pathlib import Path

from pydantic import BaseModel

# ANSI colours — only when writing to a real terminal
_TTY = sys.stdout.isatty()


def _c(code: str, text: str) -> str:
    return f"\033[{code}m{text}\033[0m" if _TTY else text


class _Status(BaseModel):
    text: str


class _LinkError(BaseModel):
    url: str
    status: _Status


class _LycheeOutput(BaseModel):
    error_map: dict[str, list[_LinkError]] = {}


def _display_url(url: str) -> str:
    """Convert file:// URLs to relative paths; leave other URLs unchanged."""
    if url.startswith("file://"):
        path_part = re.sub(r"^file://", "", url)
        file_path, _, fragment = path_part.partition("#")
        try:
            rel = Path(file_path).relative_to(Path.cwd())
            return f"{rel}#{fragment}" if fragment else str(rel)
        except ValueError:
            pass
    return url


def find_locations(filepath: str, url: str) -> list[tuple[int, int, str]]:
    # lychee normalizes relative file links to absolute file:// URLs.
    # Reconstruct a searchable pattern from just the basename + fragment.
    if url.startswith("file://"):
        path_part = re.sub(r"^file://", "", url)
        basename = path_part.split("/")[
            -1
        ]  # e.g. "task-1.md#6-authorize-in-swagger-ui"
        esc = re.escape(basename)
        # Only match the basename when it appears inside the URL delimiters
        # `(…)` or `"…"`, so we skip the display text of markdown links like
        # [`docker-compose.yml`](../../docker-compose.yml) and land on the URL.
        pattern = re.compile(r'(?<=\(|")(?:\.\.?/|[\w.-]+/)*' + esc)
    else:
        pattern = re.compile(re.escape(url.rstrip("/")))

    results: list[tuple[int, int, str]] = []
    try:
        with open(filepath) as f:
            for i, line in enumerate(f, 1):
                m = pattern.search(line)
                if m:
                    start = m.start()
                    raw_link = line[start : m.end()].rstrip()
                    results.append((i, start + 1, raw_link))
    except (OSError, UnicodeDecodeError):
        pass
    return results


raw = sys.stdin.read()
# lychee sometimes emits the JSON block twice; take the first complete object
raw_obj, _ = json.JSONDecoder().raw_decode(raw.lstrip())
data = _LycheeOutput.model_validate(raw_obj)

if not data.error_map:
    print("No broken links found.")
    sys.exit(0)

total = 0

for filepath, errors in data.error_map.items():
    try:
        relpath = Path(filepath).relative_to(Path.cwd())
    except ValueError:
        relpath = Path(filepath)
    for error in errors:
        locs = find_locations(filepath, error.url)
        display_link = _display_url(error.url)
        if locs:
            total += len(locs)
            for loc in locs:
                location = f"{relpath}:{loc[0]}:{loc[1]}"
                link = loc[2] if error.url.startswith("file://") else display_link
                print(f"{_c('1', location)}: {_c('1;31', '[ERROR]')} {_c('36', link)}")
                print(f"  {_c('2', error.status.text)}")
        else:
            total += 1
            print(
                f"{_c('1', str(relpath))}: {_c('1;31', '[ERROR]')} {_c('36', display_link)}"
            )
            print(f"  {_c('2', error.status.text)}")

print(
    f"\n{_c('1;31', f'Found {total} broken link(s) in {len(data.error_map)} file(s).')}"
)
sys.exit(1)
