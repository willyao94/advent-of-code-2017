def solve_part1(arr):
    ptr = counter = 0
    while ptr in range(0,len(arr)):
        val = arr[ptr]
        arr[ptr] += 1
        counter += 1
        ptr += val
    print(counter)

def solve_part2(arr):
    ptr = counter = 0
    while ptr in range(0,len(arr)):
        val = arr[ptr]
        arr[ptr] = arr[ptr]+1 if val < 3 else arr[ptr] - 1
        counter += 1
        ptr += val
    print(counter)

input = open('./Inputs/day5.txt').readlines()
a = [int(x) for x in input]
b = a[:]
solve_part1(a)
solve_part2(b)