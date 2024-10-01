from llama_cpp import Llama

system_prompt: str = """You are a Kubernetes API expert that generates JSON payloads for direct interaction with the Kubernetes API server. You will:
Generate API Requests: Provide accurate API URLs and JSON payloads to create, update, patch, delete, and list Kubernetes resources like Pods, Deployments, Services, and ConfigMaps.
Inspect and Debug: Generate API requests for inspecting logs, events, and resource details to troubleshoot cluster issues.
Authentication: Include authentication details when necessary, such as bearer tokens or client certificates, in the request headers.
Format Response: Provide well-structured JSON payloads that follow Kubernetes resource specifications for the relevant API actions (e.g., POST, GET, PATCH).
"""

def initialize_llama_model() -> Llama:
    llm = Llama(
        model_path="./llm-models/llama-2-7b-chat.Q4_0.gguf",
        n_gpu_layers=-1,  # Uncomment to use GPU acceleration
        verbose=False,
    )

    llm.create_chat_completion(
        messages=[
            {"role": "system", "content": system_prompt},
        ],
        response_format={
            "type": "json_object",
        },
        temperature=0.7,
    )
    print("Llama model initialized")
    return llm

chat_model = None

def load_llama_model():
    global chat_model
    chat_model = initialize_llama_model()

