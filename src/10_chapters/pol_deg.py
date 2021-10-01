from sg import *
exec(animation_code)
from phymin import *
vals = np.around(np.linspace(0,5,500),2)
def animation():
    scene(1920,500,frames = 500,alpha=0)
    text(-800,0,"Polynomial degree: " + str(vals[the_scene.frame]),alpha=interpolate(0,1,0),font=fontb,size=130,color="#000000")
    # cube(-2000,-200,30000,30000,alpha=interpolate(1,0,50,duration=50))
# show_animation(inline=True,frame=20)
animate(filename='pol_degree')
