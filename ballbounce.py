from vpython import *


# ball = sphere(pos=r, color=color.orange, make_trail=True)
# pointer = arrow(axis=r, pos=vector(1,0,1), round=True)
ball = sphere(color=color.red, radius=0.5, pos=vector(0,20,0), make_trail=True)
floor = box(pos=vector(0,0,0), color=color.white, length=100, height=0.3, width=10)
ball.velocity = vector(0,0,0)
dt = 0.001
# non perfect elastic
e = 0.5

# surface friction
sf = 0.999

while True:
    rate(1000)
    ball.pos = ball.pos + ball.velocity*dt
    if ball.pos.y < ball.radius:
        ball.velocity.y = abs(ball.velocity.y)*e
        ball.velocity.x = ball.velocity.x*sf
    else:
        ball.velocity.y = ball.velocity.y - 9.8*dt
       