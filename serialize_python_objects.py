# serialize python object into a byte stream

import pickle

data = [1, 2, 3, 4]
with open('somefile', 'wb') as f:
    pickle.dump(data, f)

s = pickle.dumps(data)
print(s)

# restor from file
with open('somefile', 'rb') as f:
    data = pickle.load(f)
    print(data)

# restore from string
data = pickle.loads(s)
print(data)
