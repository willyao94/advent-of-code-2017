dirs = open('./Inputs/day11.txt').read().strip().split(',')
pos = [0,0]
steps = max_steps = 0
# Hex coordinate system based off of axial coordinates from
# https://www.redblobgames.com/grids/hexagons/
for d in dirs:
    if 'nw' == d:
        pos[0] -= 1
        pos[1] += 1
    elif 'n' == d:
        pos[1] += 1
    elif 'ne' == d:
        pos[0] += 1
    elif 'se' == d:
        pos[0] += 1
        pos[1] -= 1
    elif 's' == d:
        pos[1] -= 1
    elif 'sw' == d:
        pos[0] -= 1
    steps = (abs(pos[0]) + abs(pos[0] + pos[1]) + abs(pos[1])) / 2
    max_steps = max(max_steps, steps)

print("Fewest steps:", steps)
print("Furthest steps from start:", max_steps)