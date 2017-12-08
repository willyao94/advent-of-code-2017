input = [x.strip() for x in open('./Inputs/day8.txt').readlines()]
registers = {}
max_val = -1
for line in input:
    # Each line has the format of [rA instr val 'if' rB op q]
    rA, instr, val, x, rB, op, q = line.split()

    if not rA in registers:
        registers[rA] = 0
    if not rB in registers:
        registers[rB] = 0

    instr = '+=' if instr == 'inc' else '-='
    if eval("registers[rB] " + op + q):
        exec("registers[rA] " + instr + val)
        max_val = max(max_val, registers[rA])

print(max(registers.values()))
print(max_val)