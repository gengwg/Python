def countdown(n):
    while n > 0:
        print('T-minus', n, 'seconds')
        n -= 1
    print('Liftoff!')

import dis
print(dis.dis(countdown))

c = countdown.__code__.co_code
print("Bytecode:", c)

import opcode

def generate_opcodes(codebytes):
    extended_arg = 0
    i = 0
    n = len(codebytes)
    while i < n:
        op = codebytes[i]
        i += 1
        if op >= opcode.HAVE_ARGUMENT:
            if i +1 >= n:
                break
            oparg = codebytes[i] + codebytes[i + 1] * 256 + extended_arg
            extended_arg = 0
            i += 2
            if op == opcode.EXTENDED_ARG:
                extended_arg = oparg * 65536
                continue
        else:
            oparg = None
        yield (op, oparg)

for op, oparg in generate_opcodes(c):
    print(op, opcode.opname[op], oparg)


print("-------------")
# use Python’s dis module directly to iterate over instructions
# (much safer for different Python versions).

for instr in dis.get_instructions(countdown):
    print(instr.opcode, instr.opname, instr.arg)


def add(x, y):
    return x + y

c = add.__code__
print(c)


## Replace the bytecode with a new one

import types
newbytecode = b'xxxx'  # This is just a placeholder; it should be valid bytecode.
# newbytecode = b'\x64\x00\x53\x00'  # LOAD_CONST 0; RETURN_VALUE (valid minimal bytecode)

nc = types.CodeType(
    c.co_argcount,
    c.co_posonlyargcount,
    c.co_kwonlyargcount,
    c.co_nlocals,
    c.co_stacksize,
    c.co_flags,
    newbytecode,
    c.co_consts,
    c.co_names,
    c.co_varnames,
    c.co_filename,
    c.co_name,
    c.co_qualname,     # new in 3.11
    c.co_firstlineno,
    c.co_linetable,    # replaces co_lnotab
    c.co_exceptiontable,
    c.co_freevars,
    c.co_cellvars
)
print(nc)

add.__code__ = nc
print(add(1, 2))  # This will raise an error since the bytecode is invalid.