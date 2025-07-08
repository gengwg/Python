import re

NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([
    NAME, NUM, PLUS, TIMES, EQ, WS
]))


from collections import namedtuple

Token = namedtuple('Token', ['type', 'value'])

def generate_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        if m.lastgroup == 'WS':
            continue
        # yield Token(m.lastgroup, m.group(m.lastgroup))

for tok in generate_tokens(master_pat, 'foo = 23 + 42 * bar'):
    print(tok)