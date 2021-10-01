from sg import *
exec(animation_code)
from phymin import *

scene(1920,1020,frames = 150)
scale2=0.45
image(-1000,530,"/home/renec/Drive/Higgsino/new_project/vid_files/0_draw/classroom.jpg",width=int(6000*scale2),height=int(3390*scale2))
rotate(20)
translate(-170,-200)
scale(2,2)
push()
translate(-200,-100)
scale(0.2,0.2)
image(0,0,'/home/renec/Drive/Higgsino/new_project/vid_files/0_draw/speech.png')
pop()
text(-100,30, "kids remember: ",font=fonti)
translate(-100,30)
text(110,0, "= 9", font=fontn,size = 45)
image(35,40,"/home/renec/Drive/Higgsino/new_project/vid_files/0_draw/MNIST/9/59927.jpg",width=60,height=60)
save("classroom.png")
show(inline=True)
