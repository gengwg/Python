"""
search for and replace a text pattern in a string.
"""

# for simple literal patterns, use str.replace() method.
text = 'yeah, but no, but yeah, but no, but yeah'
print text.replace('yeah', 'yep')

# for more complicated patterns, use the sub() method in the re module.
text = 'Today is 11/27/2012, meeting starts 3/2/2013'
import re
# first argument to sub() is the pattern to match
# second arg is the replacement pattern
# backslached digits \3 refer to capture group numbers in the pattern.
print re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)

# for repeated substitution of the same pattern, compile it first.
pat = re.compile(r'(\d+)/(\d+)/(\d+)')
print pat.sub(r'\3-\1-\2', text)

# for more complicated substitutions, use a substitution call back function.
from calendar import month_abbr

def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

print pat.sub(change_date, text)

# if want to know how many sub were made, use re.subn()
newtext, n = pat.subn(r'\3-\1-\2', text)
print newtext
print n
