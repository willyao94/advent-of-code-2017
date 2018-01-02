class Particle:
    def __init__(self, p, v, a):
        self.pos = p
        self.vel = v
        self.acc = a
        self.collides = False


def cross(a, b):
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]

    return c


def dot (a, b):
    return sum(a[i] * b[i] for i in range(len(a)))

particles = []
for x in open('./Inputs/day20.txt').readlines():
    x = x.strip().split(', ')
    temp = []
    for i in range(len(x)):
        temp.append(tuple(map(float, x[i][3:-1].split(','))))
    p = Particle(temp[0],temp[1],temp[2])
    particles.append(p)

t=10000
min_dist = (1 << 61)
min_index = 0
test = []
for i,p in enumerate(particles):
    # s = s_0 + v_0*t + 0.5*a*t^2
    x = p.pos[0] + p.vel[0]*t + (p.acc[0]/2)*(t**2)
    y = p.pos[1] + p.vel[1]*t + (p.acc[1]/2)*(t**2)
    z = p.pos[2] + p.vel[2]*t + (p.acc[2]/2)*(t**2)
    test.append((x,y,z))
    temp = sum(abs(a) for a in [x,y,z])
    if min_dist > temp:
        min_dist = temp
        min_index = i
print("Part 1:", min_index)

collided = dict()
count = 0
for i in range(len(particles)):
    if particles[i] in collided:
        continue
    
    for j in range(i+1, len(particles)):
        if particles[j] in collided:
            continue

        
print(count)
print(len(collided.keys()))