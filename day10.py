from functools import reduce


def knot_hash(key):
    lengths = list(map(ord, key))
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

    dense_hash = []
    for i in range(n//16):
        # Xor every element together in each partition
        dense_hash.append(reduce(lambda i, j: i ^ j, nums[i*16:i*16+16]))
    # Create hash by converting and joining together the 2 digit hex string of an int
    return ''.join("%0.2x" % i for i in dense_hash)


if __name__ == "__main__":
    # Part 1
    #lengths = list(map(int, (open('./Inputs/day10.txt').read().strip().split(','))))

    # Part 2
    print(knot_hash(open('./Inputs/day10.txt').read().strip()))