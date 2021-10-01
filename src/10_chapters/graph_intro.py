from sg import *
exec(animation_code)
from phymin import *

def animation():
    scene(1920,1080,frames = 20,alpha=0)
    cube(-800,-360,interpolate(1800,0,0),200,color='#ffffff')
    cube(-950,-300,180,interpolate(800,0,0),color='#ffffff')
show_animation(inline=True)

animate(filename='graph_intro')
# to_gif('dataset')
