from sg import *
exec(animation_code)
from phymin import *
vals = np.around(np.linspace(0,5,500),2)
def animation():
    scene(1920,500,frames = 60,alpha=0)
    # text(-800,0,"Polynomial degree: " + str(vals[the_scene.frame]),alpha=interpolate(0,1,0),font=fontb,size=130,color="#000000")
    image(-800,0,"/home/renec/Drive/Higgsino/new_project/vid_files/3_bias_variance_decompose/src/n_poly.png")
show_animation(inline=True,frame=20)
# animate(filename='pol_degree')
