from functools import reduce

# Part 1
#lengths = list(map(int, (open('./Inputs/day10.txt').read().strip().split(','))))

# Part 2
lengths = list(map(ord, open('./Inputs/day10.txt').read().strip()))
lengths.extend([17,31,73,47,23])

n = 256
nums = [x for x in range(n)]
curr_pos = 0
skip_size = 0
for r in range(64):
    for x in lengths:
        for c in range(x // 2):
            # Swap elements
            a = (curr_pos + c) % n
            b = (curr_pos + x - c - 1) % n
            nums[a], nums[b] = nums[b], nums[a]
        curr_pos = (curr_pos + x + skip_size) % n
        skip_size += 1
print(nums)

dense_hash = []
for i in range(n//16):
    # Xor every element together from each partition
    dense_hash.append(reduce(lambda i, j: i ^ j, nums[i*16:i*16+16]))
# Create hash by converting and joining together the int to a 2 digit hex string
knot_hash = ''.join("%0.2x" % i for i in dense_hash)
print(knot_hash)