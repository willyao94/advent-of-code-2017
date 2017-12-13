def infiltrate_firewall(delay, stealth=False):
    """ Computes the severity of infiltrating firewall given delay
    delay: ticks to wait before infiltrating
    stealth: restart if true and caught by scanner
    """
    severity = 0
    # The depth of a layer of the firewall is how many ticks have occured
    for tick, range in firewall.items():
        if (tick + delay) % (2*range - 2) == 0:
            severity = (severity + tick*range) if not stealth else -1
            if stealth:
                break
    return severity


firewall = {}
for x in open('./Inputs/day13.txt').readlines():
    depth, r = map(int,x.split(":"))
    firewall[depth] = r
print("Part 1:", infiltrate_firewall(0))

delay = 0
while True:
    delay += 1
    if infiltrate_firewall(delay, True) == 0:
        break
print("Part 2:", delay)