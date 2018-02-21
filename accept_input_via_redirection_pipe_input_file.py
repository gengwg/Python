import fileinput

with fileinput.input() as f_input:
    for line in f_input:
        print(f_input.filename(), f_input.lineno(), line, end='')


# $ py3 script.py < /etc/passwd
# $ py3 script.py < /etc/passwd
# $ ls | script.py
