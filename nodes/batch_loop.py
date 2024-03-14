from .. import console, WILDCARD, PURPLE_NAME
import random
from torch import Tensor
import torch

class VIV_Chunk_Up:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "batch": (WILDCARD,),
                "chunk_size": ("INT", {"default": 16}),
                },
            }

    RETURN_TYPES = ("INT", WILDCARD,)
    RETURN_NAMES = ("amount_chunks","chunks",)
    FUNCTION = "create_chunk"
    CATEGORY = "vivax/chunks"

    def create_chunk(self, batch, chunk_size):
        latent = False
        if isinstance(batch, dict) and "samples" in batch:
            batch = batch["samples"]
            latent = True

        chunks = []
        for i in range(0, len(batch), chunk_size):
            chunk = batch[i:i + chunk_size]
            if latent:
                chunk = {"samples": chunk}
            chunks.append(chunk)
        amount_chunks = len(chunks)
        return (amount_chunks, chunks,)

class VIV_Get_Chunk:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "chunks": (WILDCARD,),
                "index": ("INT", {"default": 0}),
                "one_index": ("BOOLEAN", {"default": True}),
                },
            "optional": {
                "seed": ("INT", {"default": 0}),
                },
            }

    RETURN_TYPES = (WILDCARD,"INT")
    RETURN_NAMES = ("chunk","seed")
    FUNCTION = "get_chunk"
    CATEGORY = "vivax/chunks"

    def get_chunk(self, chunks, index, one_index, seed=None):
        if seed is None:
            seed = random.randint(0, 1000000)

        return (chunks[index - one_index], seed + index,)

class VIV_Join_Chunks:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "chunk": (WILDCARD,),
                "batch": (WILDCARD,),
                },
            }

    RETURN_TYPES = (WILDCARD,)
    RETURN_NAMES = ("batch",)
    FUNCTION = "combine_chunks"
    CATEGORY = "vivax/chunks"

    def combine_chunks(self, chunk, batch=None):
        latent = False
        tensor = False
        if isinstance(chunk, dict) and "samples" in chunk:
            chunk = chunk["samples"]
            latent = True
        elif isinstance(chunk, Tensor):
            tensor = True

        if batch is None:
            batch = [] if not tensor else Tensor()
        elif latent:
            batch = batch["samples"]

        if tensor:
            batch = torch.cat((batch, chunk), dim=0)
        else:
            batch.extend(chunk)

        if latent:
            return ({"samples": batch},)
        return (batch,)
