import torch
import clip
from PIL import Image
import json
import os
#from transformers import pipeline
import pickle

# Load the CLIP model and the preprocessing function
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

def load_json_files(json_folder):
    metadata = []
    for file_name in os.listdir(json_folder):
        if file_name.endswith('.json'):
            with open(os.path.join(json_folder, file_name), 'r', encoding='utf-8') as file:
                data = json.load(file)
                metadata.append(data)
    return metadata

json_folder = 'G:\Projects\AIC-2024\Data_2024\Metadata\media-info-b1\media-info'
metadata = load_json_files(json_folder)

# def encode_text_with_clip(model, text, device):
#     text_tokens = clip.tokenize([text]).to(device)
#     with torch.no_grad():
#         text_features = model.encode_text(text_tokens).cpu().numpy()
#     return text_features

# def encode_long_text_with_clip(model, text, device, max_length=77):
#     words = text.split()
#     chunks = [' '.join(words[i:i+max_length]) for i in range(0, len(words), max_length)]
#     chunk_embeddings = []
#
#     for chunk in chunks:
#         text_tokens = clip.tokenize([chunk]).to(device)
#         with torch.no_grad():
#             chunk_embedding = model.encode_text(text_tokens).cpu().numpy()
#             chunk_embeddings.append(chunk_embedding)
#
#     # Combine the embeddings, e.g., by averaging
#     combined_embedding = sum(chunk_embeddings) / len(chunk_embeddings)
#     return combined_embedding


# def split_text_into_chunks(text, max_length=77):
#     tokens = clip.tokenize([text])[0]  # Tokenize the text
#     chunks = []
#     start_idx = 0
#
#     while start_idx < len(tokens):
#         end_idx = min(start_idx + max_length, len(tokens))
#         chunk_tokens = tokens[start_idx:end_idx]
#
#         # Decode tokens back into a string for CLIP
#         chunk_text = clip.tokenizer.decode(chunk_tokens.cpu().numpy())
#         chunks.append(chunk_text.strip())
#
#         start_idx = end_idx
#
#     return chunks
# def encode_long_text_with_clip(model, text, device, max_length=77):
#     chunks = split_text_into_chunks(text, max_length=max_length)
#     chunk_embeddings = []
#
#     for chunk in chunks:
#         text_tokens = clip.tokenize([chunk]).to(device)
#         with torch.no_grad():
#             chunk_embedding = model.encode_text(text_tokens).cpu().numpy()
#             chunk_embeddings.append(chunk_embedding)
#
#     # Combine the embeddings, e.g., by averaging
#     combined_embedding = sum(chunk_embeddings) / len(chunk_embeddings)
#     return combined_embedding
def split_text(text, max_length=77):
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        current_chunk.append(word)
        # Check the token length if we add the next word
        if len(clip.tokenize([' '.join(current_chunk)]).squeeze()) > max_length - 1:
            # If too long, pop the last word and save the chunk
            current_chunk.pop()
            chunks.append(' '.join(current_chunk))
            current_chunk = [word]  # Start a new chunk with the current word

    # Don't forget to add the last chunk
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks

def encode_long_text_with_clip(model, text, device, max_length=77):
    chunks = split_text(text, max_length)
    chunk_embeddings = []

    for chunk in chunks:
        text_tokens = clip.tokenize([chunk]).to(device)
        with torch.no_grad():
            chunk_embedding = model.encode_text(text_tokens).cpu().numpy()
            chunk_embeddings.append(chunk_embedding)

    # Combine the embeddings, e.g., by averaging
    combined_embedding = sum(chunk_embeddings) / len(chunk_embeddings)
    return combined_embedding





def create_video_embeddings(metadata, model, device):
    video_embeddings = []
    for video in metadata:
        title = video.get('title', '')
        description = video.get('description', '')
        combined_text = f"{title}. {description}"
        # embedding = encode_text_with_clip(model, combined_text, device)
        embedding = encode_long_text_with_clip(model, combined_text, device)
        video_embeddings.append((embedding, video))
    return video_embeddings

video_embeddings = create_video_embeddings(metadata, model, device)

# Save the video embeddings to a file
with open('video_embeddings.pkl', 'wb') as f:
    pickle.dump(video_embeddings, f)