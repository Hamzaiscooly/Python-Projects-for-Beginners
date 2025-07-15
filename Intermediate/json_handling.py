# JSON Handling

import json

data = {"name": "Bob", "age": 30}
json_string = json.dumps(data)
print(json_string)

# Convert back to Python dict
parsed = json.loads(json_string)
print(parsed["name"])