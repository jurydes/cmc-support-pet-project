from openai import OpenAI
import os


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
        self.base_url = os.getenv("BASE_URL") 
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        self.client = OpenAI(base_url=self.base_url,api_key=self.api_key)
        self.model = os.getenv("MODEL_NAME")
    
    def get_response(self, messages: list) -> str:
        """
        Возвращает ответ на запрос пользователя
        
        Args:
            messages(list): Сообщения, которые будут переданы модели
        
        Returns:
            Ответ модели

        Raises:
            ValueError: Если messages пустой или содержит только NaN
        """
        if (messages is None) or (not messages):
            raise ValueError("Сообщение не было передано!")
        
        client = self.client
        
        response = client.chat.completions.create(
            model=self.model,
            messages=messages
        )
        
        msg = response.choices[0].message.content
        return msg
