# Basit demo. Gerçek projede DeepSpeed ile model yüklenir.
class DeepSpeedBackend:
    def __init__(self, model_id):
        self.model_id = model_id
        # Gerçek projede DeepSpeed model yüklenir.

    def generate(self, prompt):
        # Burada gerçek DeepSpeed inference çağrısı olmalı.
        # Demo için sabit cevap:
        return f"[DeepSpeed {self.model_id}] Yanıt: {prompt.lower()}"