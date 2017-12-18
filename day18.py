from collections import deque


class Program:
    def __init__(self, id, registers):
        self.ptr = 0
        self.queue = deque()
        self.locked = False
        self.regs = dict()
        self.send_count = 0
        for r in registers:
            self.regs[r] = 0
        self.regs['p'] = id


def is_num(n):
    try:
        int(n)
    except ValueError:
        return False
    return True


def process_instr(line, n, prog, other_prog):
    if not (0 <= prog.ptr < n):
        prog.locked = True
        return
    instr, a = line[0], line[1]
    if instr == 'snd':
        other_prog.queue.append(prog.regs[a])
        prog.send_count += 1
    elif instr == 'rcv':
        if len(prog.queue) > 0:
            prog.locked = False
            prog.regs[a] = prog.queue.popleft()
        else:            
            prog.locked = True
            return
    else: 
        b = int(line[2]) if is_num(line[2]) else prog.regs[line[2]]
        if instr == 'set':
            prog.regs[a] = b
        elif instr == 'add':
            prog.regs[a] += b
        elif instr == 'mul':
            prog.regs[a] *= b
        elif instr == 'mod':
            prog.regs[a] %= b
        elif instr == 'jgz':
            a = int(a) if is_num(a) else prog.regs[a]
            if a > 0:
                prog.ptr += b
                return
    prog.ptr += 1


if __name__ == "__main__":
    input = [x.strip().split() for x in open('./Inputs/day18.txt').readlines()]
    registers = ['a', 'b', 'f', 'i', 'p']
    prog0 = Program(0,registers)
    prog1 = Program(1,registers)

    while not prog0.locked or not prog1.locked:
        process_instr(input[prog0.ptr], len(input), prog0, prog1)
        process_instr(input[prog1.ptr], len(input), prog1, prog0)
    print(prog1.send_count)