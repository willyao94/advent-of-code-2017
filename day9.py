input = open('./Inputs/day9.txt').read().strip()

i = 0
depth = 0
score = 0
garbage_chars = 0
garbage = False
while i<len(input):
    c = input[i]
    if c == '!':
        i += 1
    elif garbage:
        if c == '>':
            garbage = False
        else:
            garbage_chars += 1
    else:
        if c == '{':
            depth += 1
        elif c == '}':
            score += depth
            depth -= 1
        elif c == '<':
            garbage = True
    i += 1
print(score)
print(garbage_chars)