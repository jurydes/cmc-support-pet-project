import os
from pathlib import Path

SYS_PROMPT_PATH = Path(os.environ.get("SYS_PROMPT_PATH"))

SYSTEM_PROMPT = SYS_PROMPT_PATH.read_text(encoding="utf-8").strip()
USER_PROMPT_TEMPLATE = "{}"