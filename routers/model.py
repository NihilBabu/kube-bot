from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/model", tags=["model"])


@router.get("/hello")
async def model_hello():
    return {"msg": "Hello world"}


class ChatRequest(BaseModel):
    message: str
    provider: str

@router.post("/chat")
async def chat(request: ChatRequest):
    from ..dependencies import chat_model

    output = chat_model.create_chat_completion(
        messages=[
            {"role": "user", "content": request.message},
        ],
        response_format={
            "type": "json_object",
        },
        temperature=0.7,
    )
    return {"response": output}
