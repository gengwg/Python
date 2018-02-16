from tempfile import TemporaryFile

with TemporaryFile('w+t') as f:
    # r/w to file
    f.write('Hello World\n')
    f.write('Testing\n')

    # seek back to beginning and read the data
    f.seek(0)
    data = f.read()
    print(data)

from tempfile import TemporaryDirectory

with TemporaryDirectory() as dirname:
    print('dirname is:', dirname)

import tempfile
print(tempfile.gettempdir())

