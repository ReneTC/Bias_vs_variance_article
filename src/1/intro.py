from sg import *
exec(animation_code)
from phymin import *

t1 = 'Bias vs Variance;'
t2 = 'Why being too smart is dumb'


def word_cutter(word, start_frame = 0):
    res = []
    word_array = word.split(" ")
    word_len = len(word_array)
    for i in range(0,frames):
        if i <= start_frame:
            res.append(" ")
        else:
            res.append(" ".join(word_array[0:i-start_frame]))
    return res





# %%
def animation():
    scene(1920,1080,frames =10)
    t1_test = word_cutter(t1,start_frame=0)
    t2_test = word_cutter(t2,start_frame=3)

    text(-850,100, t1_test[frame], font=fontn,size=200)
    text(-550,-0, t2_test[frame], font=fonti,size=80)

animate(filename='animation')
