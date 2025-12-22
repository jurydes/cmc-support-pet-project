from pathlib import Path
from functools import lru_cache

class Loader:
    """Класс для загрузки системного промпта и контекста"""
    def __init__(self, sys_prompt_path: Path, context_path: Path):
        self._sys_prompt_path = sys_prompt_path
        self._context_path = context_path

    @lru_cache
    def load_system_prompt(self) -> str:
        """Загрузка системного промпта"""
        return self._sys_prompt_path.read_text(encoding="utf-8")
    
    @lru_cache
    def load_context(self) -> str:
        """Загрузка контекста"""
        return self._context_path.read_text(encoding="utf-8")
