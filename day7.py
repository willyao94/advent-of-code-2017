def calc_total_weight(x):
    """Calculate the total weight of a given node in a tree
    tree and weights are global vars
    """
    if len(tree[x]) == 0:
        return combined_weights[x]
    else:
        combined_weights[x] += sum([calc_total_weight(y) for y in tree[x]])
        return combined_weights[x]


input = [x.strip().split() for x in open('./Inputs/day7.txt').readlines()]
seen = []
weights = {}
tree = {}
for x in input:
    # Has format [key, (weight), '->', children]
    # Add node to tree
    tree[x[0]] = []
    # Add children to node
    if (len(x)) > 3:
        for i in range(3, len(x)):
            x[i] = x[i].replace(',','')
            tree[x[0]].append(x[i])
            # Only append children since root can't be a child
            seen.append(x[i])
    # Create weights mapping
    weights[x[0]] = int(x[1].strip("()"))

root = ''
for x in input:
    if not x[0] in seen:
        root = x[0]
print("Tree root is:",root)

# Make a new tree with each node having its weight combined with its children's
combined_weights = dict(weights)
calc_total_weight(root)
parent = root
# Traverse each layer of the tree from the root
while True:
    # Get weights of children in the order they are
    seen = []
    for i in range(len(tree[root])):
        seen.append(combined_weights[tree[root][i]])

    temp = set(seen)
    i = 0
    if (len(temp) == 1):
        # If all children have the same weight, break
        break
    else:
        # Find weight that is diff
        for x in temp:
            if seen.count(x) == 1:
                i = x
                break

    # Iterate on the child that has a diff weight
    i = seen.index(i)
    parent = root
    root = tree[root][i]

# Get the diff between the child with diff weight
seen = []
for i in range(len(tree[parent])):
    seen.append(combined_weights[tree[parent][i]])
seen = list(set(seen))
diff = abs(seen[0] - seen[1])
print("Node", root, "must weigh", weights[root] - diff, 
    "instead to have a balanced tree.")