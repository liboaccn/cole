import os
from openai import OpenAI

_llm = OpenAI(
    api_key   = os.getenv("API_KEY"),
    base_url  = os.getenv("BASE_URL"), 
)
def get(prompt, model):
    model_name  = model.model_name
    gpt_model = _llm
    # print('LLM:', gpt_model.api_key)
    response = gpt_model.chat.completions.create(
        model       = model_name,
        temperature = model.temperature,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content 

 