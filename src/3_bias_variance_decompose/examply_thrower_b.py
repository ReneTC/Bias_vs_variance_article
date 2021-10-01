from sg import *
exec(animation_code)
from phymin import *
import numpy as np
np.random.seed(10)
rand =np.random.normal(0, 1, size=(1, 10))
rand = rand[0]
def animation():
    scene(1920,1080,frames = 70)
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

    size = 50
    # thrower
    circle(700+rand[0]*size,0,interpolate(0,10,0),color=get_color(0.7))
    circle(700+rand[1]*size,0,interpolate(0,10,10),color=get_color(0.7))
    circle(700+rand[2]*size,0,interpolate(0,10,20),color=get_color(0.7))
    circle(700+rand[3]*size,0,interpolate(0,10,30),color=get_color(0.7))
    circle(700+rand[4]*size,0,interpolate(0,10,40),color=get_color(0.7))
    circle(700+rand[5]*size,0,interpolate(0,10,50),color=get_color(0.7))

show_animation(inline=True,frame=0)
animate('thrower_bias')
to_gif('thrower_bias')
