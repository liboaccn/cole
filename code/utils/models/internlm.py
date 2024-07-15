



def get(query, model):

    # print(query)    
    response, history = model.model.chat(model.tokenizer, query, history=[],
        temperature=model.temperature,
        do_sample=True,
        max_new_tokens=1024,
        repetition_penalty = 1.1,
        top_k = 5,
        top_p = 0.85,
    )
    # print(response)
    return response