import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# params = {'legend.fontsize': '12',
#           'axes.labelsize': '12',
#           'axes.titlesize': '15',
#           'xtick.labelsize': '12',
#           'ytick.labelsize': '12',
#           'legend.numpoints': '1',
#           'legend.edgecolor': '0.2',
#           'legend.fancybox': False,
#           'text.latex.preamble' : r'\usepackage{amsmath}',
#           'axes.spines.right': False,
#           'axes.spines.top': False,
#           'figure.figsize'      : [10,4],
#           'figure.dpi': 150,
#           'legend.frameon': True,
#           }
#
# plt.rcParams.update(params)
# plt.rc('text', usetex=True)
# plt.rc('font', family='serif')

def get_color(val):
    cmap = plt.cm.get_cmap('gist_rainbow')
    rgba = cmap(val)
    hex_code = matplotlib.colors.to_hex(rgba, keep_alpha=False)
    return hex_code

grey1 = "#dadada"
grey2 = "#909090"
grey3 = "#4f4f4f"
white = "#000000"
black = "#ffffff"


fontb = "/home/renec/anaconda3/lib/python3.7/site-packages/phymin/fonts/cmunbi.ttf"
fonti = "/home/renec/anaconda3/lib/python3.7/site-packages/phymin/fonts/cmunti.ttf"
fontn = "/home/renec/anaconda3/lib/python3.7/site-packages/phymin/fonts/cmunui.ttf"


def word_cutter(word, start_frame = 0):
    res = []
    word_array = word.split(" ")
    word_len = len(word_array)
    start_frame = 1
    for i in range(0,frames):
        if i < start_frame:
            res.append(["hej"])
        elif i >= start_frame and i <= start_frame+word_len:
            res.append(word_array[0:i])
        else:
            res.append(word_array)
    return res

def to_gif(filename=None):
    '''
    creates a gif png's exists. saver has to have been called
    '''
    import pathlib
    from sys import argv
    import os
    from pygifsicle import optimize
    import imageio
    if filename == None:
        filename = os.path.basename(os.path.splitext(argv[0])[0])
    path = pathlib.Path().absolute()
    isfile = os.path.join(path,filename)

    if not os.path.exists(isfile):
        assert("error files not rendered - folder does not exists")


    import glob
    fp_in = os.path.join(path,filename, "*.png")
    fp_out = os.path.join(path,filename,str(filename) + ".gif")

    img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in))]
    # img.save(fp=fp_out, format='GIF', append_images=imgs,
    #          save_all=True, duration=40, loop=0)
    imageio.mimsave(fp_out, imgs, fps=20)

    optimize(fp_out)


import io
from PIL import Image, ImageChops

def latex(tex,path,color='#000000',size = 100):
    # buf = io.BytesIO()
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.axis('off')
    plt.text(0.05, 0.5, f'${tex}$', size=size, color = color)
    plt.savefig(path, format='png',bbox_inches = 'tight',
    pad_inches = 0)
    plt.close()

    # crop
    im = Image.open(path)
    im.size  # (364, 471)
    im.getbbox()  # (64, 89, 278, 267)
    im2 = im.crop(im.getbbox())
    im2.size  # (214, 178)
    im2.save(path)

# latex(r'\frac{x}{y^2}')

# gif to mp4
# ffmpeg -i animated.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" video.mp4
