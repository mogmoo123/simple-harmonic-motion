from vpython import *
from math import *

#objects
ball = sphere(pos=vector(5,0,0), radius = 1, color = color.green)
spring = helix(pos=vector(7,0,0),axis = vector(7,0,0), radius = 0.5, coils = 8, thickness = 0.1, color = color.gray(0.5))

#variables
k = 1
A = 5
m = 2
w = sqrt(k/m)
t = 0

#graph
gd_xt = graph(width = 500, height = 300, x = 410, y = 0, title = 'x-t graph', xtitle = 'time (s)', ytitle = 'x positon (m)', ymax = 6, ymin = -6, xmax= 20)
xt = gcurve(graph=gd_xt, color = color.red)

gd_vt = graph(width = 500, height = 300, x = 410, y = 0, title = "v-t graph", xtitle = 'time (s)', ytitle = 'velocity (m/s)', ymax = 6, ymin = -6, xmax = 20)
vt = gcurve(graph = gd_vt, color = color.red)

gd_at = graph(width = 500, height = 300, x = 410, y = 0, title = "a-t graph", xtitle = 'time (s)', ytitle = 'acceleration (m/s^2)', ymax = 6, ymin = -6, xmax = 20)
at = gcurve(graph = gd_at, color = color.red)
#labels
label1 = label()
label2 = label()
label3 = label()

#animation
while True:
    rate(100)
    t+=0.1
    #calculate    
    x = vector(A*cos(w*t),0,0)
    v = -1*A*w*sin(w*t)
    a = -1*A*w*w*cos(w*t)
    
    #moving objects
    ball.pos = x
    spring.axis.x = ball.pos.x-7

    #ploting
    xt.plot(t,ball.pos.x)
    vt.plot(t,v)
    at.plot(t,a)

    #labeling
    label1.pos = spring.pos + vector(-2,-2,0)
    label1.text = 'time : %.2f s' %t

    label2.pos = spring.pos + vector(-2,-3,0)
    label2.text = 'velocity : %.2f m/s' %v

    label3.pos = spring.pos + vector(-2,-4,0)
    label3.text = 'acceleration : %.2f m/s^2' %a