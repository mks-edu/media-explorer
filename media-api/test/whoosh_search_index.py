from whoosh.qparser import MultifieldParser, OrGroup
from whoosh.fields import Schema, TEXT, NUMERIC, ID, DATETIME
from whoosh.qparser import QueryParser
from whoosh import index
from datetime import datetime
from whoosh.qparser import QueryParser

def search_simple():
    # Query the index
    with ix.searcher() as searcher:
        query = QueryParser("description", ix.schema).parse("60 giay hom nay")
        results = searcher.search(query)

        print_result(results)


def search_by_fields(query_string, search_fields = ["title", "description", "keywords", "publish_date"]):
    '''
    @param query_string: User query term (you can replace this with dynamic input)
    '''
    # List of all the fields you want to search in
    # search_fields = ["title", "description", "keywords", "publish_date"]

    # Perform the search with OR across all fields
    with ix.searcher() as searcher:
        # Create a multifield parser with OR group
        parser = MultifieldParser(search_fields, ix.schema, group=OrGroup)

        # Parse the query
        query = parser.parse(query_string)

        # Execute the search
        results = searcher.search(query)
        print_result(results)
def print_result(results):
    # Print out the search results
    i = 1
    for result in results:
        print(f"Result : {i}")
        print(f"Title: {result['title']}")
        print(f"Description: {result['description']}")
        print(f"Upload Date: {result['upload_date']}")
        print(f"watch_url: {result['watch_url']}")
        print("-" * 40)
        i += 1

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

# Open the index
ix = index.open_dir(whoosh_index_dir)

# Try to search
search_by_fields("60 Giây Chiều - Ngày 11/10/2023", )

