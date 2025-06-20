from fastapi import APIRouter, Body, Query
from app.backends.gpt4all_backend import GPT4AllBackend
from app.backends.petals_backend import PetalsBackend
from app.backends.deepspeed_backend import DeepSpeedBackend
from app.models.model_registry import get_available_models
from app.utils.voting import majority_vote

router = APIRouter()

INFERENCE_BACKENDS = {
    "gpt4all": GPT4AllBackend,
    "petals": PetalsBackend,
    "deepspeed": DeepSpeedBackend
}

@router.post("/")
def run_inference(
    prompt: str = Body(..., embed=True),
    backend: str = Query("gpt4all"),
    model_id: str = Query(None)
):
    """
    Seçilen backend ve model ile inference çalıştırır.
    """
    available_models = get_available_models(backend)
    if model_id is None:
        model_id = available_models[0]["id"]
    backend_class = INFERENCE_BACKENDS[backend]
    backend_instance = backend_class(model_id)
    response = backend_instance.generate(prompt)
    return {"output": response}

@router.post("/vote")
def multi_backend_vote(
    prompt: str = Body(..., embed=True)
):
    """
    Aynı prompt'u tüm backend'lere yollar, cevapları toplar ve majority voting uygular.
    """
    results = {}
    for backend, backend_class in INFERENCE_BACKENDS.items():
        model_id = get_available_models(backend)[0]["id"]
        backend_instance = backend_class(model_id)
        answer = backend_instance.generate(prompt)
        results[backend] = answer

    answers = list(results.values())
    consensus_answer, confidence = majority_vote(answers)

    return {
        "results": results,
        "consensus_answer": consensus_answer,
        "confidence": confidence
    }