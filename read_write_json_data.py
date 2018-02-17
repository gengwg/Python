# read/write data encoded as JSON.

import json

data = {
    'name': 'ACME',
    'shares': 100,
    'price': 543.23
}

json_str = json.dumps(data)
print(json_str)

data = json.loads(json_str)
print(data)

# minor changes
print(json.dumps(False))

d = {
    'a': True,
    'b': 'Hello',
    'c': None
}
print(json.dumps(d))

# indent
print(json.dumps(data, indent=4))
# sort keys
print(json.dumps(data, indent=4, sort_keys=True))
