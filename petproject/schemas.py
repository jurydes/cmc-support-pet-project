from pydantic import BaseModel
from enum import Enum

class Role(str, Enum):
    """Роль"""
    SYSTEM = "system"
    USER = "user"

class Message(BaseModel):
    """Сообщение"""
    role: Role
    content: str

    def unwrap(self) -> dict:
        return {"role" : self.role, "content" : self.content}
    
class Messages(BaseModel):
    """Список сообщений"""
    messages: list[Message]    

    def add_msg(self, msg: Message):
        """Добавляет сообщение в список"""
        self.messages.append(msg)

    def create_add_msg(self, role: str, content: str):
        """Создает сообщение по наполнению и добавляет в список"""
        self.messages.append(Message(role=role, content=content))

    def unwrap(self) -> list[dict]:
        """Разворачивает список, делая его удобным для OpenRouter"""
        return [msg.unwrap() for msg in self.messages]
