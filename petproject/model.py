from openai import OpenAI
from schemas import Messages
from config import config


class Model:
    """
    LLM, которая отвечает на запросы юзера

    Attributes:
        base_url (str): Базовый URL API OpenRouter
        api_key(str): Ключ авторизации OpenRouter
        model(str): Название модели
    """

    def __init__(self):
        """Инициализирует модель"""
        self.base_url = config.url
        self.api_key = config.api_key.get_secret_value()
        self.client = OpenAI(base_url=self.base_url,api_key=self.api_key)
        self.model = config.model_name
    
    def get_response(self, messages: Messages) -> str:
        """
        Возвращает ответ на запрос пользователя
        
        Args:
            messages(Messages): Сообщения, которые будут переданы модели
        
        Returns:
            Ответ модели

        Raises:
            ValueError: Если messages пустой или содержит только NaN
        """
        if not messages:
            raise ValueError("Сообщение не было передано!")
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages.unwrap()
        )
        
        msg = response.choices[0].message.content
        return msg

model = Model()