"""Unit-test configuration — runs before any test module is imported."""

import os

# The import chain (routers → database → settings) requires API_KEY.
# Unit tests never call the real API, so a dummy value is sufficient.
os.environ.setdefault("API_KEY", "test")
