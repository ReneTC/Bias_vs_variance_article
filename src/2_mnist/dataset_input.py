from sg import *
exec(animation_code)
from phymin import *

def animation():
    scene(1920,1080,frames = 150)
    translate(-100,0)
    translate(-700,-300)
    text(0,0, "Data point", font=fontn,size = 90,alpha=interpolate(0,1,0))
    text(0,-100, "(Input, Output)", font=fontn,size = 45,alpha=interpolate(0,1,20))

    text(0,-200, "( "+" "+""+" "+""+" "+""+" "+", 9)", font=fontn,size = 45,alpha=interpolate(0,1,40))
    image(35,-160,"/home/renec/Drive/Higgsino/new_project/vid_files/0_draw/MNIST/9/59927.jpg",width=60,height=60,alpha=interpolate(0,1,40))

    text(180,-200, " = ", font=fontn,size = 45,alpha=interpolate(0,1,60))
    cube(250,-215,50,50,color=grey2,alpha=interpolate(0,1,60))


    text(900,0, "Dataset", font=fontn,size = 90,alpha=interpolate(0,1,80))
    for i in range(0,10):
        for j in range(0,10):
            cube(900+70*i,-100-70*j,50,50,color=grey2,alpha=interpolate(0,1,100+i+j))
# show_animation(inline=True,frame=150)
animate(filename='dataset')
# to_gif('dataset')
