steps = int(open('./Inputs/day17.txt').read().strip())

# Part 1
buffer = [0]
ptr = 0
for n in range(1,2019):
    ptr = ((ptr + steps) % n) + 1
    buffer.insert(ptr, n)
ptr = buffer.index(2017)
print("Part 1:", buffer[(ptr+1)%len(buffer)])

# Part 2
ptr = 0
# Value 0 always stays at index 0
# Keep track of the values in index 1
cache = []
for n in range(1,50000001):
    ptr = ((ptr + steps) % n) + 1
    if ptr == 1:
        cache.append(n)
print("Part 2:", cache[-1])