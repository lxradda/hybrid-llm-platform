def get_available_models(backend):
    if backend == "gpt4all":
        return [
            {"id": "tinyllama", "name": "TinyLlama"},
            {"id": "phi3-mini", "name": "Phi-3 Mini"}
        ]
    elif backend == "petals":
        return [{"id": "bigscience/bloom-petals", "name": "BLOOM (Petals)"}]
    elif backend == "deepspeed":
        return [{"id": "bigscience/bloom", "name": "BLOOM (DeepSpeed)"}]
    return []