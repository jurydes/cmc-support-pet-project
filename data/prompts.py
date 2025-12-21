from petproject.config import config

with open(config.sys_prompt, 'r') as file:  
        prompt = file.read()
    
with open(config.context, 'r') as file:  
    context = file.read()