# -*- coding: utf-8 -*-
"""
To loop over two or more sequences at the same time, the entries can be
paired with the zip() function.

Output:
[{'name': 'Gus’s World Famous Fried Chicken',
  'numrevs': 549,
  'price': '$$',
  'stars': '4.0'},
{'name': 'South City Kitchen - Midtown',
  'numrevs': 1777,
  'price': '$$',
  'stars': '4.5'},
{'name': 'Mary Mac’s Tea Room',
  'numrevs': 2241,
  'price': '$$',
  'stars': '4.0'},
{'name': 'Busy Bee Cafe', 'numrevs': 481, 'price': '$$', 'stars': '4.0'},
{'name': 'Richards’ Southern Fried',
  'numrevs': 108,
  'price': '$$',
  'stars': '4.0'},
{'name': 'Greens & Gravy', 'numrevs': 93, 'price': '$$', 'stars': '3.5'
},
{'name': 'Colonnade Restaurant',
  'numrevs': 350,
  'price': '$$',
  'stars': '4.0'},
{'name': 'South City Kitchen Buckhead',
  'numrevs': 248,
  'price': '$$',
  'stars': '4.5'},
{'name': 'Poor Calvin’s', 'numrevs': 1558, 'price': '$$', 'stars': '4.5'},
{'name': 'Rock’s Chicken & Fries',
  'numrevs': 67,
  'price': '$',
  'stars': '4.0'}]
"""
d = {'name': ['Gus’s World Famous Fried Chicken',
  'South City Kitchen - Midtown',
  'Mary Mac’s Tea Room',
  'Busy Bee Cafe',
  'Richards’ Southern Fried',
  'Greens & Gravy',
  'Colonnade Restaurant',
  'South City Kitchen Buckhead',
  'Poor Calvin’s',
  'Rock’s Chicken & Fries'],
'numrevs': [549, 1777, 2241, 481, 108, 93, 350, 248, 1558, 67],
'price': ['$$', '$$', '$$', '$$', '$$', '$$', '$$', '$$', '$$', '$'],
'stars': ['4.0',
  '4.5',
  '4.0',
  '4.0',
  '4.0',
  '3.5',
  '4.0',
  '4.5',
  '4.5',
  '4.0']}
data = d

print ([{'name':x, 'numrevs':y, 'price': z, 'starts': w}
for (x,y,z,w) in zip(d['name'], d['numrevs'], d['price'], d['stars'])])

# print zip(*data.values())
# print [zip(data.keys(), x) for x in zip(*data.values())]
print([dict(zip(data.keys(), d)) for d in zip(*data.values())])

import pandas
print (pandas.DataFrame(data).to_json(orient='records'))
# print pandas.DataFrame(data).to_json()
