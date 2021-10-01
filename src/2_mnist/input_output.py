from sg import *
exec(animation_code)
from phymin import *
exec(open("/home/renec/Drive/Higgsino/new_project/vid_files/0_draw/server.py").read())


pc = server(0,0)
def animation():
    scene(1920,1080,frames = 100)
    translate(-100,100)
    text(interpolate(-300,0,20),0, "Input", font=fontn,size = 63)
    text(interpolate(-5,300,60),0, "Output", font=fontn,size = 63)
    pc.draw()

    # image(interpolate(-300,0,0),100,"/home/renec/Drive/Higgsino/new_project/vid_files/0_backup/MNIST/7/59856.jpg",width=150,height=150)
    cube(-400,-100,350,300,alpha=interpolate(1,0,0),color="#ffffff")
    cube(300,-100,350,300,alpha=interpolate(0,1,80),color="#ffffff")
animate(filename='input_output')
# to_gif('input_output')

# animation()
# show(inline=True)
