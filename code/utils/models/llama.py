

from transformers.generation.utils import GenerationConfig
def get(query, model):
    # messages = []

    inputs = model.tokenizer(
        [query], return_tensors="pt", add_special_tokens=False
    )
    generation_config = GenerationConfig(
        temperature=model.temperature,
        do_sample=True,
        top_k=5,
        top_p=0.85,
        repetition_penalty=1.1,
        max_new_tokens=1024, 
    )
    generate_ids = model.model.generate(
        input_ids=inputs["input_ids"].to(model.model.device),
        attention_mask=inputs["attention_mask"].to(model.model.device), 
        eos_token_id=model.tokenizer.eos_token_id,
        pad_token_id=model.tokenizer.pad_token_id, 
        generation_config=generation_config
    )
    # print(query)
    output = model.tokenizer.decode(generate_ids[0],skip_special_tokens=True).split("[/INST]")[-1].strip()
    
    return output