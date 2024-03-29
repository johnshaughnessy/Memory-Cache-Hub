from memory_cache_hub.core.llm import ollama_completions, openai_compatible_completions
from memory_cache_hub.core.types import Message
from memory_cache_hub.core.files import write_file_summary, get_project_uploads_directory
import os

def summarize_file(server_url:str, model: str, root_directory: str, project_name: str, file_path: str):
    project_uploads_directory = get_project_uploads_directory(root_directory, project_name)

    # Check if the file exists
    if not os.path.exists(os.path.join(project_uploads_directory, file_path)):
        return False

    with open(os.path.join(project_uploads_directory, file_path)) as file:
        file_contents = file.read()

    messages = [
        Message(
            role="system",
            # Use a python multi-line string for "content":
            content="""
You are a helpful file summarization assistant.
When given a file, you create a short markdown summary.
You only respond with a summary. You never ask questions. You never provide additional information or conversational formalities.
Your response always begins with the file's name in a level 1 markdown header.
For example, if the user sends you a file named "src/core/webrtc_server.py", you respond with:
# src/core/webrtc_server.py

A WebRTC server implemented in python.

## Details

- The `WebRTCSignallingServer` class handles WebRTC signalling.
- The `WebRTCDataServer` class handles WebRTC data channels.
- The `WebRTCVideoServer` class handles WebRTC video channels.
"""),
        Message(
            role="user",
            content=f"Summarize this file ({file_path}):\n{file_contents}"
        )
    ]
    print(messages)
    print("Sending summary request to the server. This might take a while.")
    #reply = ollama_completions(server_url, model, messages)
    reply = openai_compatible_completions(server_url, model, messages)
    print(reply)
    write_file_summary(root_directory, project_name, file_path, reply)
    return True
