input = open('./Inputs/day1.txt').read().strip()
# Part 1
sum_part1 = 0
for i in range(len(input)):
	if input[i] == input[i-1]:
		sum_part1 += int(input[i])
print(sum_part1)

# Part 2
sum_part2 = 0
halfLength = int(len(input) / 2)
for i in range(len(input)):
	if input[i] == input[(i+halfLength) % len(input)]:
		sum_part2 += int(input[i])
print(sum_part2)