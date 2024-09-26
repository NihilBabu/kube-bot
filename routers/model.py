from fastapi import APIRouter

router = APIRouter(prefix="/model", tags=["model"])


@router.get("/hello")
async def model_hello():
    return {"msg": "Hello world"}


@router.get("/llama")
async def chat():
    return {}
