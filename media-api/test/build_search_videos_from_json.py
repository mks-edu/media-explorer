import json
import os
from collections import defaultdict

def load_json_files(json_folder):
    metadata = []
    for file_name in os.listdir(json_folder):
        if file_name.endswith('.json'):
            with open(os.path.join(json_folder, file_name), 'r', encoding='utf-8') as file:
                data = json.load(file, )
                metadata.append(data)
    return metadata

def build_index(metadata):
    index = defaultdict(list)
    for video in metadata:
        # Use keywords, title, and description for indexing
        keywords = video.get('keywords', [])
        title = video.get('title', '').lower()
        description = video.get('description', '').lower()
        for word in keywords:
            index[word.lower()].append(video)
        index[title].append(video)
        index[description].append(video)
    return index


def search_videos(query, index):
    query = query.lower()
    results = index.get(query, [])
    return results


def display_search_results(results, video_folder):
    for video in results:
        title = video.get('title', 'No Title')
        watch_url = video.get('watch_url', 'No URL')
        video_file = os.path.join(video_folder, f"{title}.mp4")

        print(f"Title: {title}")
        print(f"Watch URL: {watch_url}")
        if os.path.exists(video_file):
            print(f"Video File: {video_file}")
        else:
            print("Video File: Not Found")
        print("\n---\n")


def main():
    json_folder = r'G:\Projects\AIC-2024\Data_2024\Metadata\media-info-b1\media-info'  # Replace with your folder path
    video_folder = r'G:\Projects\AIC-2024\Data_2024\Video'  # Replace with your folder path

    # Load metadata from JSON files
    metadata = load_json_files(json_folder)

    # Build the search index
    index = build_index(metadata)

    # Search query
    search_query = input("Enter search query: ")

    # Search for videos
    results = search_videos(search_query, index)

    # Display results
    if results:
        display_search_results(results, video_folder)
    else:
        print("No results found.")


if __name__ == "__main__":
    main()
