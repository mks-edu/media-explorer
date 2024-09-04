import os
import torch
import clip
from PIL import Image
import json
import pickle
import numpy as np
class MyClip:
    def __init__(self):
        # Load the CLIP model and the preprocessing function
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model, self.preprocess = clip.load("ViT-B/32", device=self.device)

        print("Init class MyClip with device=", self.device)

    def load_json_files(self, json_folder):
        metadata = []
        real_json_folder = os.path.realpath(json_folder)
        for file_name in os.listdir(json_folder):
            if file_name.endswith('.json'):
                with open(os.path.join(json_folder, file_name), 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    metadata.append(data)
        return metadata

    def split_text(self, text, max_length=77):
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

    def encode_long_text_with_clip(self, model, text, device, max_length=77):
        chunks = self.split_text(text, max_length)
        chunk_embeddings = []

        for chunk in chunks:
            text_tokens = clip.tokenize([chunk]).to(device)
            with torch.no_grad():
                chunk_embedding = model.encode_text(text_tokens).cpu().numpy()
                chunk_embeddings.append(chunk_embedding)

        # Combine the embeddings, e.g., by averaging
        combined_embedding = sum(chunk_embeddings) / len(chunk_embeddings)
        return combined_embedding

    def create_video_embeddings(self, metadata, model, device):
        video_embeddings = []
        for video in metadata:
            title = video.get('title', '')
            description = video.get('description', '')
            combined_text = f"{title}. {description}"
            # embedding = encode_text_with_clip(model, combined_text, device)
            embedding = self.encode_long_text_with_clip(model, combined_text, device)
            video_embeddings.append((embedding, video))
        return video_embeddings

    def build_video_embeddings_metajson(self, json_folder: str, out_pkl: str):

        metadata = self.load_json_files(json_folder)

        video_embeddings = self.create_video_embeddings(metadata, self.model, self.device)

        # Save the video embeddings to a file
        with open(out_pkl, 'wb') as f:
            pickle.dump(video_embeddings, f)
    ########################
    def search_videos_with_clip(self, query, video_embeddings, model, device):
        query_embedding = self.encode_long_text_with_clip(model, query, device)

        similarities = []
        for embedding, video in video_embeddings:
            similarity = np.dot(query_embedding, embedding.T)
            similarities.append((similarity, video))

        # Sort by similarity
        similarities.sort(key=lambda x: x[0], reverse=True)

        return similarities
    def load(self, pkl_filepath):
        with open(pkl_filepath, 'rb') as f:
            self.video_embeddings = pickle.load(f)

    def search(self, query):
        if self.video_embeddings is None:
            print('video_embeddings is not created. Please check to call function load(pkl_filepath).')
        else:
            results = self.search_videos_with_clip(query, self.video_embeddings, self.model, self.device)

            for similarity, video in results[:5]:  # Display top 5 results
                print(f"Title: {video['title']}")
                print(f"Description: {video['description']}")
                print(f"Similarity: {similarity}")
                print(f"Watch URL: {video['watch_url']}")
                print("\n---\n")
