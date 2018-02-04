text = 'Hello World'

print
print 'string methods'.center(20, '=')

print text.ljust(20)
print text.rjust(20)
print text.center(20)

print text.rjust(20, '=')
print text.center(20, '*')

print
print 'format() func'.center(20, '=')

print format(text, '<20')
print format(text, '>20')
print format(text, '^20')

print format(text, '=>20s')
print format(text, '*^20s')

print
print 'multiple values'.center(20, '=')

print '{:>10s} {:>10s}'.format('Hello', 'World')

print
print 'formate numbers'.center(20, '=')

x = 1.2345
print format(x, '>20')
print format(x, '^20.2f')
