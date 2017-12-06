arr = [int(x) for x in open('./Inputs/day6.txt').read().strip().split()]
num_blks = len(arr)
seen = []
steps = 0
while not arr in seen:
    seen.append(arr[:])
    val = max(arr)
    ptr = arr.index(val)
    # Calc how much val will be divided to all other indices
    increment = val // (num_blks-1) if val >= num_blks else 1
    # Calc if there is any left over after distribution
    arr[ptr] = val % (num_blks-1) if val >= num_blks else 0
    ptr = (ptr + 1) % num_blks
    # Restrict range to at most num blocks
    iterations = val if val < num_blks else num_blks - 1
    for i in range(iterations):
        x = (ptr + i) % num_blks
        arr[x] += increment
    steps += 1

print("Part 1: ", steps)
print("Part 2: ", steps - seen.index(arr))