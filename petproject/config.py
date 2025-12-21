from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, SecretStr 
from pathlib import Path

class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8')
    
    api_key: SecretStr = Field(alias='OPENROUTER_API_KEY')
    model_name: str = Field("arcee-ai/trinity-mini:free", description="Название модели")
    sys_prompt: Path = Field("data/sysprompt.txt", description="Путь к файлу с системным промптом")
    context: Path = Field("data/context.txt", description="Путь к файлу с контекстом")
    url: str = Field("https://openrouter.ai/api/v1", description="Базовый URL API")

config = Config()