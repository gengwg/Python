"""
these conversions only pertain to the conversion of integer to and from a textual
representation. under the cover there is only one integer type.
"""

x = 1234

print(bin(x))
print(oct(x))
print(hex(x))

print(format(x, 'b'))
print(format(x, 'o'))
print(format(x, 'x'))

x = -1234
print(format(x, 'b'))
print(format(x, 'o'))
print(format(x, 'x'))

# unsigned value add in the max value to set the bit length
print(format(2**32 + x, 'b'))
print(format(2**32 + x, 'x'))

# convert integer strings in diff bases
print(int('4d2', 16))
print(int('10011010010', 2))

# using octal numbers
import os
os.chmod('file.sh', 0o0755)
