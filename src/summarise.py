import os
import sys

sys.path.append(os.path.abspath("src"))

from models import llm, llm1, llm2

model = llm1

def summarise(user_query,text):
    prompt_template = f"Provide a detailed response to the following question based on the context provided.\nQuestion: {user_query}\nContext:\n{text}"
    prompt_template_1 = f"Provide a detailed response to the following question based on the context provided.\nQuestion: {user_query}\nContext:\n{text}\
        Instructions: 1. Format the output into points.\
        2. Include the information that is only related to the User Query."
    
    result = model.invoke(prompt_template_1)

    if model == llm:
        return result.content
    
    elif model == llm1:
        return result
    else:
        return result.content