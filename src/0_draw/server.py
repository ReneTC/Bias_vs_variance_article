from phymin import *
class server:
    def __init__(self,x,y,**kwargs):
        self.x = x
        self.y = y

    def draw(self):
        x = self.x
        y = self.y
        cube(x+0,y-200,200,400,color=grey1)
        cube(x+10,y+120,180,50,color=grey2)
        cube(x+10,y+120-70,180,50,color=grey2)
        cube(x+10,y+120-2*70,180,50,color=grey2)

        # outline
        cube_path(x+0,y-200,x+200,y+400,color = grey2)
        frame = the_scene.frame
        # dots
        green = get_color(0.4)
        # circle(x+50,y-50,10,color = hold_switch(grey2,boolean_pulse(4,frame,on_val=green,off_val=grey2,offset=0),40,frame))
        # circle(x+50+30,y-50,10,color = hold_switch(grey2,boolean_pulse(4,frame,on_val=green,off_val=grey2,offset=1),40,frame))
        # circle(x+50+2*30,y-50,10,color = hold_switch(grey2,boolean_pulse(4,frame,on_val=green,off_val=grey2,offset=2),40,frame))
        # circle(x+50+3*30,y-50,10,color = hold_switch(grey2,boolean_pulse(4,frame,on_val=green,off_val=grey2,offset=3),40,frame))
        circle(x+50,y-50,10,color = boolean_pulse(4,frame,on_val=green,off_val=grey2,offset=0))
        circle(x+50+30,y-50,10,color = boolean_pulse(4,frame,on_val=green,off_val=grey2,offset=1))
        circle(x+50+2*30,y-50,10,color = boolean_pulse(4,frame,on_val=green,off_val=grey2,offset=2))
        circle(x+50+3*30,y-50,10,color = boolean_pulse(4,frame,on_val=green,off_val=grey2,offset=3))

from sg import *
from phymin import *
# scene(1000,500)
# pc = server(0,0)
# pc.draw(start = 0, stop = 10)
# show(inline=True)
