from model import Model
from config import project_config
from prompts import Loader

loader = Loader(
    sys_prompt_path=project_config.sys_prompt_path,
    context_path=project_config.context_path,
)

model = Model()

def get_prompt_and_context(request: str) -> list[str]:
    """
    Загружает системный промпт и контекст из файлов
    
    Args:
        request(str): Исходный запрос пользователя
        
    Returns:
        Список из трех строк: [системный промпт, пользовательский промпт]
    """
    prompt = loader.load_system_prompt()
    context = loader.load_context()

    user_prompt = f"Контекст: {context}\n\nВопрос: {request}"

    return [prompt, user_prompt]


def ai_request(*, request: str = "Привет! Расскажи о себе.") -> str:
    """
    Точка входа для получения ответа
    
    Args:
        request: Запрос пользователя. 
            По умолчанию "Hi! Tell me about yourself."
        
    Returns:
        Ответ модели на запрос
    """
    prompt, user_prompt = get_prompt_and_context(request)
    answer = model.get_answer(sys_prompt=prompt, request=user_prompt)
    
    return answer
