#2 Challenge: Query Instance Metadata and Output JSON

# query_instance_metadata.py

import requests
import json

# Function to query instance metadata from AWS
def query_instance_metadata(data_key=None):

# URL for accessing instance metadata in AWS
    metadata_url = 'http://169.254.169.254/latest/meta-data/'

# Send HTTP GET request to retrieve metadata
    response = requests.get(metadata_url)

# Split metadata into separate items
    metadata = response.text.split('\n')

# Initializing an empty dictionary to store metadata
    metadata_dict = {}

# Iterate through each metadata item
    for item in metadata:
        if data_key:
            if item == data_key:
                return {data_key: requests.get(metadata_url + item).text}
        else:
            metadata_dict[item] = requests.get(metadata_url + item).text

# If a specific data key is provided but not found in the metadata
    if data_key:
        return {}  # Return empty dictionary if specified data key not found
    else:

# If no specific data key is provided, return the dictionary containing all metadata
        return metadata_dict

# Example usage
if __name__ == "__main__":
    # Query all metadata
    instance_metadata = query_instance_metadata()

# Print all metadata in JSON format with proper indentation
    print(json.dumps(instance_metadata, indent=4))

    # Query specific metadata key
    data_key = "instance-id"
    specific_metadata = query_instance_metadata(data_key)

# Print metadata for the specified key in JSON format with proper indentation
    print(json.dumps(specific_metadata, indent=4))
