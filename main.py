from string_find import find
from string_find_cls import Find

data = ["helloworld", "foo", "bar", "stylight_team", "seo"]
query = "eos"

# Function Usage
result = find(data, query)
print(result)  # ["seo"]

# Class Usage
result = Find(data, query)
print(result)  # ["seo"]
