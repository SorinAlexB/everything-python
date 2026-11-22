import json
import sys
from pathlib import Path

import requests

# Make the project folder importable so we can reach tool/tool.py
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from tools.tools import TOOL_REGISTRY, get_full_system_prompt, extract_tool_invocations
# if the file is tools.py:  from tool.tools import ...

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen3.5:0.8b"

YOU_COLOR = "\033[94m"        # blue
ASSISTANT_COLOR = "\033[93m"  # yellow
RESET_COLOR = "\033[0m"


def execute_llm_call(conversation):
    resp = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "messages": conversation,
        "stream": False,
        "think": True,
    })
    resp.raise_for_status()
    return resp.json()["message"]["content"]


def run_coding_agent_loop():
    system_prompt = get_full_system_prompt()
    print(system_prompt)
    conversation = [{"role": "system", "content": system_prompt}]

    while True:
        try:
            user_input = input(f"{YOU_COLOR}You:{RESET_COLOR} ")
        except (KeyboardInterrupt, EOFError):
            break

        conversation.append({"role": "user", "content": user_input.strip()})

        while True:
            assistant_response = execute_llm_call(conversation)
            tool_invocations = extract_tool_invocations(assistant_response)
            conversation.append({"role": "assistant", "content": assistant_response})
            print(conversation)

            if not tool_invocations:
                print(f"{ASSISTANT_COLOR}Assistant:{RESET_COLOR} {assistant_response}")
                break

            for name, args in tool_invocations:
                print(f"[tool] {name} {args}")
                tool = TOOL_REGISTRY.get(name)

                if tool is None:
                    resp = {"error": f"unknown tool '{name}'. Available: {list(TOOL_REGISTRY)}"}
                else:
                    try:
                        resp = tool(**args)
                    except Exception as e:
                        resp = {"error": f"{type(e).__name__}: {e}"}

                conversation.append({
                    "role": "user",
                    "content": f"tool_result({json.dumps(resp)})"
                })


if __name__ == "__main__":
    run_coding_agent_loop()

"""
conversation variable keeps the entire history from system prompt all the way to the fial output prompt. if a tool is called(even if it does not exist) 
the program will keep it as history in the conversation and afterwards the llm will read the conversation and see the output of the tool

e.g.
"list evrything from this directory <path>"
first in conversation will be loaded the sys prompt and the query prompt
llm sees the request and returns a json format for a tool call
tool checking phase, adding the tool to the history conversation. afterwards the while loop repets
no tool is called so it will go to the llm response(llm reads the history and answer), llm generates an output and the conversation ends
"""