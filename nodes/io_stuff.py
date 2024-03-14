from .. import console, PURPLE_NAME, WILDCARD
import subprocess
import shlex
import tempfile

from PIL import Image
import numpy as np

class VIV_Swww_Wallpaper:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                    "wallpaper": ("IMAGE",),
                    "extra_args": ("STRING", {"default": "-t any"}),
                },
            }
    
    RETURN_TYPES = ()
    RETURN_NAMES = ()
    FUNCTION = "set_wallpaper"
    CATEGORY = "vivax/io"
    OUTPUT_NODE = True

    def set_wallpaper(self, wallpaper, extra_args):
        wallpaper = wallpaper[0]
        wallpaper = 255. * wallpaper.cpu().numpy()
        wallpaper = Image.fromarray(np.clip(wallpaper, 0, 255).astype(np.uint8))

        path = tempfile.mktemp(suffix=".png")
        wallpaper.save(path)

        subprocess.run(["swww", "img", path] + shlex.split(extra_args))
        return ()

NODES = {}
if subprocess.run(["which", "swww"]).returncode == 0:
    NODES["Set Wallpaper (Swww)"] = VIV_Swww_Wallpaper
else:
    console.print(f"{PURPLE_NAME} Swww not found, skipping wallpaper node.")
