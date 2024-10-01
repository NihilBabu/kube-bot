from fastapi import FastAPI
from contextlib import asynccontextmanager
from .dependencies import load_llama_model

from .routers import model, chat


@asynccontextmanager
async def initialize_llama_model(app: FastAPI):
    load_llama_model()
    yield

app = FastAPI(lifespan=initialize_llama_model)

app.include_router(model.router)
app.include_router(chat.router)