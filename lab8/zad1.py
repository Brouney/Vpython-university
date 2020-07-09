from vpython import *

scene = canvas(width=1000, height=1000, range=9**12)

slonce = sphere(pos=vector(0, 0, 0), color=color.yellow, radius=11.5**10)
merkury = sphere(pos=vector(70*10**9, 0, 0), color=color.orange, v=vector(0, 47 * 10 ** 3, 0), make_trail=True, radius=10**10)
wenus = sphere(pos=vector(110*10**9, 0, 0), color=color.green, v=vector(0, 35 * 10 ** 3, 0), make_trail=True, radius=10**10)
ziemia = sphere(pos=vector(150*10**9, 0, 0), color=color.blue, v=vector(0, 30 * 10 ** 3, 0), make_trail=True,
               radius=10**10)
mars = sphere(pos=vector(250*10**9, 0, 0), color=color.red, v=vector(0, 24 * 10 ** 3, 0), make_trail=True, radius=10**10)

M = 2 * 10 ** 30
G = 6.67 * (10 ** -11)
dt = 3600

while (True):
    rate(1000)
    merkury.a = -G * M * merkury.pos / mag(merkury.pos) ** 3
    wenus.a = -G * M * wenus.pos / mag(wenus.pos) ** 3
    ziemia.a = -G * M * ziemia.pos / mag(ziemia.pos) ** 3
    mars.a = -G * M * mars.pos / mag(mars.pos) ** 3
    
    merkury.v += merkury.a * dt
    merkury.pos += merkury.v * dt

    wenus.v += wenus.a * dt
    wenus.pos += wenus.v * dt

    ziemia.v += ziemia.a * dt
    ziemia.pos += ziemia.v * dt

    mars.v += mars.a * dt
    mars.pos += mars.v * dt    
    


