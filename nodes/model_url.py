from .. import console, PURPLE_NAME
import requests
import os
import folder_paths
from comfy.utils import ProgressBar

class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False

class VIV_Model_From_URL:
    @classmethod
    def INPUT_TYPES(s):
        return {
                "required": {
                    "url": ("STRING", {"default": ""}),
                    "folder": ("STRING", {"default": "loras"}),
                    "force_update": ("BOOLEAN", {"default": False}),
                    },
                "optional": {
                    "filename": ("STRING", {"default": None}),
                    },
                }

    RETURN_TYPES = (AnyType("*"),)
    RETURN_NAMES = ("ckpt_name",)
    FUNCTION = "download"
    CATEGORY = "vivax/url"

    def download(self, url, folder, force_update, filename=None):
        console.print(f"{PURPLE_NAME} [bold yellow]getting filename of: [/bold yellow]", url)


        response = None
        if filename is None or filename == "":
            try:
                response = requests.get(url, stream=True)
                filename = response.headers.get('content-disposition').split("filename=")[1].strip('"')
            except:
                filename = url.split("/")[-1]
        console.print(f"{PURPLE_NAME} [bold yellow]filename: [/bold yellow]", filename)


        if not force_update and folder_paths.get_full_path(folder, filename) is not None:
            console.print(f"{PURPLE_NAME} [bold yellow]file already exsists[/bold yellow]")
            return (filename,)

        if response is None:
            response = requests.get(url, stream=True)
        if response.status_code != 200:
            console.print(f"{PURPLE_NAME} [bold red]failed to get file[/bold red]", response.status_code)
            console.print(response.text);
            raise Exception(f"Failed to get file: {url}")
            return ()

        console.print(f"{PURPLE_NAME} [bold yellow]downloading file[/bold yellow]")

        folder = folder_paths.folder_names_and_paths[folder][0][0]
        full_filename = os.path.join(folder, filename)
        console.print(f"{PURPLE_NAME} [bold yellow]saving to: [/bold yellow]", full_filename)

        total_size = int(response.headers.get('content-length', 0))
        current_size = 0

        pbar = ProgressBar(total_size)
        with open(full_filename, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024*1024):
                file.write(chunk)
                current_size += len(chunk)
                pbar.update(len(chunk))
                console.print(f"{PURPLE_NAME} [bold yellow]downloaded: [/bold yellow]", f"{current_size}/{total_size} ({current_size/total_size*100:.2f}%)", end="\r")
        print()

        return (filename,)
