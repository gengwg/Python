'''
Problem: 
you have a collection of sorted sequences.
you want to iterator over a sorted sequence of them all merged together.
'''
# heapq.merge() requires all input sequnces already sorted.
# because it simply examines the set of items from front of each input sequence
# and emits the smallest one found. 
import heapq

a = [1, 4, 7, 10]
b = [2, 5, 6, 11]
for c in heapq.merge(a, b):
    print(c)

# merge two sorted files
with open('sorted_file_1', 'rt') as file1, \
     open('sorted_file_2', 'rt') as file2, \
     open('merged_file', 'wt') as outfile:
     
     for line in heapq.merge(file1, file2):
         outfile.write(line)


