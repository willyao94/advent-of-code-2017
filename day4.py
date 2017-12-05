with open('./Inputs/day4.txt') as f:
    count_part1 = count_part2 = 0
    for line in f:
        line = line.strip().split(" ")

        # Part 1
        seen = []
        dupe = 0
        for word in line:
            if not word in seen:
                seen.append(word)
            else:
                dupe = 1
                break
        if dupe == 0:
            count_part1 += 1

        # Part 2
        seen = []
        dupe = 0
        for word in line:
            dict = {}
            for c in word:
                dict[c] = 1 if not c in dict else dict[c] + 1
            if not dict in seen:
                seen.append(dict)
            else:
                dupe = 1
        if dupe == 0:
            count_part2 += 1
            
    print(count_part1)
    print(count_part2)