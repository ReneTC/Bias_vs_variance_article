from sg import *
exec(animation_code)
from phymin import *
exec(open("/home/renec/Drive/Higgsino/new_project/vid_files/0_draw/server.py").read())


pc = server(0,0)
def animation():
    scene(1920,1080,frames = 130)
    translate(-100,100)


    # w1
    # image(interpolate(-300,0,20),100,"/home/renec/Drive/Higgsino/new_project/vid_files/0_draw/MNIST/7/59856.jpg",width=150,height=150)
    # text(interpolate(-5,300,60),0, "3", font=fontn,size = 90)

    # w2
    # image(interpolate(-300,0,20),100,"/home/renec/Drive/Higgsino/new_project/vid_files/0_draw/MNIST/1/59836.jpg",width=150,height=150)
    # text(interpolate(-5,300,60),0, "9", font=fontn,size = 90)

    # w3
    # image(interpolate(-300,0,20),100,"/home/renec/Drive/Higgsino/new_project/vid_files/0_draw/MNIST/5/59923.jpg",width=150,height=150)
    # text(interpolate(-5,300,60),0, "8", font=fontn,size = 90)

    # r1
    image(interpolate(-300,0,20),100,"/home/renec/Drive/Higgsino/new_project/vid_files/0_draw/MNIST/4/59893.jpg",width=150,height=150)
    text(interpolate(-5,300,60),0, "4", font=fontn,size = 90)


    pc.draw()
    when = 100
    translate(550,interpolate(-900,-100,0+when))
    rotate(interpolate(80,-30,0+when))
    push()
    translate(-350,-340)
    # image(0,0,"/home/renec/Drive/Higgsino/new_project/vid_files/0_draw/baseball-bat.png")
    pop()

animate(filename='r1')
# to_gif('r1')

# animation()
# show(inline=True)
