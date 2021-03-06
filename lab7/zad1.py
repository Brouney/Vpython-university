from vpython import *
import random as rn
from func import *
scene = canvas(width = 550, height = 580)

ball = sphere(radius = 0.9,color = color.white)

ball.vel = vector(rn.random(), rn.random(), rn.random())
t = 0
dt = 0.005


d= 0.6
size = 8

wallR = box(pos = vector(4,0,0),size=vector(d,size,size),color=color.green)
wallL = box(pos = vector(-4,0,0),size=vector(d,size,size),color=color.red)
wallB = box(pos=vector(0, -4, 0), size=vector(size, d, size), color=color.yellow)
wallT = box(pos=vector(0, 4, 0), size=vector(size, d, size), color=color.blue)
wallBack = box(pos=vector(0, 0, -4), size=vector(size, size, d), color=color.orange)
wallFront = box(pos=vector(0, 0, 4), size=vector(size, size, d), color=color.white, opacity=0)


while t<100:
    rate(1000)
    ball.pos = ball.pos + ball.vel*dt
    check(ball,wallR, wallL, wallT, wallB, wallBack, wallFront,d)
    t+=dt

