from rich.console import Console

console = Console(color_system="truecolor", force_terminal=True)

PURPLE_NAME = "[bold purple]VIVAX: [/bold purple]"
console.print(f"{PURPLE_NAME} Nodes package loaded.")

from .nodes.debug import *
from .nodes.model_url import *

NODE_CLASS_MAPPINGS = {
        "Inspect": VIV_Inspect,
        "Any String": VIV_Any_String,
        "Model From URL": VIV_Model_From_URL,
        }


MANIFEST = {
        "name": "VIVAX",
        }
