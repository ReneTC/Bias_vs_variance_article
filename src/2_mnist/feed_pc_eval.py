from sg import *
exec(animation_code)
from phymin import *
exec(open("/home/renec/Drive/Higgsino/new_project/vid_files/0_draw/server.py").read())


pc = server(0,0)
def animation():
    scene(1920,1080,frames = 100)

    text(-350,400,"Training",font=fontb,size=150,alpha=interpolate(1,0,40))
    text(-320,400,"Testing",font=fontb,size=150,alpha=interpolate(0,1,40))
    translate(-100,100)
    push()
    translate(interpolate(-300,50,20),0)
    rotate(-45)

    # text(-100,0, "Dataset", font=fontn,size = interpolate(63,0,20))
    pop()



    cube(-400,-100,350,300,alpha=interpolate(1,0,0),color="#ffffff")
    # cube(300,-100,350,300,alpha=interpolate(0,1,80),color="#ffffff")
    for i in range(0,4):
        cube(interpolate(-300,0,i*10),0,50,50,color=grey2,alpha=interpolate(0,1,i*10))

    for i in range(0,10):
        cube(interpolate(-300,0,i*10+40),0,50,50,color=get_color(0.5),alpha=interpolate(0,1,i*10+40))

    push()
    scale(1.2,1.2)
    pc.draw()
    pop
# show_animation(inline=True)
animate(filename='eval')
# to_gif('input_output')

# animation()
# show(inline=True)
