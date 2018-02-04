"""
match or search text for a specific pattern.
"""

import re

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'


pat = re.compile(r'\d+/\d+/\d+')

if pat.match(text1):
    print 'yes'
else:
    print 'no'

if pat.match(text2):
    print 'yes'
else:
    print 'no'

# find all matches
text = 'Today is 11/27/2012, meeting starts 3/2/2013'
print pat.findall(text) # ['11/27/2012', '3/2/2013']

pat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = pat.match(text1)
print m

print m.group(0)
print m.group(1)
print m.group(2)
print m.group(3)
print m.groups()

# find all matches
print pat.findall(text) # [('11', '27', '2012'), ('3', '2', '2013')]

for month, day, year in pat.findall(text):
    print '{}-{}-{}'.format(year, month, day)

# find matches iteratively
for m in pat.finditer(text):
    # print m.groups()
    month, day, year = m.groups()
    print '{}-{}-{}'.format(year, month, day)
