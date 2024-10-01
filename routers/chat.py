import uuid

from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import JSONResponse

from ..util.files import create_chat_file

class ChatRequest(BaseModel):
    user_prompt: str
    provider: str
    chat_id: str | None

class ChatPrompt(BaseModel):
    system_prompt: str
    user_prompt: str
    assistant_prompt: str | None

router = APIRouter(prefix="/chat", tags=["chat"])

@router.post("/chat")
async def create_chat(request: ChatRequest):

    chat_id = request.chat_id or str(uuid.uuid4())

    chat_data = ""
    # Create a new JSON file for the chat
    create_chat_file(chat_id)

    # Prepare the response
    response_data = {"chat_id": chat_id}
    return JSONResponse(content=response_data)