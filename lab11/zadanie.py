from vpython import *
import math

#------------------------------------------------------
phi1        = math.pi       
tetha1      = math.pi - 0.1 

phi2        = math.pi       
tetha2      = math.pi - 0.1 

phiPrim1   = 0             
tethaPrim1 = 0 

phiPrim2   = 0             
tethaPrim2 = 0 

L1 = 1
L2 = 1.0000000001
#------------------------------------------------------
scene = canvas(width=920, height=680)
t = 0
g = 9.81
XX = vector(1,0,0)
YY = vector(0,1,0)
wektzer = vector(0,0,0)
scene.center = wektzer

thickness = 0.01
a = L1
aa = L2
radiuss = 0.05

phiBis1 = (-g/L1 * (2*math.sin(phi1) - math.sin(tetha1) * math.cos(phi1 - tetha1)) - 1/2 * phiPrim1 * phiPrim1 * math.sin(2*phi1 - 2*tetha1) - tethaPrim1*tethaPrim1*math.sin(phi1 - tetha1)) / (1 + math.sin(phi1 - tetha1)**2)

tethaBis1 = (-g/L1 * (2*math.sin(tetha1) - 2*math.sin(phi1) * math.cos(phi1 - tetha1)) + 1/2 * tethaPrim1 * tethaPrim1 * math.sin(2*phi1 - 2*tetha1) + 2*phiPrim1*phiPrim1*math.sin(phi1 - tetha1)) / (1 + math.sin(phi1 - tetha1)**2)

phiBis2 = (-g/L2 * (2*math.sin(phi2) - math.sin(tetha2) * math.cos(phi2 - tetha2)) - 1/2 * phiPrim2 * phiPrim2 * math.sin(2*phi2 - 2*tetha2) - tethaPrim2*tethaPrim2*math.sin(phi2 - tetha2)) / (1 + math.sin(phi2 - tetha2)**2)

tethaBis2 = (-g/L2 * (2*math.sin(tetha2) - 2*math.sin(phi2) * math.cos(phi2 - tetha2)) + 1/2 * tethaPrim2 * tethaPrim2 * math.sin(2*phi2 - 2*tetha2) + 2*phiPrim2*phiPrim2*math.sin(phi2 - tetha2)) / (1 + math.sin(phi2 - tetha2)**2)


Line1 = curve(pos=[a*wektzer, a*YY], color=color.yellow, radius=thickness)  
Ball1 = sphere(pos=a*YY, radius=radiuss, color=color.red, vel=wektzer)

Line2 = curve(pos=[a*YY, a*vector(1, 1, 0)], color=color.yellow, radius=thickness)
Ball2 = sphere(pos=(a*XX + a*YY), radius=radiuss, color=color.red, vel=wektzer)

Line11 = curve(pos=[aa*wektzer, aa*YY], color=color.red, radius=thickness)  
Ball11 = sphere(pos=aa*YY, radius=radiuss, color=color.yellow, vel=wektzer)

Line22 = curve(pos=[aa*YY, aa*vector(1, 1, 0)], color=color.red, radius=thickness)
Ball22 = sphere(pos=(aa*XX + aa*YY), radius=radiuss, color=color.yellow, vel=wektzer)

t = 0
dt = 0.001
while True:
    rate(500)
    
    posx1 = L1 * math.sin(phi1)
    posy1 = -L1 * math.cos(phi1)
    posx2 = posx1 + L1 * math.sin(tetha1)
    posy2 = posy1 - L1 * math.cos(tetha1)

    posx11 = L2 * math.sin(phi2)
    posy11 = -L2 * math.cos(phi2)
    posx22 = posx11 + L2 * math.sin(tetha2)
    posy22 = posy11 - L2 * math.cos(tetha2)

    Ball2.pos.x =  posx2
    Ball2.pos.y =  posy2
    Ball1.pos.x = posx1
    Ball1.pos.y = posy1

    Ball22.pos.x =  posx22
    Ball22.pos.y =  posy22
    Ball11.pos.x = posx11
    Ball11.pos.y = posy11

    Line1.modify(1, x=Ball1.pos.x, y=Ball1.pos.y)
    Line2.modify(0, x=Ball1.pos.x, y=Ball1.pos.y)
    Line2.modify(1, x=Ball2.pos.x, y=Ball2.pos.y)

    
    Line11.modify(1, x=Ball11.pos.x, y=Ball11.pos.y)
    Line22.modify(0, x=Ball11.pos.x, y=Ball11.pos.y)
    Line22.modify(1, x=Ball22.pos.x, y=Ball22.pos.y)

    phiBis1 = (-g/L1 * (2*math.sin(phi1) - math.sin(tetha1) * math.cos(phi1 - tetha1)) - 1/2 * phiPrim1 * phiPrim1 * math.sin(2*phi1 - 2*tetha1) - tethaPrim1*tethaPrim1*math.sin(phi1 - tetha1)) / (1 + math.sin(phi1 - tetha1)**2)
    tethaBis1 = (-g/L1 * (2*math.sin(tetha1) - 2*math.sin(phi1) * math.cos(phi1 - tetha1)) + 1/2 * tethaPrim1 * tethaPrim1 * math.sin(2*phi1 - 2*tetha1) + 2*phiPrim1*phiPrim1*math.sin(phi1 - tetha1)) / (1 + math.sin(phi1 - tetha1)**2)

    phiBis2 = (-g/L2 * (2*math.sin(phi2) - math.sin(tetha2) * math.cos(phi2 - tetha2)) - 1/2 * phiPrim2 * phiPrim2 * math.sin(2*phi2 - 2*tetha2) - tethaPrim2*tethaPrim2*math.sin(phi2 - tetha2)) / (1 + math.sin(phi2 - tetha2)**2)
    tethaBis2 = (-g/L2 * (2*math.sin(tetha2) - 2*math.sin(phi2) * math.cos(phi2 - tetha2)) + 1/2 * tethaPrim2 * tethaPrim2 * math.sin(2*phi2 - 2*tetha2) + 2*phiPrim2*phiPrim2*math.sin(phi2 - tetha2)) / (1 + math.sin(phi2 - tetha2)**2)

    phiPrim1   += phiBis1 * dt
    tethaPrim1 += tethaBis1 * dt
    phi1   += phiPrim1 * dt
    tetha1 += tethaPrim1 * dt

    phiPrim2   += phiBis2 * dt
    tethaPrim2 += tethaBis2 * dt
    phi2   += phiPrim2 * dt
    tetha2 += tethaPrim2 * dt

    t += dt