from model import get_model
import os

def get_answer(*, sys_prompt, request, context) -> str:
    """
    Docstring for get_answer
    
    :param request: Description
    :type request: str
    :return: Description
    :rtype: str
    """
    model = get_model()

    messages = []
    
    messages = [
        {"role": "system", "content": sys_prompt},    
        {"role": "user", "content": context},           
        {"role": "user", "content": request} 
    ]
    
    response = model.chat.completions.create(
        model=os.getenv("MODEL_NAME"),
        messages=messages
    )
    
    return response.choices[0].message.content

def add_context(request: str) -> list[str]:
    """
    Docstring for add_context
    
    :param request: User request to the LLM
    :type request: str
    :return: User request to the LLM with prompt and context
    :rtype: str
    """
    with open(os.getenv("MODEL_SYS_PROMPT"), 'r') as file:  
        prompt = file.read()
        file.close()
    with open(os.getenv("MODEL_CONTEXT"), 'r') as file:  
        context = file.read()
        file.close()
    

    return prompt, request, context


def ai_request(*, request: str ="Hi! Tell me about yourself.") -> str:
    """
    Sends user request to the LLM and returns its answer
    
    :param request: User request to the LLM
    :type request: str
    :return: Answer from the LLM
    :rtype: str
    """
    sys_prompt, context_request, context = add_context(request)
    answer = get_answer(sys_prompt=sys_prompt, request=context_request, context=context)
    
    return answer
