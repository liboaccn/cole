def get(query, model):
    messages = []
    messages.append({"role": "user", "content": query})

    text = model.tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    model_inputs = model.tokenizer([text], return_tensors="pt").to(model.model.device)

    generated_ids = model.model.generate(
        model_inputs.input_ids,
        max_new_tokens=1024,
        temperature=model.temperature,
        do_sample = True,
        repetition_penalty = 1,
        top_k = 5,
        top_p = 0.85,     
    )
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]

    response = model.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]   
    # print('resp:',response)
    return response