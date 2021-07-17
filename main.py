from string_find import find
from string_find_cls import Find, StringFind

data = ["helloworld", "foo", "bar", "stylight_team", "seo"]
query = "eos"

# Function Usage
result = find(data, query)
print(result)  # ["seo"]

# Class Usage
result = Find(data, query)
print(result)  # ["seo"]

# Class Different Usage
result = StringFind(data, query).find()
print(result)  # ["seo"]
