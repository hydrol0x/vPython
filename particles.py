from time import thread_time
from vpython import *
import random
from itertools import combinations
scene.forward = vector(0,-.3,-1)

class Electron:
    def __init__(self, velocity: vector, pos):
       self.mass = 1 
       self.charge = -1
       self.velocity = velocity
       self.momentum = self.velocity * self.mass
       self._pos = pos
       self.sphere = sphere(pos=self._pos,make_trail=True)
       self.sphere.color = color.blue
    
    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        self._pos = value
        self.sphere.pos = value

class Proton:
    def __init__(self, velocity: vector, pos):
       self.mass = 1 
       self.charge = 1
       self.velocity = velocity
       self.momentum = self.velocity * self.mass
       self._pos = pos
       self.sphere = sphere(pos=self._pos,make_trail=True)
       self.sphere.color = color.red
    
    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        self._pos = value
        self.sphere.pos = value

class Neutron:
    def __init__(self, velocity: vector, pos):
       self.mass = 1 
       self.charge = 0
       self.velocity = velocity
       self.momentum = self.velocity * self.mass
       self._pos = pos
       self.sphere = sphere(pos=self._pos,make_trail=True)
       self.sphere.color = color.white
    
    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        self._pos = value
        self.sphere.pos = value


# G = 6.7e-11
# G = 6.7e-3
G = 0

# acceleration direction = norm(vector pointing to 0, 0, 0)*mag(g_acc)

# def g_acceleration(mass, radius):
#     return -(G*mass / mag(radius)**2)

# def centrifugal_acceleration(velocity, radius):
#     return ((mag(velocity)**2)) / mag(radius)

# F = dp/dt 

def create_particle(mass, radius, position, velocity):
    particle = sphere(pos=position, color=color.blue, radius=radius, make_trail=False)
    particle.velocity = velocity
    particle.mass = mass
    particle.momentum = velocity * mass
    # particle = Electron(velocity, position)
    return particle

def get_radius(particle1, particle2):
    return particle2.pos - particle1.pos

def grav_force(particle1, particle2):
    # F = -G* m1m2 / r^2 
    rad = get_radius(particle1, particle2)
    r = rad.hat
    force_mag = G*(particle1.mass*particle2.mass) / mag(rad)**2 
    force_vector = r * force_mag
    return force_vector
    

particles = []
for i in range(20):
    # x = random.randint(1, 10) 
    x=random.randint(1, 15) 
    y = random.randint(1, 15) 
    z = random.randint(1,15) 
    
    vx = random.randint(-100, 100) 
    vy = random.randint(-100, 100) 
    vz = random.randint(-100, 100) 

    particle = create_particle(100, 1, vector(x,y,z), vector(vx,vy,vz))
    particles.append(particle) 

def are_colliding(particle1, particle2):
    threshold = min(particle1.radius, particle2.radius) * .01
    sum_r = particle1.radius + particle2.radius
    distance = mag(particle2.pos - particle1.pos)
    return distance-threshold < sum_r

def calc_collision_dp(particle1, particle2):
    m1 = particle1.mass
    m2 = particle2.mass

    v1 = particle1.velocity
    v2 = particle2.velocity

    # Calculate the norm vector for collision
    r = particle2.pos - particle1.pos
    collision_vector = r.hat

    # Coefficient of restitution
    epsilon = 1 

    m_reduced = 1/((1/m1)+(1/m2))
    impact_v = collision_vector.dot(v2 - v1) # Impact speed

    J = (1+epsilon)*m_reduced*impact_v


    return collision_vector * J


# Simulation loop
dt=0.0000001
while True:
    
    for pair in combinations(particles,2):
        container_size = 20
        force = grav_force(*pair)
        dp = force*dt

        # # equal and opposite force
        particle1 = pair[0] 
        particle2 = pair[1]
        particle1.momentum += dp  
        particle2.momentum -=dp
        particle1.color = color.red

        if are_colliding(*pair):
            J = calc_collision_dp(*pair)
            particle1.momentum += J
            particle2.momentum -= J

        particle1.pos += (particle1.momentum / particle1.mass)*dt
        particle2.pos += (particle2.momentum / particle2.mass)*dt

        # # TODO : simulate actual plane or box collisions
        # if (particle1.pos.x > 20 or particle1.pos.x < -20 or 
        #     particle1.pos.y > 20 or particle1.pos.y < -20 or
        #     particle1.pos.z > 20 or particle1.pos.z < -20): 
        #         particle1.momentum = -particle1.momentum
        # if (particle2.pos.x > 20 or particle2.pos.x < -20 or 
        #     particle2.pos.y > 20 or particle2.pos.y < -20 or
        #     particle2.pos.z > 20 or particle2.pos.z < -20): 
        #         particle2.momentum = -particle2.momentum
                
                # For particle1
        if particle1.pos.x > container_size or particle1.pos.x < -container_size:
            particle1.momentum.x = -particle1.momentum.x
        if particle1.pos.y > container_size or particle1.pos.y < -container_size:
            particle1.momentum.y = -particle1.momentum.y
        if particle1.pos.z > container_size or particle1.pos.z < -container_size:
            particle1.momentum.z = -particle1.momentum.z

        # For particle2
        if particle2.pos.x > container_size or particle2.pos.x < -container_size:
            particle2.momentum.x = -particle2.momentum.x
        if particle2.pos.y > container_size or particle2.pos.y < -container_size:
            particle2.momentum.y = -particle2.momentum.y
        if particle2.pos.z > container_size or particle2.pos.z < -container_size:
            particle2.momentum.z = -particle2.momentum.z

        # energies = [0.5*particle.mass*(mag(particle.velocity)**2) for particle in particles]
                
    # for particle in particles:
    #     dx = (particle.momentum/particle.mass)*dt
    #     particle.pos+=dx
    rate(1/(dt))
    