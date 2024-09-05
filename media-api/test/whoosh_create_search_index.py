import os
import json
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, NUMERIC, ID, DATETIME
from datetime import datetime

# Define the schema for the index
schema = Schema(
    author=TEXT(stored=True),
    channel_id=TEXT(stored=True),
    channel_url=TEXT(stored=True),
    description=TEXT(stored=True),
    keywords=TEXT(stored=True),
    length=NUMERIC(stored=True),
    publish_date=TEXT(stored=True),
    thumbnail_url=TEXT(stored=True),
    title=TEXT(stored=True),
    watch_url=TEXT(stored=True),
    upload_date=DATETIME(stored=True),
    #file_path=ID(stored=True, unique=True)
)

# Create an index directory
whoosh_index_dir = 'out/whoosh_index'
if not os.path.exists(whoosh_index_dir):
    os.mkdir(whoosh_index_dir)

# Create or open the index
ix = create_in(whoosh_index_dir, schema)

# Open the writer to add documents
# writer = ix.writer()

# Path to the folder containing JSON files
folder_path = "data/aic-2024/media-info"
# Open the writer to add documents
with ix.writer() as writer:
    # Process each JSON file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

                # Parse upload_date to datetime if necessary
                upload_date = datetime.strptime(data.get('publish_date', '1970-01-01'), '%d/%m/%Y')

                try:
                    # Add document to the index
                    writer.add_document(
                        author=data.get('author', ''),
                        channel_id=data.get('channel_id', ''),
                        channel_url=data.get('channel_url', ''),
                        description=data.get('description', ''),
                        keywords=' '.join(data.get('keywords', [])),
                        length=data.get('length', ''),
                        publish_date=data.get('publish_date', ''),
                        thumbnail_url=data.get('thumbnail_url', ''),
                        title=data.get('title', ''),
                        watch_url=data.get('watch_url', ''),
                        upload_date=upload_date
                    )
                except ValueError:
                    print('Could not add_document')

# Commit the changes
# writer.commit()
