from day10 import knot_hash


input = open('./Inputs/day14.txt').read().strip()
#input = 'flqrgnkx'
count = regions = 0
grid = [[0 for x in range(128)] for y in range(128)]
for i in range(128):
    hash = knot_hash(input + '-' + str(i))
    # https://stackoverflow.com/a/4859937
    binary = bin(int(hash, 16))[2:].zfill(128)
    grid[i] = list(map(int,binary))
    count += sum(grid[i])
print("Part 1:", count)

seen = []
for x in range(len(grid)):
    for y in range(len(grid[x])):
        if (x,y) in seen or not grid[x][y]:
            continue
        regions += 1
        # DFS
        frontier = [(x,y)]
        while len(frontier):
            i,j = frontier.pop()
            if (i,j) in seen or not grid[i][j]:
                continue
            seen.append((i,j))
            # Search surrounding if within bounds
            if i>0:
                frontier.append((i-1,j))
            if i<127:
                frontier.append((i+1,j))
            if j>0:
                frontier.append((i,j-1))
            if j<127:
                frontier.append((i,j+1))
print("Part 2:", regions)