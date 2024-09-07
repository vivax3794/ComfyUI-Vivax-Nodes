from .. import console, PURPLE_NAME, WILDCARD

import requests

class VIV_Message:
    @classmethod
    def INPUT_TYPES(s):
        return {
                "required": {
                    "role": (("user", "system", "assistant"), {"default": "user"}),
                    "message": ("STRING", {"default": "", "multiline": True}),
                    },
                "optional": {
                    "prev_message": ("MESSAGE[]", {"default": []}),
                    },
                }

    RETURN_TYPES = ("MESSAGE[]",)
    RETURN_NAMES = ("messages",)
    FUNCTION = "add"
    CATEGORY = "vivax/ollama"

    def add(self, role, message, prev_message=None):
        if prev_message is None:
            prev_message = []
        return prev_message + [{"role": role, "content": message}],

class VIV_Generate:
    @classmethod
    def INPUT_TYPES(s):
        return {
                "required": {
                        "messages": ("MESSAGE[]", {"default": []}),
                        "model": ("STRING", {"default": "mistral"}),
                        "seed": "INT",
                        "host": ("STRING", {"default": "http://ollama:11434"})
                    },
                }
    
    RETURN_TYPES = ("MESSAGE[]", "STRING")
    RETURN_NAMES = ("messages", "response")
    FUNCTION = "generate"
    CATEGORY = "vivax/ollama"

    def generate(self, messages, model, seed, host):
        console.print(f"{PURPLE_NAME} Generating with {len(messages)} messages.")
        response = requests.post(f"{host}/api/chat", json={"messages": messages, "model": model, "stream": False, "options": {"seed": seed}, "keep_alive": "10s"})
        response = response.json()
        message = response["message"]
        result = messages + [message], message["content"]

        return {"ui": {"response": [message["content"]]}, "result": result}

NODES2 = {
        "Ollama Message": VIV_Message,
        "Ollama Generate": VIV_Generate,
        }


