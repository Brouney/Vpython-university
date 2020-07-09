
from vpython import *
def check(ball,wallR, wallL, wallT, wallB, wallBack, wallFront,d):
    d=d/2
    if (ball.pos.x >= wallR.pos.x -d- ball.radius):
        ball.vel.x = -ball.vel.x
        ball.color = wallR.color
       
    elif (ball.pos.x <= wallL.pos.x +d+ ball.radius):
        ball.vel.x = -ball.vel.x
        ball.color = wallL.color
        
    elif (ball.pos.y >= wallT.pos.y-d - ball.radius):
        ball.vel.y = -ball.vel.y
        ball.color = wallT.color
        
    elif (ball.pos.y <= wallB.pos.y+d + ball.radius):
        ball.vel.y = -ball.vel.y
        ball.color = wallB.color
        
    elif (ball.pos.z >= wallFront.pos.z -d- ball.radius):
        ball.vel.z = -ball.vel.z
        ball.color = wallFront.color
       
    elif (ball.pos.z <= wallBack.pos.z +d+ ball.radius):
        ball.vel.z = -ball.vel.z
        ball.color = wallBack.color
        