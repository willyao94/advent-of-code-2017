from collections import defaultdict

finish = 12399302
tape = defaultdict(int)
ptr = 0
curr_state = 'A'
for _ in xrange(finish):
    curr_val = tape[ptr]
    # State A
    if curr_state == 'A':
        if curr_val == 0:
            tape[ptr] = 1
            ptr += 1
            curr_state = 'B'
        elif curr_val == 1:
            tape[ptr] = 0
            ptr += 1
            curr_state = 'C'
    # State B
    elif curr_state == 'B':
        if curr_val == 0:
            tape[ptr] = 0
            ptr -= 1
            curr_state = 'A'
        elif curr_val == 1:
            tape[ptr] = 0
            ptr += 1
            curr_state = 'D'
    # State C
    elif curr_state == 'C':
        if curr_val == 0:
            tape[ptr] = 1
            ptr += 1
            curr_state = 'D'
        elif curr_val == 1:
            tape[ptr] = 1
            ptr += 1
            curr_state = 'A'
    # State D
    elif curr_state == 'D':
        if curr_val == 0:
            tape[ptr] = 1
            ptr -= 1
            curr_state = 'E'
        elif curr_val == 1:
            tape[ptr] = 0
            ptr -= 1
            curr_state = 'D'
    # State E
    elif curr_state == 'E':
        if curr_val == 0:
            tape[ptr] = 1
            ptr += 1
            curr_state = 'F'
        elif curr_val == 1:
            tape[ptr] = 1
            ptr -= 1
            curr_state = 'B'
    # State F
    elif curr_state == 'F':
        if curr_val == 0:
            tape[ptr] = 1
            ptr += 1
            curr_state = 'A'
        elif curr_val == 1:
            tape[ptr] = 1
            ptr += 1
            curr_state = 'E'
    
checksum = sum(tape[k] for k in tape.keys())
print("Part 1:", checksum)