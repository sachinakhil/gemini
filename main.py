import os
import json
from serpapi import GoogleSearch


# Set up search parameters
params = {
    "q": "iPhone with 256 GB",
    "location": "India",
    "hl": "en",
    "gl": "in",
    "api_key": os.getenv('SERPAPI_API_KEY')  # Replace with actual SerpAPI key from .env
}

# Perform the search
search = GoogleSearch(params)
results = search.get_dict()

# Extract shopping results
shopping_results = results.get("shopping_results", [])

# Define the JSON file name
json_file = "/Users/akhilsachin/laptop-recommendation-system/shopping_results.json"

# Write shopping results to a JSON file
with open(json_file, 'w') as file:
    json.dump(shopping_results, file, indent=4)

print(f"Shopping results have been written to {json_file}")
