def sample():
    yield 'Is'
    yield 'SF'
    yield 'Not'
    yield 'SF?'

print ' '.join(sample())

for part in sample():
    print part
