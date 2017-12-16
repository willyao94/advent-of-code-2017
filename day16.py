def dance(moves, iterations=1):
    position = list('abcdefghijklmnop')
    seen = []
    for n in xrange(iterations):
        # Look for a cycle
        if ''.join(position) in seen:
            return seen[iterations % n]
        else:
            seen.append(''.join(position))
            for x in moves:
                move = x[0]
                if move == 's':
                    pos = int(x[1:])
                    position = position[-pos:] + position[:len(position)-pos]
                elif move == 'x':
                    a,b = map(int,x[1:].split('/'))
                    position[a], position[b] = position[b], position[a]
                elif move == 'p':
                    a,b = x[1:].split('/')
                    i_a = position.index(a)
                    i_b = position.index(b)
                    position[i_a], position[i_b] = position[i_b], position[i_a]
    return ''.join(position)


moves = open('./Inputs/day16.txt').read().split(',')
print("Part 1:", dance(moves))
print("Part 2:", dance(moves, 1000000000))