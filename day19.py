def step(dir, pos):
    if dir == 0:
        pos -= length
    elif dir == 1:
        pos += 1
    elif dir == 2:
        pos += length
    elif dir == 3:
        pos -= 1
    return pos


input = open('./Inputs/day19.txt').read()
length = input.index('\n')  
maze = input.replace('\n','')
# starting position is first index of |
pos = maze.index('|')
# 0 = up, 1 = right, 2 = down, 3 = left
dirs = [0,1,2,3]
curr_dir = 2
letters = ''
steps = 0
while True:
    obj = maze[pos]
    if obj == ' ':
        # No where left to go; end of maze
        break
    elif obj.isalpha():
        letters += obj
    elif obj == '+':
        op_dir = (curr_dir+2)%len(dirs)
        while True:
            curr_dir+=1
            new_dir = (curr_dir)%len(dirs)
            # Don't go in opposite direction
            if new_dir == op_dir:
                continue
            new_pos = step(new_dir, pos)
            if 0<=new_pos<len(maze) and maze[new_pos] != ' ':
                curr_dir = new_dir
                break

    pos = step(curr_dir, pos)
    steps+=1
print("Part 1:", letters)
print("Part 2:", steps)