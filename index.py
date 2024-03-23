from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import os

# Initialize Elasticsearch client
client = Elasticsearch(
    "https://c87a178966b84e85ad1853d2ca9896e4.us-central1.gcp.cloud.es.io",
    api_key="YTNhRmE0NEJkUE9ic3NxbElDZEc6LVhhZGdKT2NUSlc1RVVsX0gwTnpTZw=="
)

# Define the index name
index_name = "search-xophom"

# Specify the path to the text file
txt_path = "hereshegoes.txt"

# Function to index a document
def index_document(client, index_name, document_id, document):
    return {
        "_index": index_name,
        "_id": document_id,
        "_source": document
    }

# Read the content of the text file
with open(txt_path, 'rb') as file:
    txt_content = file.read()

# Prepare metadata for indexing
document_metadata = {
    "name": os.path.basename(txt_path),
    "content_type": "text/plain",
    "custom_data": txt_content  # Store binary content directly
}

# Index the document
bulk_operations = [index_document(client, index_name, os.path.basename(txt_path), document_metadata)]
bulk(client, bulk_operations, pipeline="ent-search-generic-ingestion")

# Perform a search to find documents containing specific text
search_text = "21 year old boy with beard"
response = client.search(index=index_name, q=search_text)

# Print search results
print("Search Results:")
for hit in response["hits"]["hits"]:
    print(hit["_source"])

# Print total hits
print(f"Total Hits: {response['hits']['total']['value']}")
