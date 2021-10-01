from sg import *
exec(animation_code)
from phymin import *
import numpy as np


class arrow:
    def __init__(self,x,y,**kwargs):
        self.x = x
        self.y = y
        self.scale = 50

    def draw(self):
        push()
        s = interpolate(0,1,1)
        s1 = interpolate(1,0,100)
        translate(np.sin(the_scene.frame/10)*100,0)
        translate(interpolate(-800,0,0),0)
        scale(1,s)
        scale(s1,s1)
        vertices([[self.x-self.scale,self.y-self.scale],[self.x-self.scale,self.y+self.scale],[self.x,self.y]])
        cube(self.x-300,-20,300-self.scale,40)
        pop()

def animation():
    scene(800,800,frames = 120,alpha=0)

    a = arrow(0,0)
    a.draw()


# show_animation(inline=True,frame=0)
animate('arrow')
