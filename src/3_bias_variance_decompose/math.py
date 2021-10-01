from sg import *
exec(animation_code)
from phymin import *



def animation():
    scene(1920,200,frames = 160)
    # latex(r'f(x) = a_n x^n + \ldots + a_2 x^2 + a_1 x + a_0','src/n_poly.png')
    # latex(r'y = 0.2 x^2 + 1.5 x + 1','src/poly_true.png')
    # latex(r'y = a_2 x^2 + a_1 x + a_0','src/poly_second.png')
    # latex(r'\mathrm{Bias}(\hat{y}) = y - E[\hat{y}]','src/bias.png')
    # latex(r'\mathrm{Error} = \mathrm{Bias}(\hat{y})^2+ \mathrm{Var}(\hat{y})+\mathrm{Noise}','src/e.png')
    image(-700,50,'/home/renec/Drive/Higgsino/new_project/vid_files/3_bias_variance_decompose/src/e.png')
    cube(-700,-50,320,100,alpha=interpolate(1,0,0),color='#ffffff')
    cube(-360,-70,320,120,alpha=interpolate(1,0,30),color='#ffffff')
    cube(-20,-70,380,120,alpha=interpolate(1,0,60),color='#ffffff')
    cube(360,-70,400,120,alpha=interpolate(1,0,90),color='#ffffff')

# show_animation(inline=True,frame=70)
# animate('totale')
# show(inline=True)
latex(r'\hat{y} = a_5 x^5 + \ldots + a_2 x^2 + a_1 x + a_0','src/5_poly.png',color=get_color(0.9))
latex(r'\hat{y} = a_0','src/0_poly.png',color=get_color(0.7))
latex(r'\approx y','src/apprex.png')
