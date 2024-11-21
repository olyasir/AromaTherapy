from transformers import AutoTokenizer, CLIPTextModelWithProjection
from properties import PROPERTY
import torch

model = CLIPTextModelWithProjection.from_pretrained("openai/clip-vit-base-patch32")
tokenizer = AutoTokenizer.from_pretrained("openai/clip-vit-base-patch32")

inputs = [e.value for e in PROPERTY]
inputs = tokenizer( inputs, padding=True, return_tensors="pt")

outputs = model(**inputs)
text_embeds = outputs.text_embeds

torch.cdist( text_embeds, text_embeds )
print("")