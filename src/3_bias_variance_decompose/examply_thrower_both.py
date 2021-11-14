from sg import *
exec(animation_code)
from phymin import *
import numpy as np
np.random.seed(15)
rand =np.random.normal(0, 1, size=(1, 10))
rand = rand[0]
def animation():
    scene(1920,1080,frames = 90)
    # number line
    translate(-670,200)
    cube(-0,-5,1400,10)
    for i in range(1,14):
        cube(-0+i*100+10,-10, 5,16,)
        text(-0+i*100,-70, str(i), font=fontn,size = 50)

    # arrow
    displ_x = 1400
    displ_y = 0
    vertices([(0+displ_x,-25+displ_y),(0+displ_x,25+displ_y),(50+displ_x,0+displ_y)])
    # items on numberline

    # target
    circle(1000+15,0,40,color=get_color(0))
    circle(1000+15,0,30,color='#ffffff')
    circle(1000+15,0,20,color=get_color(0))
    circle(1000+15,0,10,color='#ffffff')

    size = interpolate(0,200,20)
    bias = interpolate(0,-80,40)
    # thrower
    col = 0.9
    x0 = 1015+rand[0]*size+bias
    x1 = 1015+rand[1]*size+bias
    x2 = 1015+rand[2]*size+bias
    x3 = 1015+rand[3]*size+bias
    x4 = 1015+rand[4]*size+bias
    x5 = 1015+rand[5]*size+bias
    x6 = 1015+rand[6]*size+bias
    x7 = 1015+rand[7]*size+bias
    x8 = 1015+rand[8]*size+bias
    circle(x1,0,interpolate(0,15,0),color=grey3)
    circle(x1,0,interpolate(0,15,0),color=grey3)
    circle(x2,0,interpolate(0,15,0),color=grey3)
    circle(x3,0,interpolate(0,15,0),color=grey3)
    circle(x4,0,interpolate(0,15,0),color=grey3)
    circle(x5,0,interpolate(0,15,0),color=grey3)
    circle(x6,0,interpolate(0,15,0),color=grey3)
    circle(x7,0,interpolate(0,15,0),color=grey3)
    circle(x8,0,interpolate(0,15,0),color=grey3)

    var = np.var([x0,x1,x2,x3,x4,x5,x6,x7,x8])/100
    bias = np.mean([x0,x1,x2,x3,x4,x5,x6,x7,x8])-1015
    text(0,100,"var : "+str(np.around(var)),size=100,font=fontn,color=get_color(0.9))
    text(0,200,"bias: "+str(np.around(bias)),size=100,font=fontn,color=get_color(0.7))

show_animation(inline=True,frame=0)
animate('thrower_both2')
to_gif('thrower_both2')
