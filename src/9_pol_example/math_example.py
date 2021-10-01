
from sg import *
exec(animation_code)
from phymin import *
import numpy as np

degree = np.linspace(0,2,200)
def animation():
    scene(1980,300,frames = 200)
    translate(0,-50)
    image(-200,0,'/home/renec/Drive/Higgsino/new_project/vid_files/3_bias_variance_decompose/src/poly_second.png')

    cube(265,-120,250,170,alpha=1-degree[the_scene.frame],color='#ffffff')
    cube(-20,-120,280,170,alpha=2-degree[the_scene.frame],color='#ffffff')
show_animation(inline=True)
animate('math_example')
# to_gif('math_example')
