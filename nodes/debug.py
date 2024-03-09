from .. import console, WILDCARD

class VIV_Inspect:
    @classmethod
    def INPUT_TYPES(s):
        return {
                "required": {
                    "item": (WILDCARD,),
                    }
                }

    RETURN_TYPES = (WILDCARD,)
    RETURN_NAMES = ("*",)
    FUNCTION = "inspect"
    CATEGORY = "vivax/debug"
    OUTPUT_NODE = True

    def inspect(self, item):
        console.print("[bold yellow]INSPECT:[/bold yellow]", item)
        return (item,)

class VIV_Any_String:
    @classmethod
    def INPUT_TYPES(s):
        return {
                "required": {
                    "value": ("STRING", {"default": "photon_v1.safetensors"}),
                    }
                }

    RETURN_TYPES = (WILDCARD,)
    RETURN_NAME = ("value",)
    FUNCTION = "inspect"
    CATEGORY = "vivax/debug"
    OUTPUT_NODE = True

    def inspect(self, value):
        return (value,)
