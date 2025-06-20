from fastapi import APIRouter, Query
from app.models.model_registry import get_available_models

router = APIRouter()

@router.get("/")
def list_models(backend: str = Query("gpt4all")):
    """
    Seçili backend için kullanılabilir modelleri listeler.
    """
    return get_available_models(backend)