#/usr/bin/env python

x = 1234.56789

# two decimal places of accuracy
# round according to round()
print format(x, '0.2f')

# right justified in 10 chars, one digit accuracy
print format(x, '>10.1f')

# left justified
print format(x, '<10.1f')

# centered
print format(x, '^10.1f')

# inclusion of thousand separator
print format(x, ',')
print format(x, '0,.1f')

# exponential notation
print format(x, 'e')
print format(x, '0.2e')

# general form: '[<>^]?width[,]?(.digits)?'

# same format codes used in .format() method of strings
print 'The value is {:0,.2f}'.format(x)
