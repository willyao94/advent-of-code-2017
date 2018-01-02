def print_image(arr):
    for x in arr:
        print(x)
    print()

def rotate(box):
    box = box.split('/')
    new_grid = []
    #https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
    for r in zip(*box[::-1]):
        new_grid.append(''.join(r))
    return '/'.join(new_grid)

def flip_x(box):
    box = flip_y(box)
    for i in range(2):
        box = rotate(box)
    return box

def flip_y(box):
    new_grid = []
    for r in box.split('/'):
        new_grid.append(r[::-1])
    return '/'.join(new_grid)

transformations = dict()
#output = open('./my_output.txt', 'w')
for x in open('./Inputs/day21.txt').readlines():
    arr = x.strip().split(' => ')
    transformations[arr[0]] = arr[1]
    
    # Add other variations
    rotated = arr[0]
    for r in range(4):
        rotated = rotate(rotated)
        x = flip_x(rotated)
        y = flip_y(rotated)
        transformations[rotated] = arr[1]
        transformations[x] = arr[1]
        transformations[y] = arr[1]

image = [".#.","..#","###"]
print(image)
iterations = 18
for _ in range(iterations):
    size = len(image[0])
    #print("size: %d" % size)
    if size%2 == 0 or size%3 == 0:
        n = 2 if size%2==0 else 3
        #print("n: %d" % n)
        splits = []
        for a in range(size//n):
            x = a * n
            for b in range(size//n):
                y = b * n
                box = ''
                for i in range(n):
                    for j in range(n):
                        box += image[x+i][y+j]
                    if i < n-1:
                        box += '/'
                splits.append(box)
        
        grid = [transformations[k] for k in splits]
        #print(grid)

        grid = [_.split('/') for _ in grid]
        # Piece back splits together
        new_image = []
        for a in range(size//n):
            for b in range(len(grid[0])):
                line = ''
                for c in range(size//n):
                    line += grid[c+(size//n)*a][b]
                new_image.append(line)
        image = new_image
#print_image(image)
    #print()
count = ''.join(image).count('#')

print(count)