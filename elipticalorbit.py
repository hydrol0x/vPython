from time import thread_time
from vpython import *

# radius
r = 20
# angular velocity
omega = 2*pi*r/360
dt = 0.01
theta = 0
# a is x part of ellipse axis
a = 15
# b is y part of ellipse axis
b = 1
# focus of ellipse
c = sqrt(a**2 + b**2)

planet = sphere(pos=vector(r,0,0), color=color.blue, radius=1, make_trail=True)

star = sphere(pos=vector(0,0,0), color=color.yellow, radius=5)
if a > b:
    star.pos = star.pos + vector(c,0,0)
    e = c/a
else:
    star.pos = star.pos + vector(0,c,0)
    e = c/b
string = f'eccentricity: {e}'
display = text(text=string)

while True:
    rate(100)
    # defining circular motion through trig
    planet.pos.x = a*r*cos(theta)
    planet.pos.y = b*r*sin(theta)
    # updating omega
    theta = theta + omega*dt