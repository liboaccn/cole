

def get(query, model):
    # messages = []
    # messages.append({"role": "user", "content": query})
    generation_config = {
        "temperature": model.temperature,
        "do_sample" :True,
        "top_k": 5,
        "top_p": 0.85,
        "repetition_penalty": 1.1,
        "max_new_tokens": 1024,
    }
    response, history = model.model.chat(model.tokenizer, query, **generation_config)

    # print('msg:',messages)
    # print('resp:',response)
    return response