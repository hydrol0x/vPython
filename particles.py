from time import thread_time
from vpython import *
import random
scene.forward = vector(0,-.3,-1)


# G = 6.7e-11
G = 10000

# acceleration direction = norm(vector pointing to 0, 0, 0)*mag(g_acc)

# def g_acceleration(mass, radius):
#     return -(G*mass / mag(radius)**2)

# def centrifugal_acceleration(velocity, radius):
#     return ((mag(velocity)**2)) / mag(radius)

# F = dp/dt 

def create_particle(mass, radius, position, velocity):
    particle = sphere(pos=position, color=color.blue, radius=radius, make_trail=True)
    particle.mass = mass
    particle.velocity = velocity 
    particle.momentum = velocity * mass
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
for i in range(2):
    x = random.randint(1, 100) 
    y = random.randint(1, 100) 
    z = random.randint(1, 100) 
    
    vx = random.randint(0, 1) 
    vy = random.randint(0, 1) 
    vz = random.randint(0, 1) 
    particle = create_particle(100, 1, vector(x,y,z), vector(vx,vy,vz))
    particles.append(particle) 
# particles.append(create_particle(1e6, 100, vector(0,0,0), vector(0,100,0)))
# planet = create_particle(1000, 5, vector(400,0,0), vector(0,0,5000))
# particles.append(planet)
# particles.append(create_particle(1, 1, vector(420,0,0), vector(0,500,5500)))
# scene.camera.follow(planet)


# Simulation loop
dt=0.00001
while True:
    for particle1 in particles:
        for particle2 in particles:
            if particle1 != particle2:
                #  2 acts on 1
                # dp/dt = F
                # Fdt = dp
                force = grav_force(particle1, particle2)
                dp = force*dt
                particle1.momentum += dp
                particle1.color = color.red
    for particle in particles:
        dx = (particle.momentum/particle.mass)*dt
        print(particles[0].pos)
        particle.pos+=dx
    rate(1/(dt))
    