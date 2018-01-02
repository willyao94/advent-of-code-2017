from day18 import Program

def is_num(n):
    try:
        int(n)
    except ValueError:
        return False
    return True

#https://stackoverflow.com/a/17377939
def is_prime(n):
    if n == 2:
        return True
    if not n & 1 or n <= 1:
        return False

    sqr = int(n**0.5) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

input = [x.strip() for x in open('./Inputs/day23.txt').readlines()]
registers = ['a', 'b', 'c', 'd', 'e', 'f', 'h']
prog = Program(0,registers)
mul_counter = 0
while prog.ptr < len(input):
    instr, x, y = input[prog.ptr].split()
    b = int(y) if is_num(y) else prog.regs[y]
    if instr == 'set':
        prog.regs[x] = b
    elif instr == 'sub':
        prog.regs[x] -= b
    elif instr == 'mul':
        prog.regs[x] *= b
        mul_counter += 1
    elif instr == 'jnz':
        a = int(x) if is_num(x) else prog.regs[x]
        if a != 0:
            prog.ptr += b
            continue
    prog.ptr += 1
print("Part 1:", mul_counter)

counter = 0
for i in range(107900, 124901, 17):
    if not is_prime(i):
        counter+=1
print("Part 2:", counter)