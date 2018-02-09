import random
values = [1,2,3,4,5,6]

for _ in range(0,10):
    print random.choice(values)

for _ in range(0,10):
    print random.sample(values, 2)

for _ in range(0,10):
    print random.sample(values, 3)

for _ in range(0,3):
    random.shuffle(values)
    print values

# random integers
for _ in range(0,10):
    print random.randint(0, 10)

# uniform floating-point values in range 0 to 1
for _ in range(0,10):
    print random.random()

# N random bits expressed as integer
r = random.getrandbits(200)
print r
print format(r, 'b')

