# test if lst1 is a sub list of lst2
def sublist(lst1, lst2):
    sub_set = False
    for i in range(len(lst2)):
        if lst2[i] == lst1[0]:
            n = 1
            while n < len(lst1) and lst1[i+n] == lst1[n]:
                n += 1
            if n == len(lst1):
                sub_set = True
    return sub_set

print sublist([1,2], [1, 2,5,3])

