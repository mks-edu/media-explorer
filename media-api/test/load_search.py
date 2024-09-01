import torch
import clip
import numpy as np

import pickle

def encode_text_with_clip(model, text, device):
    text_tokens = clip.tokenize([text]).to(device)
    with torch.no_grad():
        text_features = model.encode_text(text_tokens).cpu().numpy()
    return text_features
def search_videos_with_clip(query, video_embeddings, model, device):
    query_embedding = encode_text_with_clip(model, query, device)

    similarities = []
    for embedding, video in video_embeddings:
        similarity = np.dot(query_embedding, embedding.T)
        similarities.append((similarity, video))

    # Sort by similarity
    similarities.sort(key=lambda x: x[0], reverse=True)

    return similarities

with open('video_embeddings.pkl', 'rb') as f:
    video_embeddings = pickle.load(f)

device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

query = "60 Giây Chiều - Ngày 29/03/2024"
results = search_videos_with_clip(query, video_embeddings, model, device)

for similarity, video in results[:5]:  # Display top 5 results
    print(f"Title: {video['title']}")
    print(f"Description: {video['description']}")
    print(f"Similarity: {similarity}")
    print(f"Watch URL: {video['watch_url']}")
    print("\n---\n")
