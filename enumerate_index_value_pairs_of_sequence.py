my_list = ['a', 'b', 'c']

for idx, val in enumerate(my_list):
    print(idx, val)

for idx, val in enumerate(my_list, 1):
    print(idx, val)


def parse_data(filename):
    with open(filename) as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
            try:
                count = int(fields[1])
                # ... process data
            except ValueError as e:
                print(f'Line {lineno}: Parse error: {e}')


# map words in a file to the lines in which they occur
from collections import defaultdict

word_summary = defaultdict(list)

with open('myfile.txt') as f:
    lines = f.readlines()

for idx, line in enumerate(lines, 1):
    # create a list of words in current line
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)

for k, v in word_summary.items():
    print(f'{k}: {v}')


