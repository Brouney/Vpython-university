from vpython import *

scene = canvas(width=1000, height=1000, range=9.5**12)

slonce = sphere(pos=vector(-150*10**9 , 0, 0), color=color.yellow, v=vector(0, 30 * 10 ** 3, 0), radius=11.5**10)
merkury = sphere(pos=vector(-80*10**9, 0, 0), color=color.orange, v=vector(0, 47 * 10 ** 3, 0), make_trail=True, radius=10**10)
wenus = sphere(pos=vector(-40*10**9, 0, 0), color=color.green, v=vector(0, 35 * 10 ** 3, 0), make_trail=True, radius=10**10)
ziemia = sphere(pos=vector(0, 0, 0), color=color.blue, make_trail=True,
               radius=10**10)
mars = sphere(pos=vector(100*10**9, 0, 0), color=color.red, v=vector(0, 24 * 10 ** 3, 0), make_trail=True, radius=10**10)


scene.center = ziemia.pos

M = 2 * 10 ** 30
G = 6.67 * (10 ** -11)
dt = 3600

while (True):
    rate(1000)
    merkury.a = -G * M * merkury.pos / mag(merkury.pos) ** 3
    wenus.a = -G * M * wenus.pos / mag(wenus.pos) ** 3
    slonce.a = -G * M * slonce.pos / mag(slonce.pos) ** 3
    mars.a = -G * M * mars.pos / mag(mars.pos) ** 3
    
    merkury.v += merkury.a * dt
    merkury.pos += merkury.v * dt

    wenus.v += wenus.a * dt
    wenus.pos += wenus.v * dt

    slonce.v += slonce.a * dt
    slonce.pos += slonce.v * dt

    mars.v += mars.a * dt
    mars.pos += mars.v * dt    
