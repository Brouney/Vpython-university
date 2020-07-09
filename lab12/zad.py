from vpython import *
import math


for k in range(6):

    scene = canvas(width=920, height=680)
    box1 = box(pos = vector(-1.1,0,0),size = vector(1,1,1))
    box2 = box(pos = vector(0,0,0),size = vector(1,1,1))
    wall = box(pos = vector(2.1,0,0), size = vector(0.1,3,3))
    tt = label(pos = vector(0,1,0),text = '0',height = 20,color = color.cyan, linecolor = color.red,)
    tt2 = label(pos = vector(-1.6,1,0),text = '0',height = 20,color = color.cyan, linecolor = color.red)
    tt2.text = "k = "+str(k)
    m1 = 100**k
    m2 = 1

    box1.vel = vector(1,0,0)
    box2.vel = vector(0,0,0)
    t = 0
    dt = 0.0001

    if k > 3:
        dt = 1 / (10**(k+2))
    licznik = 0
    while box1.pos.x > -10:
        rate(10000) 
        if k > 3:
            if box1.pos.x <-2:
                break;
        if (sqrt(pow(box2.pos.x - box1.pos.x,2))) < 1 :
            licznik +=1
            V1prim = ((m1-m2)/(m1+m2))*box1.vel + ((2*m2)/(m1+m2)) * box2.vel
            V2prim = ((m2-m1)/(m1+m2))*box2.vel + ((2*m1)/(m1+m2)) * box1.vel
            box1.vel = V1prim
            box2.vel = V2prim
        elif box2.pos.x > 1.55:
            box2.vel = -box2.vel
            licznik +=1
        box1.pos = box1.pos + box1.vel * dt
        box2.pos = box2.pos + box2.vel * dt
        tt.text = str(licznik)
        t+=dt
    scene.delete()
