from sg import *
exec(animation_code)
from phymin import *

def animation():
    scene(1920,1080,frames = 100)
    text(interpolate(-1880,-800,0),0, "SoME1", font=fontb,size = 250)
    text(interpolate(-2880,-800,10),-200, "Summer of Math Exposition #1", font=fonti,size = 120,color=grey3)

    cube(300,-50,100,interpolate(0,100,20),color='#ad7f51',alpha=interpolate(0,1,20))
    cube(300,75,interpolate(0,100,30),100,color='#ad7f51',alpha=interpolate(0,1,30))
    cube(420,0,interpolate(0,100,40),100,color='#ad7f51',alpha=interpolate(0,1,40))
    cube(650,0,interpolate(0,100,50),100,color='#6ab0ca',alpha=interpolate(0,1,50))
# show_animation(inline=True)
animate(filename='3b1b')
# to_gif('dataset')
