import os
import qianfan

def get(prompt, model):

    model_name = model.model_name

    chat_comp = qianfan.ChatCompletion()
    messages = [{
        "role": "user",
        "content": prompt
    }]
    response = chat_comp.do(
        model       = model_name,
        temperature = model.temperature,
        # extra_parameters = {},
        messages=[
            {"role": "user", "content": prompt}
        ]
    ) 
    return response.body['result']