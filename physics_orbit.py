from time import thread_time
from vpython import *
scene.forward = vector(0,-.3,-1)


G = 6.7e-11

# acceleration direction = norm(vector pointing to 0, 0, 0)*mag(g_acc)

def g_acceleration(mass, radius):
    return -(G*mass / mag(radius)**2)

def centrifugal_acceleration(velocity, radius):
    return ((mag(velocity)**2)) / mag(radius)

planet = sphere(pos=vector(50,0,0), color=color.blue, radius=1, make_trail=True)
star = sphere(pos=vector(1e-5,0,0), color=color.yellow, radius=3, make_trail=True)
planet.mass=100
star.mass=10e8
planet.velocity = vector(0, 500, 1)
star.velocity = vector(0,0,10)
star.acceleration = vector(0,0,0)
scene.camera.follow(star)
# radius from origin

dt=0.0001
while True:
    rate(1000)
    planet_r = planet.pos - star.pos
    print(planet.pos)
    planet_a = ((planet.pos-star.pos).hat*(g_acceleration(star.mass, planet_r)-centrifugal_acceleration(planet.velocity, planet_r)))
    planet.velocity = planet.velocity + planet_a*dt
    planet.pos = planet.pos + planet.velocity*dt
    star.pos = star.pos + star.velocity * dt
    star.velocity = star.velocity + star.acceleration * dt
