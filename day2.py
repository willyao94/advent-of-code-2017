sum_part1 = 0
sum_part2 = 0
with open('./Inputs/day2.txt') as f:
    for line in f:
        # Part 1
        arr = list(map(int, line.strip().split('\t')))
        sum_part1 += max(arr) - min(arr)

        # Part 2
        for m in range(len(arr)):
            for n in range(len(arr)):
                if arr[m] == arr[n] or arr[m] < arr[n]:
                    continue
                elif arr[m] % arr[n] == 0:
                    sum_part2 += arr[m] / arr[n]

print(sum_part1)
print(sum_part2)