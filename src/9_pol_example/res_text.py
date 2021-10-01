
from sg import *
exec(animation_code)
from phymin import *
import numpy as np

degree = np.linspace(0,2,200)
scene(1980,500,frames = 200)
translate(-400,-80)
image(-100,70,'/home/renec/Drive/Higgsino/new_project/vid_files/3_bias_variance_decompose/src/0_poly.png')

text(-500,0,"Error of",font=fontn, size = 80)
text(-500,-100,"Bias: 51",font=fontn, size = 80)
text(-500,-200,"Var : 0",font=fontn, size = 80)

# image(-100,70,'/home/renec/Drive/Higgsino/new_project/vid_files/3_bias_variance_decompose/src/5_poly.png')
# text(-500,0,"Error of",font=fontn, size = 80)
# text(-500,-100,"Bias: 3",font=fontn, size = 80)
# text(-500,-200,"Var : 120",font=fontn, size = 80)

# animate('res_text')
# show_animation(inline=True)
save("0_pol.png")
