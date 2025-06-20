# Basit örnek. Gerçek projede GPT4All Python modülü kullanılmalı.
class GPT4AllBackend:
    def __init__(self, model_id):
        self.model_id = model_id
        # Gerçek projede burada model yüklenir.

    def generate(self, prompt):
        # Burada gerçek inference çağrısı olmalı.
        # Demo için sabit cevap:
        return f"[GPT4All {self.model_id}] Yanıt: {prompt[::-1]}"