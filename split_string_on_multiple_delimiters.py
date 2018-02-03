"""
split a string into fileds.
delimiters and spaces arounds them not consistent throughout the string.
"""

import re
line = 'adf jsdf; adf, sdfd,dfse,      foo'

# separator is either a comma, semicolon, or whitespace
# followed by any amount of extra whitespace.
print re.split(r'[;,\s]\s*', line)
# ['adf', 'jsdf', 'adf', 'sdfd', 'dfse', 'foo']

print re.split(r'[;,]\s*', line)
# ['adf jsdf', 'adf', 'sdfd', 'dfse', 'foo']

# capture groups enclosed in parenthesis
# ==> matched text is also in the result.
print re.split(r'(;|,|\s)\s*', line)
# ['adf', ' ', 'jsdf', ';', 'adf', ',', 'sdfd', ',', 'dfse', ',', 'foo']

# use noncapture group (?:...) to get same as brackets result
print re.split(r'(?:;|,|\s)\s*', line)
# ['adf', 'jsdf', 'adf', 'sdfd', 'dfse', 'foo']

