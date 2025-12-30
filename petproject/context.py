import os
from pathlib import Path

CONTEXT_PATH = Path(os.environ.get("CONTEXT_PATH"))

CONTEXT = CONTEXT_PATH.read_text(encoding="utf-8").strip()