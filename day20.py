from functools import total_ordering

@total_ordering
class Particle:
    def __init__(self, p, v, a):
        self.pos = p
        self.vel = v
        self.acc = a

    def __lt__(self, other):
        if self.pos[0] != other.pos[0]:
            return self.pos[0] < other.pos[0]
        elif self.pos[1] != other.pos[1]:
            return self.pos[1] < other.pos[1]
        elif self.pos[2] != other.pos[2]:
            return self.pos[2] < other.pos[2]

    def __eq__(self, other):
        return ((self.pos[0] == other.pos[0]) and 
                (self.pos[1] == other.pos[1]) and
                (self.pos[2] == other.pos[2]))

    def step(self):
        x = self.vel[0] + self.acc[0]
        y = self.vel[1] + self.acc[1]
        z = self.vel[2] + self.acc[2]
        self.vel = (x,y,z)
        x = self.pos[0] + self.vel[0]
        y = self.pos[1] + self.vel[1]
        z = self.pos[2] + self.vel[2]
        self.pos = (x,y,z)

if __name__ == "__main__":
    particles = []
    for x in open('./Inputs/day20.txt').readlines():
        x = x.strip().split(', ')
        temp = []
        for i in range(len(x)):
            temp.append(tuple(map(float, x[i][3:-1].split(','))))
        p = Particle(temp[0],temp[1],temp[2])
        particles.append(p)

    t=1000
    min_dist = (1 << 61)
    min_index = 0
    for i,p in enumerate(particles):
        # s = s_0 + v_0*t + 0.5*a*t^2
        x = p.pos[0] + p.vel[0]*t + (p.acc[0]/2)*(t**2)
        y = p.pos[1] + p.vel[1]*t + (p.acc[1]/2)*(t**2)
        z = p.pos[2] + p.vel[2]*t + (p.acc[2]/2)*(t**2)
        temp = sum(abs(a) for a in [x,y,z])
        if min_dist > temp:
            min_dist = temp
            min_index = i
    print("Part 1:", min_index)

    while True:
        for p in particles:
            p.step()
        particles.sort()

        collisions = []
        for i in range(len(particles)-1):
            if particles[i] == particles[i+1]:
                collisions.append(particles[i])
                collisions.append(particles[i+1])
                
        for p in collisions:
            if p in particles:
                particles.remove(p)
        # Answer will be the value that hasn't changed in a while
        print(len(particles))