## Counting the occurrences of letters in a string:

from collections import Counter

s = 'hello world'
letter_counts = Counter(s)
print(letter_counts)
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

## Counting the occurrences of words in a list:

from collections import Counter

lst = ['apple', 'banana', 'cherry', 'apple', 'banana', 'apple', 'apple']
word_counts = Counter(lst)

print(word_counts)
# Output: Counter({'apple': 4, 'banana': 2, 'cherry': 1})

## Counting the occurrences of elements in a tuple:

from collections import Counter

t = (1, 2, 3, 2, 1, 1, 2, 3, 1, 1)
element_counts = Counter(t)

print(element_counts)
# Output: Counter({1: 5, 2: 3, 3: 2})

## Counting the occurrences of characters in a file:

from collections import Counter

with open('file.txt', 'r') as f:
    char_counts = Counter(f.read())

print(char_counts)

## Counting the occurrences of words in a file:

from collections import Counter

word_list = []
with open('file.txt', 'r') as f:
    for line in f:
        for word in line.split():
            word_list.append(word.lower())
    word_counts = Counter(word_list)

print(word_counts)

