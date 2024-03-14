from rich.console import Console

console = Console(color_system="truecolor", force_terminal=True)

class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False

WILDCARD = AnyType("*")

PURPLE_NAME = "[bold purple]VIVAX: [/bold purple]"
console.print(f"{PURPLE_NAME} Nodes package loaded.")

from .nodes.debug import *
from .nodes.model_url import *
from .nodes.batch_loop import *
from .nodes.io_stuff import NODES

NODE_CLASS_MAPPINGS = {
        "Inspect": VIV_Inspect,
        "Any String": VIV_Any_String,
        "Model From URL": VIV_Model_From_URL,
        "Chunk Up": VIV_Chunk_Up,
        "Get Chunk": VIV_Get_Chunk,
        "Join Chunks": VIV_Join_Chunks,
        }
NODE_CLASS_MAPPINGS.update(NODES)


MANIFEST = {
        "name": "VIVAX",
        }
