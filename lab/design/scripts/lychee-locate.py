"""Post-process lychee --format json output to add file:line locations.
"""

import json
import re
import sys

from pydantic import BaseModel


class _Status(BaseModel):
    text: str


class _LinkError(BaseModel):
    url: str
    status: _Status


class _LycheeOutput(BaseModel):
    error_map: dict[str, list[_LinkError]] = {}


def find_line(filepath: str, url: str) -> int | None:
    # lychee normalizes relative file links to absolute file:// URLs.
    # Reconstruct a searchable pattern from just the basename + fragment.
    if url.startswith("file://"):
        path_part = re.sub(r"^file://", "", url)
        basename = path_part.split("/")[-1]  # e.g. "task-1.md#6-authorize-in-swagger-ui"
        pattern = re.compile(re.escape(basename))
    else:
        pattern = re.compile(re.escape(url.rstrip("/")))

    try:
        with open(filepath) as f:
            for i, line in enumerate(f, 1):
                if pattern.search(line):
                    return i
    except (OSError, UnicodeDecodeError):
        pass
    return None


raw = sys.stdin.read()
# lychee sometimes emits the JSON block twice; take the first complete object
raw_obj, _ = json.JSONDecoder().raw_decode(raw.lstrip())
data = _LycheeOutput.model_validate(raw_obj)

if not data.error_map:
    print("No broken links found.")
    sys.exit(0)

for filepath, errors in data.error_map.items():
    for error in errors:
        lineno = find_line(filepath, error.url)
        location = f"{filepath}:{lineno}" if lineno else filepath
        print(f"{location}: [ERROR] {error.url}")
        print(f"  {error.status.text}")

sys.exit(1)
