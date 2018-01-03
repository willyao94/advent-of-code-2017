def make_tree(n, arr):
    build = []
    for c in arr:
        a, b = map(int, c.split('/'))
        if a==n or b==n:
            m = b if a==n else a
            others = arr[:]
            others.remove(c)
            temp = [c]            
            branch = make_tree(m, others)
            if len(branch):
                temp += branch
            build.append(temp)
    return build 

def dfs_strongest(b):
    if not len(b):
        return 0
    x,y = map(int, b[0].split('/'))
    curr = x+y
    temp = 0
    for i in xrange(1,len(b)):
        temp = max(temp, dfs_strongest(b[i]))
    return curr + temp

def dfs_longest(b):
    if not len(b):
        return
    children = []
    for i in xrange(1, len(b)):
        children.append(dfs_longest(b[i]))
    longest = []
    for x in children:
        if len(x) > len(longest):
            longest = x
        elif len(x) == len(longest):
            longest = bridge_compare(x, longest)
    return [b[0]] + longest

def bridge_compare(a, b):
    str_a = sum_bridge(a)
    str_b = sum_bridge(b)
    return a if str_a > str_b else b

def sum_bridge(b):
    return sum(sum(map(int, i.split('/'))) for i in b)

components = [x.strip() for x in open('./Inputs/day24.txt').readlines()]
tree = []
for x in components:
    a, b = map(int, x.split('/'))
    if a==0 or b==0:
        if b==0:
            b = a
            a = 0
        others = components[:]
        others.remove(x)
        temp = make_tree(b, others)
        temp.insert(0,x)
        tree.append(temp)

strongest = 0
for branches in tree:
    strongest = max(strongest, dfs_strongest(branches))
print("Part 1:", strongest)

longest = []
for branches in tree:
    temp = dfs_longest(branches)
    if len(temp) > len(longest):
        longest = temp
    elif len(temp) == len(longest):
        longest = bridge_compare(longest, temp)

longest_str = sum_bridge(longest)
print("Part 2:", longest_str)