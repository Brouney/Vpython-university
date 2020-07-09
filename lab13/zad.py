
from vpython import *
import math
import numpy as np
import matplotlib.pyplot as plt
scene = canvas(width=920, height=680)

ball3 = sphere(pos = vector(0,1.5,0),radius = 0.1)
ball2 = sphere(pos = vector(0,1.25,0),radius = 0.1)
ball1 = sphere(pos = vector(0,1,0),radius = 0.1)
wall = box(pos = vector(0,0,0), size = vector(3,0.1,3))
m3 = 0.1
m2 = 1
m1 = 10

t = 0
dt = 0.0001
ball1.vel = vector(0,0,0)
ball2.vel = vector(0,0,0)
ball3.vel = vector(0,0,0)

g = 9.8

ydataball3 = np.array([])
timer = np.array([])

kinetyczna = np.array([])
potencjalna = np.array([])
zsumowana = np.array([])
while t < 20:
    rate(1000)
    ball1.vel.y = ball1.vel.y - g * (dt)
    ball2.vel.y = ball2.vel.y - g * (dt)
    ball3.vel.y = ball3.vel.y - g * (dt)

    if (sqrt(pow(ball2.pos.y - ball1.pos.y,2))) < 0.2:
        V1prim = ((m1-m2)/(m1+m2))*ball1.vel + ((2*m2)/(m1+m2)) * ball2.vel
        V2prim = ((m2-m1)/(m1+m2))*ball2.vel + ((2*m1)/(m1+m2)) * ball1.vel
        ball1.vel = V1prim
        ball2.vel = V2prim
    if (sqrt(pow(ball3.pos.y - ball2.pos.y,2))) < 0.2:
        V3prim = ((m3-m2)/(m3+m2))*ball3.vel + ((2*m2)/(m3+m2)) * ball2.vel
        V2prim = ((m2-m3)/(m3+m2))*ball2.vel + ((2*m3)/(m3+m2)) * ball3.vel
        ball3.vel = V3prim
        ball2.vel = V2prim
    if ball1.pos.y < 0.1:
        ball1.vel = - ball1.vel
    


    ball1.pos = ball1.pos + ball1.vel * dt
    ball2.pos = ball2.pos + ball2.vel * dt
    ball3.pos = ball3.pos + ball3.vel * dt
    

    ydataball3 = np.append(ydataball3,ball3.pos.y)

    timer = np.append(timer,t)

    kin = 1/2*m1*(ball1.vel.y**2) + 1/2*m2*(ball2.vel.y**2) + 1/2*m3*(ball3.vel.y**2 )
    kinetyczna = np.append(kinetyczna,kin)

    pot = m1*g*ball1.pos.y + m2*g*ball2.pos.y + m3*g*ball3.pos.y 
    potencjalna = np.append(potencjalna,pot)

    
    t+=dt

sumaryczna = kinetyczna + potencjalna
fig, (ax1, ax2) = plt.subplots(1, 2)

fig.suptitle('Wykresy')

ax1.plot(timer,ydataball3,color = "#FF69B4",label = 'y m3')

ax2.plot(timer,kinetyczna, color = "#FF7F50",label = 'Ek')
ax2.plot(timer,potencjalna, color = "#8B008B",label = 'Ep')
ax2.plot(timer,sumaryczna,color = "#1E90FF",label = 'Ek+Ep')
fig.legend(loc = 'upper right')

plt.show()


    





