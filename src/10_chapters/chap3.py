from sg import *
exec(animation_code)
from phymin import *

def animation():
    scene(1920,1080,frames = 140)
    translate(0,-100)
    # rotate(-frame/40)
    text(interpolate(-600,-800,-30,duration=100),0, "Chapter 3", font=fontb,size = 250)
    text(interpolate(-780-200,-780,-30,duration=100),-200, "Complexity trade-off", font=fonti,size = 110,color=grey3)
    # text(-780,-350, "Polynomial fit, regularization", font=fontn,size = 50,color=grey3)
    # cube(-800,-360,interpolate(400,0,20),50,color='#000000')
    # cube(-290,-360,interpolate(200,0,40),50,color='#000000')
    # cube(-80,-360,interpolate(210,0,60),50,color='#000000')
    # cube(150,-360,interpolate(370,0,80),50,color='#000000')
# show_animation(inline=True)
animate(filename='chap3_')
# to_gif('dataset')
