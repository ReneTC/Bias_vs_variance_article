from sg import *
exec(animation_code)
from phymin import *

def animation():
    scene(1920,1080,frames = 100)
    translate(-200,-100)
    text(150,200, "Dataset", font=fontn,size = 90,alpha=interpolate(1,0,10))

    push()
    translate(interpolate(0,-650,10),0)
    text(0,200, "Training set", font=fontn,size = 90,alpha=interpolate(0,1,10))
    for i in range(0,8):
        for j in range(0,10):
            cube(0+70*i,100-70*j,50,50,color=grey2)
    pop()
    translate(interpolate(0,200,10),0)
    text(450,200, "Test set", font=fontn,size = 90,alpha=interpolate(0,1,10))
    for i in range(0,2):
        for j in range(0,10):
            cube(560+70*i,100-70*j,50,50,color=interpolate_color(grey2,get_color(0.5),20))

animate(filename='data_set_split')
# to_gif('data_set_split')
