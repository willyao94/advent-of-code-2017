def generate(n, factor, mod=-1):
    while True:
        n = n * factor % 2147483647
        if mod < 0 or not n % mod:
            return n
            

initA, initB = [int(x.split()[-1]) for x in open('./Inputs/day15.txt').read().splitlines()]

A, B = initA, initB
factorA, factorB = 16807, 48271
part1 = part2 = 0

for _ in range(40000000):
    A = generate(A, factorA)
    B = generate(B, factorB)
    if (A & 0xFFFF) == (B & 0xFFFF):
        part1 += 1
print("Part 1:", part1)

A, B = initA, initB
for _ in range(5000000):
    A = generate(A, factorA, 4)
    B = generate(B, factorB, 8)
    if (A & 0xFFFF) == (B & 0xFFFF):
        part2 += 1
print("Part 2:", part2)