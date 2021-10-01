from sg import *
exec(animation_code)
from phymin import *
def animation():
    scene(1920,300,frames = 60,alpha=0)
    scale(interpolate(1,0,45),interpolate(1,0,40))
    text(interpolate(-1900,-800,0),0,".. is too variant  ",alpha=interpolate(0,1,0),font=fonti,size=80,color="#000000")
    # cube(-2000,-200,30000,30000,alpha=interpolate(1,0,50,duration=50))
# show_animation(inline=True,frame=20)
animate(filename='is_var')
