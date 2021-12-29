from time import thread_time
from vpython import *

# radius
r = 20
# angular velocity
omega = 2*pi*r/360
dt = 0.01
theta = 0

planet = sphere(pos=vector(r,0,0), color=color.blue, radius=1, make_trail=True)
star = sphere(pos=vector(0,0,0), color=color.yellow, radius=5)

while True:
    rate(100)
    # defining circular motion through trig
    planet.pos.x = 20*cos(theta)
    planet.pos.y = 20*sin(theta)
    # updating omega
    theta = theta + omega*dt