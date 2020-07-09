from vpython import *
from random import *
from math import *
from time import *

#---------------------------------------------------
N = 25 #ilość małych kulek - identycznych
malamasa = 1 #masy małych kuleczek
duzamasa = 100 #masa dużej kuleczki
prommaly = 1 #promien malych
promduzy = 2  #promien duzych kulek
#---------------------------------------------------

scene = canvas(width = 1200,height = 800)
N = N+1

NN = N
if NN < 20:
    NN = 20

def random_V():
    return vector(uniform(-4, 4), uniform(-4, 4), 0)


line = curve(pos=[vector(-NN,-NN,0),vector(-NN,NN,0),vector(NN,NN,0),vector(NN,-NN,0),vector(-NN,-NN,0)],color=color.purple,radius = 0.5)

balls = []
for i in range(N - 1):
    balls.append(sphere(pos=vector((-NN/2 + 1.5 * i), (-NN/2 + 1.5 * i), 0),
                        radius=prommaly, color=color.yellow))
balls.append(sphere(pos=vector((-15), (15), 0),
                    radius=promduzy, color=color.red))
pos = [b.pos for b in balls]
vel = [random_V() for b in balls]
vel[N - 1] = random_V()
m = [malamasa for b in balls]  
m[N - 1] = duzamasa          #masa dużej kuleczki

tra = curve(radius = 0.09)

sleep(2)
dt = 0.005
while 1:
    rate(500)
    for i in range(N):
        
        if pos[i].x - balls[i].radius < -NN + 0.5 or pos[i].x + balls[i].radius > NN - 0.5:
            vel[i].x = -vel[i].x
           
        elif pos[i].y  + balls[i].radius > NN - 0.5 or pos[i].y - balls[i].radius < -NN + 0.5:
             vel[i].y = -vel[i].y

        for j in range(i,N):
            if i != j and mag(pos[i] - pos[j]) < balls[i].radius + balls[j].radius:

                a = mag(vel[i] - vel[j]) ** 2
                b = dot(-2 * (pos[i] - pos[j]), (vel[i] - vel[j]))
                c = mag(pos[i] - pos[j]) ** 2 - \
                    (balls[i].radius + balls[j].radius) ** 2

                delta = b ** 2 - 4 * a * c

                if a != 0 and delta > 0:
                    dtprim = (-b + sqrt(delta)) / (2 * a)

                    pos[i] = pos[i] - vel[i] * dtprim
                    pos[j] = pos[j] - vel[j] * dtprim

                    zmienna = (dot(vel[i] - vel[j], (pos[i] - pos[j]) / mag(pos[i] - pos[j]))) * (
                                (pos[i] - pos[j]) / mag(pos[i] - pos[j]))

                    vel[i] -= (2 * m[j] / (m[i] + m[j])) * zmienna
                    vel[j] += (2 * m[i] / (m[i] + m[j])) * zmienna

                    pos[i] += vel[i] * dtprim
                    pos[j] += vel[j] * dtprim

                    balls[i].pos = pos[i]
                    balls[j].pos = pos[j]

        
        pos[i] = pos[i] + dt * vel[i]
        balls[i].pos = pos[i]
        if i == N-1:
            tra.append(pos = pos[i],retain = 500)
