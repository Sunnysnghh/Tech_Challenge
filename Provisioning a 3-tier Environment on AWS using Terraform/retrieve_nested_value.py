#3 Challenge: Retrieve Value from Nested Object by Key

# retrieve_nested_value.py

# Function to retrieve a value from a nested object using a given key
def retrieve_nested_value(obj, key):

# Split the key into individual keys based on '/'
    keys = key.split('/')

# Initializing a temporary object as the input object
    temp_obj = obj

# Iterate through each key in the list of keys
    for k in keys:
        if k in temp_obj:
            temp_obj = temp_obj[k]
        else:
            return None  # Return None if key not found
    return temp_obj

# Examples: 

if __name__ == "__main__":
    # Example Inputs
    obj1 = {"a": {"b": {"c": "d"}}}
    key1 = "a/b/c"

# Retrieve the value for key1 from obj1 and print the result
    print(retrieve_nested_value(obj1, key1))  # Output: d

    obj2 = {"x": {"y": {"z": "a"}}}
    key2 = "x/y/z"

# Retrieve the value for key2 from obj2 and print the result
    print(retrieve_nested_value(obj2, key2))  # Output: a
