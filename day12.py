def create_group(key):
    """ Returns a set of all nodes in graph connected to node[key]
    """
    stack = [x for x in graph[key]]
    seen = set()
    seen.update([key])
    # DFS to find all other nodes
    while len(stack) > 0:
        v = stack.pop()
        seen.update([v])
        for x in graph[v]:
            if not x in seen:
                stack.append(x)
    return seen


graph = {}
for x in open('./Inputs/day12.txt').readlines():
    key, _, val = x.split(maxsplit=2)
    graph[key] = val.replace(',','').split()
print("Part 1:", len(create_group('0')))

groups = 0
while len(graph) > 0:
    # Get a key from the graph
    key = next (iter (graph.keys()))
    group = create_group(key)
    groups += 1
    # Remove all nodes in graph that is in this group
    for x in group:
        graph.pop(x, None)
print("Part 2:", groups)