from pathlib import Path
import json

def create_chat_file(chat_id: str) -> Path:
   data_dir = Path("./data")
   data_dir.mkdir(exist_ok=True)
   
   chat_file = data_dir / f"{chat_id}.json"
   chat_file.touch()
   return chat_file

def write_chat_data(chat_id: str, data: dict) -> None:
    chat_file = create_chat_file(chat_id)
    chat_file.write_text(json.dumps(data, indent=2))