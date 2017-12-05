import math

def solve_part1(input):
    if input == 1:
        print(0)
        return

    # Find which layer the input will be in the spiral
    layer = 0
    # Build up arr of the starting numbers in a layer that contains input
    spiral = [1]
    while input >= spiral[layer]:
        if layer == 0:
            spiral.append(spiral[layer] + 1)
        else:
            spiral.append(spiral[layer] + 8*layer)
        layer += 1

    layer_side_count = 2*layer - 1
    layer_first_num = spiral[len(spiral)-2]
    layer_last_num = spiral[len(spiral)-1]-1

    # Find the starting num of the side the input is in
    side_start = spiral[len(spiral)-2]
    for i in range(4):
        if input in range(side_start, side_start + layer_side_count-1):
            break
        else:
            side_start += layer_side_count-1

    # Find the offset
    offset = 0
    while side_start < layer_last_num:
        if side_start == input:
            break
        else:
            side_start += 1
            offset += 1
    # Calculate the distance
    dist = abs(offset - (layer - 2)) + (layer - 1)
    print("Dist: {0}".format(dist))

def solve_part2(input):
    layer = 1
    # Must pick an odd num, large enough value + 1 to avoid out of bound checks
    length = height = 11
    matrix = [[0 for x in range(length)] for y in range(height)]
    x_ptr = math.floor(length / 2)
    y_ptr = math.floor(height / 2)
    # Starting value
    matrix[x_ptr][y_ptr] = 1
    x_ptr = x_ptr+1
    while layer < math.floor(length/2):
        count = layer * 2
        # Left-side
        for x in range(count):
            sum_surrounding(matrix, x_ptr, y_ptr, input)
            y_ptr -= 1
        x_ptr -= 1
        y_ptr += 1
        # Top-side
        for x in range(count):
            sum_surrounding(matrix, x_ptr, y_ptr, input)
            x_ptr -= 1
        x_ptr += 1
        y_ptr += 1
        # Right-side
        for x in range(count):
            sum_surrounding(matrix, x_ptr, y_ptr, input)
            y_ptr += 1
        x_ptr += 1
        y_ptr -= 1
        # Bottom-side
        for x in range(count):
            sum_surrounding(matrix, x_ptr, y_ptr, input)
            x_ptr += 1
        layer += 1

def print_matrix(m):
    [print(x) for x in m]
    print()

def sum_surrounding(m, x, y, input):
    val = 0
    # Top
    val += m[y-1][x-1]
    val += m[y-1][x]
    val += m[y-1][x+1]
    # Centre
    val += m[y][x-1]
    val += m[y][x+1]
    # Bottom
    val += m[y+1][x-1]
    val += m[y+1][x]
    val += m[y+1][x+1]
    
    m[y][x] = val
    if val > input:
        print("1st larger val: {0}".format(val))
        # Very ugly
        exit()

input = int(open('./Inputs/day3.txt').read().strip())
solve_part1(input)
solve_part2(input)