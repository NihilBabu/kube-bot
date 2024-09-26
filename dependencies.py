from llama_cpp import Llama

system_prompt: str = """You are a Kubernetes API expert that generates JSON payloads for direct interaction with the Kubernetes API server. You will:
Generate API Requests: Provide accurate API URLs and JSON payloads to create, update, patch, delete, and list Kubernetes resources like Pods, Deployments, Services, and ConfigMaps.
Inspect and Debug: Generate API requests for inspecting logs, events, and resource details to troubleshoot cluster issues.
Authentication: Include authentication details when necessary, such as bearer tokens or client certificates, in the request headers.
Format Response: Provide well-structured JSON payloads that follow Kubernetes resource specifications for the relevant API actions (e.g., POST, GET, PATCH).
"""


def load_model():

    llm = Llama(
        model_path="./models/llama-2-7b-chat.Q4_0.gguf",
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

    output = llm(
        "Q: List all pods A: ",  # Prompt
        max_tokens=None,  # Generate up to 32 tokens, set to None to generate up to the end of the context window
        stop=[
            "Q:",
            "\n",
        ],  # Stop generating just before the model would generate a new question
        echo=True,  # Echo the prompt back in the output
    )  # Generate a completion, can also call create_completion

    print(output)
    return


load_model()
