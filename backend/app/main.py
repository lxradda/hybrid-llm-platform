from fastapi import FastAPI
from app.api import inference, models

app = FastAPI(
    title="Hybrid LLM Platform",
    description="Local, Distributed, Cluster LLM Inference API"
)

app.include_router(inference.router, prefix="/inference", tags=["Inference"])
app.include_router(models.router, prefix="/models", tags=["Model Management"])