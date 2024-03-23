# from elasticsearch import Elasticsearch

# client = Elasticsearch(
#   "https://c87a178966b84e85ad1853d2ca9896e4.us-central1.gcp.cloud.es.io",
#   api_key="YTNhRmE0NEJkUE9ic3NxbElDZEc6LVhhZGdKT2NUSlc1RVVsX0gwTnpTZw=="
# )
# client.info()
# print("Successfully connected to clinet")
documents = [
  { "index": { "_index": "search-xophom", "_id": "9780553351927"}},
  {"name": "Sumeet", "author": "Sumeet", "release_date": "1992-06-01", "page_count": 123, "_extract_binary_content": True, "_reduce_whitespace": True, "_run_ml_inference": True},
  { "index": { "_index": "search-xophom", "_id": "9780441017225"}},
  {"name": "Sujal", "author": "Sujal", "release_date": "2000-03-15", "page_count": 222, "_extract_binary_content": True, "_reduce_whitespace": True, "_run_ml_inference": True},
  { "index": { "_index": "search-xophom", "_id": "9780451524935"}},
  {"name": "Soham", "author": "Soham", "release_date": "1985-06-01", "page_count": 328, "_extract_binary_content": True, "_reduce_whitespace": True, "_run_ml_inference": True},
  { "index": { "_index": "search-xophom", "_id": "9781451673319"}},
  {"name": "Raghvendra", "author": "Raghvendra", "release_date": "1953-10-15", "page_count": 227, "_extract_binary_content": True, "_reduce_whitespace": True, "_run_ml_inference": True},
  { "index": { "_index": "search-xophom", "_id": "9780060850524"}},
  {"name": "Kunal", "author": "Kunal", "release_date": "1932-06-01", "page_count": 268, "_extract_binary_content": True, "_reduce_whitespace": True, "_run_ml_inference": True},
  
]


# client.search(index="search-xophom", q="snow")

from elasticsearch import Elasticsearch

client = Elasticsearch(
    "https://c87a178966b84e85ad1853d2ca9896e4.us-central1.gcp.cloud.es.io",
    api_key="YTNhRmE0NEJkUE9ic3NxbElDZEc6LVhhZGdKT2NUSlc1RVVsX0gwTnpTZw=="
)

client.bulk(operations=documents, pipeline="ent-search-generic-ingestion")

# Perform the search operation
response = client.search(index="search-xophom", q="Sumeet")

# Print the search results
print("Search Results:")
for hit in response["hits"]["hits"]:
    print(hit["_source"])

# Print total hits
print(f"Total Hits: {response['hits']['total']['value']}")
