# Basit demo. Gerçek projede Petals'a bağlanan kod olmalı.
class PetalsBackend:
    def __init__(self, model_id):
        self.model_id = model_id
        # Gerçek projede burada Petals ile bağlantı yapılır.

    def generate(self, prompt):
        # Burada gerçek Petals inference çağrısı olmalı.
        # Demo için sabit cevap:
        return f"[Petals {self.model_id}] Yanıt: {prompt.upper()}"