import string

def toStr(n, base):
    convertString = string.digits + string.letters
    if n < base:
        return convertString[n]
    else:
        # If we reversed returning the convertString lookup and returning the toStr call,
        # the resulting string would be backward!
        # But by delaying the concatenation operation until after the recursive call has returned,
        # we get the result in the proper order.
        # This should remind you of our discussion of stacks back in the previous chapter.

        # return convertString[n % base] + toStr(n // base, base)
        return toStr(n // base, base) + convertString[n % base]

if __name__ == '__main__':
    print(toStr(1453, 62))
