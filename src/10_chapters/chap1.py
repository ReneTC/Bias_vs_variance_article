from sg import *
exec(animation_code)
from phymin import *

def animation():
    scene(1920,1080,frames = 140)
    translate(0,-100)
    # rotate(-frame/40)
    text(interpolate(-600,-800,-30,duration=100),0, "Chapter 1", font=fontb,size = 250)
    text(interpolate(-780-200,-780,-30,duration=100),-200, "Machine Learning theory", font=fonti,size = 120,color=grey3)
    text(-780,-350, "Supervised learning, dataset, training, generalisability", font=fontn,size = 50,color=grey3)
    cube(-800,-360,interpolate(500,0,20),50,color='#ffffff')
    cube(-290,-360,interpolate(200,0,40),50,color='#ffffff')
    cube(-80,-360,interpolate(210,0,60),50,color='#ffffff')
    cube(150,-360,interpolate(370,0,80),50,color='#ffffff')
# show_animation(inline=True)
animate(filename='chap1_')
# to_gif('dataset')
