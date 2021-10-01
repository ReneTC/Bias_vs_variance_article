from sg import *
exec(animation_code)
from phymin import *


def animation():
    scene(1920,1080,frames = 100)
    # number line
    translate(-670,200)
    cube(-0,-5,interpolate(0,1400,0),10)
    for i in range(1,14):
        cube(-0+i*100+10,-10, 5,16,alpha = interpolate(0,1,8+i))
        text(-0+i*100,-70, str(i), font=fontn,size = 50,alpha = interpolate(0,1,15+i*2))

    # arrow
    displ_x = interpolate(0,1400,0)
    displ_y = 0
    vertices([(0+displ_x,-25+displ_y),(0+displ_x,25+displ_y),(50+displ_x,0+displ_y)],alpha=interpolate(0,1,0))
    # items on numberline

    # target
    circle(1000+15,0,interpolate(0,40,50),color=get_color(0))
    circle(1000+15,0,interpolate(0,30,55),color='#ffffff')
    circle(1000+15,0,interpolate(0,20,60),color=get_color(0))
    circle(1000+15,0,interpolate(0,10,65),color='#ffffff')


show_animation(inline=True,frame=0)
animate('intro')
# to_gif('intro')
