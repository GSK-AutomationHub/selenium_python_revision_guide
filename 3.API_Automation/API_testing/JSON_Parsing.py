''' JSON Parsing
In Python, we use requests library to make HTTP request & we get the response body in JSON format.
we parse it into a native Python dictionary or list using .json() or using json.load() from json module.
Parsed JSON becomes regular Python data structures  so you can easily validate keys, values, lists, etc.
'''
import request

# Make an API request
response = requests.get("https://jsonplaceholder.typicode.com/users/1")

# Check if request succeeded
if response.status_code == 200:
    # Parse JSON response to Python dict
    print(response)
    # print(response.text)
    # print(response.content)
    data = response.json()
    print(data)  # whole JSON
    print(f"User name: {data['name']}")
    print(f"Email: {data['email']}")
else:
    print(f"Request failed with status code {response.status_code}")

print("-------------------------------------------------------------------------")

import json

# Example raw JSON string
json_string = '{"name": "John Doe", "email": "john@example.com"}'
print(type(json_string))

# Parse JSON string to dict
data = json.loads(json_string)
print(type(data))
print(data['name'])  # John Doe

print("-------------------------------------------------------------------------")