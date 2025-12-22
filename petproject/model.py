from openai import OpenAI
from schemas import Messages, Message
from config import project_config


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
        self.base_url = project_config.url
        self.api_key = project_config.api_key.get_secret_value()
        self.client = OpenAI(base_url=self.base_url,api_key=self.api_key)
        self.model = project_config.model_name
    
    def build_message(self, messages: Messages) -> str:
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

    def get_answer(self, sys_prompt: str, request: str) -> str:
        """
        Получает ответ от LLM на основе системного промпта, контекста и запроса
        
        Args:
            sys_prompt(str): Системный промпт, определяющий поведение модели
            request(str): Обогащенный контекстом запрос пользователя
            
        Returns:
            Ответ языковой модели в виде строки
        """
        messages = Messages(messages=[
            Message(role="system", content=sys_prompt),
            Message(role="user", content=request)
        ])
        
        response = self.build_message(messages)
        
        return response
