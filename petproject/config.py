from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, SecretStr 


class Config(BaseSettings):
    """Глобальные параметры конфигурации приложения"""
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8')
    
    api_key: SecretStr = Field(alias='OPENROUTER_API_KEY')
    model_name: str = Field("arcee-ai/trinity-mini:free", description="Название модели")
    url: str = Field("https://openrouter.ai/api/v1", description="Базовый URL API")
