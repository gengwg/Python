import os

def bad_filename(filename):
    return repr(filename)[1:-1]

files = os.listdir('.')
for name in files:
    try:
        print(name)
    except UnicodeEncodeError:
        print(bad_filename(name))


