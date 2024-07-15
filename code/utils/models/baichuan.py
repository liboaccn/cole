


from transformers.generation.utils import GenerationConfig

def get(query, model):
    messages = []
    messages.append({"role": "user", "content": query})
    generation_config = GenerationConfig(
        temperature=model.temperature,
        do_sample=True,
        assistant_token_id =  196,
        bos_token_id = 1,
        # do_sample =  true,
        eos_token_id = 2,
        max_new_tokens = 1024,
        pad_token_id =  0,
        repetition_penalty = 1.1,
        top_k = 5,
        top_p = 0.85,
        # transformers_version =  "4.31.0",
        user_token_id =  195,
    )
    model.model.generation_config = generation_config

    # response = model.model.chat(model.tokenizer, messages,temperature=model.temperature,do_sample=True)
    response = model.model.chat(model.tokenizer, messages)
    print('msg:',messages)
    print('resp:',response)
    return response