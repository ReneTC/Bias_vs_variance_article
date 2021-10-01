from sg import *
exec(animation_code)
from phymin import *
p = ["Sven Ostertag", "Bjartur Mortensen", "Martin Vasilev", "Kale Crosbie", "Henrik McDonald","1x anonymous"]
def animation():
    scene(1920,1080,frames = 100,alpha=0)
    image(-1000,800,"/home/renec/Drive/Higgsino/ASSETS/Higgsino/assets/coverbig.JPG")
    text(interpolate(-1900,-900,0),300,"Higgsino Patreons",alpha=interpolate(0,1,0),font=fontb,size=100,color="#ffffff")
    j = 0
    for i in p:
        text(interpolate(-1900,-900,j*10+20),150-100*j,i,font=fonti,color = get_color(j/6),size=80)
        j += 1
    # cube(-2000,-200,30000,30000,alpha=interpolate(1,0,50,duration=50))
# show_animation(inline=True,frame=100)
animate(filename='patreon')
