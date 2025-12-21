from model import model
from config import config
from schemas import Messages, Message

def get_answer(*, sys_prompt: str, request: str, context: str) -> str:
    """
    Получает ответ от LLM на основе системного промпта, контекста и запроса
    
    Args:
        sys_prompt(str): Системный промпт, определяющий поведение модели
        request(str): Основной запрос пользователя
        context(str): Дополнительный контекст для запроса
        
    Returns:
        Ответ языковой модели в виде строки
    """
    messages = Messages(messages=[
        Message(role="system", content=sys_prompt),
        Message(role="user", content=f"Контекст: {context}\n\nВопрос: {request}")
    ])
    
    response = model.get_response(messages)
    
    return response

def add_context(request: str) -> list[str]:
    """
    Загружает системный промпт и контекст из файлов
    
    Args:
        request(str): Исходный запрос пользователя
        
    Returns:
        Список из трех строк: [системный промпт, исходный запрос, контекст]
    """
    with open(config.sys_prompt, 'r') as file:  
        prompt = file.read()
    
    with open(config.context, 'r') as file:  
        context = file.read()
    
    return [prompt, request, context]

def ai_request(*, request: str = "Hi! Tell me about yourself.") -> str:
    """
    Точка входа для получения ответа
    
    Args:
        request: Запрос пользователя. 
            По умолчанию "Hi! Tell me about yourself."
        
    Returns:
        Ответ модели на запрос
    """
    prompt, context_request, context = add_context(request)
    answer = get_answer(sys_prompt=prompt, request=context_request, context=context)
    
    return answer
