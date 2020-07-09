from vpython import *

n = 30

scene = canvas(width=1400, height=800, range=3 * n)

m = 1
k = 1
dt = 0.001
r = 0.6
g = 9.81
t = 0
balls = []
balls.append(sphere(color=color.red, radius=r, pos=vector(
    5, 50, 0), v=vector(0, 0, 0), frac=vector(0, 0, 0)))
for i in range(2, n+1):
    balls.append(sphere(color=color.red, radius=r, pos=vector(
        i * 5, 0, 0), v=vector(0, 0, 0), frac=vector(0, 0, 0)))


wallL = box(pos=vector(0, 0, 0), size=vector(0.1, 5, 3))
wallR = box(pos=vector((n + 1) * 5, 0, 0), size=vector(0.1, 5, 3))

scene.center = vector(n // 2 * 5, 0, 0)

heli = []

heli.append(helix(pos=vector(wallL.pos),
                  axis=balls[0].pos - wallL.pos, radius=0.2, coils=10, thickness=0.05))
heli.append(helix(pos=vector(balls[n - 1].pos), axis=wallR.pos -
                  balls[n - 1].pos, radius=0.2, coils=10, thickness=0.05))
for i in range(1, n):
    heli.append(helix(pos=vector(
        balls[i].pos), axis=balls[i - 1].pos - balls[i].pos, radius=0.2, coils=10, thickness=0.05))


while 1:
    rate(30)
    balls[0].force = k * (wallL.pos + balls[1].pos - 2 * balls[0].pos)
    for i in range(1, n - 1):
        balls[i].force = k * (balls[i - 1].pos +
                             balls[i + 1].pos - 2 * balls[i].pos)
    balls[n - 1].force = (balls[n - 2].pos + wallR.pos - 2 * balls[n - 1].pos)
    for tmp in balls:
        tmp.v = tmp.v + tmp.force / m
        tmp.pos = tmp.pos + tmp.v * dt
        tmp.v.y = tmp.v.y - g * dt
        tmp.pos.y = tmp.pos.y - g * (dt ** 2) / 2
        tmp.frac.y = dt * tmp.v.y
        tmp.v = tmp.v - tmp.frac / m

    heli[0].axis = balls[0].pos - wallL.pos
    for i in range(1, n):
        heli[i].pos = balls[i - 1].pos
        heli[i].axis = balls[i].pos - balls[i - 1].pos
    heli[n].pos = balls[n - 1].pos
    heli[n].axis = balls[n - 1].pos - wallR.pos
    t += dt
