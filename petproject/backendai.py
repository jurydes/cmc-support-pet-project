from model import Model


model = Model()

def ai_request(*, request: str = "Привет! Расскажи о себе.") -> str:
    """
    Точка входа для получения ответа
    
    Args:
        request: Запрос пользователя. 
            По умолчанию "Hi! Tell me about yourself."
        
    Returns:
        Ответ модели на запрос
    """
    
    answer = model.get_answer(user_request=request)
    
    return answer
