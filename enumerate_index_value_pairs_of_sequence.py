my_list = ['a', 'b', 'c']

for idx, val in enumerate(my_list):
    print(idx, val)

for idx, val in enumerate(my_list, 1):
    print(idx, val)


def parse_data(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
            try:
                count = int(fields[1])
                # ... process data
            except ValueError as e:
                print('Line {}: Parse error: {}'.format(lineno, e))


# map words in a file to the lines in which they occur
from collections import defaultdict

word_summary = defaultdict(list)

with open('myfile.txt', 'r') as f:
    lines = f.readlines()

for idx, line in enumerate(lines, 1):
    # create a list of words in current line
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)

for k, v in word_summary.items():
    print '{}: {}'.format(k, v)


