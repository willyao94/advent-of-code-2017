def extend_matrix(m, x, y):
    if x < 0:
        m.insert(0,['.' for _ in range(len(m[0]))])
    elif x > len(matrix)-1:
        m.append(['.' for _ in range(len(m[0]))])
    elif y < 0:
        for i in m:
            i.insert(0,'.')
    elif y > len(matrix[0])-1:
        for i in m:
            i.append('.')
    return m

matrix = [list(x.strip()) for x in open('./Inputs/day22.txt').readlines()]
n = len(matrix)
# 0 = up, 1 = left, 2=down, 3=right
dirs = { 0: (-1,0), 1: (0,-1), 2: (1,0), 3: (0,1)}
x = y = n//2
iterations = 10000000
curr_dir = infections = 0
for _ in range(iterations):
    curr_node = matrix[x][y]
    if curr_node == '.':
        matrix[x][y] = 'W'
        # Turn left
        curr_dir = (curr_dir+1)%4
    elif curr_node == 'W':
        matrix[x][y] = '#'
        infections += 1
    elif curr_node == '#':
        matrix[x][y] = 'F'
        # Turn right
        curr_dir = curr_dir-1 if curr_dir-1 >= 0 else 3
    elif curr_node == 'F':
        matrix[x][y] = '.'
        # Reverse direction
        curr_dir = (curr_dir+2)%4
    move = dirs[curr_dir]
    x += move[0]
    y += move[1]
    if x > len(matrix)-1 or x < 0 or y > len(matrix[0])-1 or y < 0:
        matrix = extend_matrix(matrix, x, y)
        if x < 0:
            x = 0
        if y < 0:
            y = 0
print("Infections:", infections)