# Convert List to Dictionary: Even items as keys, odd items as values

# Example:
# inv = ['apples', 2, 'oranges', 3, 'limes', 10, 'bananas', 7, 'grapes', 4]
# I want to create a dictionary from this list,
# where the items in the even positions (apples, oranges, limes, bananas, grapes) are the keys,
# and the items in the odd positions (2, 3, 10, 7, 4) are the values.
# inv_dict = {'apples':2, 'oranges':3, 'limes':10, 'bananas':7, 'grapes':4}
# https://stackoverflow.com/questions/38194403/list-to-dictionary-even-items-as-keys-odd-items-as-values

with open('input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]
#print(content)
content_dict = dict(zip(content[::2], content[1::2]))
print(content_dict)

for k, v in content_dict.items():
    print('{}, {}'.format(k, v))
