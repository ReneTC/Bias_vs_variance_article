import numpy as np
import matplotlib.pyplot as plt
exec(open('/home/renec/Drive/Higgsino/ASSETS/flotplot.py').read())
from scipy.optimize import curve_fit
import matplotlib.animation as animation

np.random.seed(5)

# %% construct true function to fit


y_true = np.poly1d([0.2,1.5,1])
x = np.linspace(0,10,100)

# %% pick 10 samples to train
n_train_size = 8
noise_size = 3
x_train = np.sort(np.random.choice(x,n_train_size))
y_train = y_true(x_train)+ noise_size * np.random.normal(size=n_train_size)

# %% pick 10 samples to val
n_val_size = 4

x_val = np.sort(np.random.choice(x,n_val_size))
y_val = y_true(x_val)+ noise_size * np.random.normal(size=n_val_size)

# plt.ylim([0,40])
# plt.plot(x,y_true(x),color="k")
# plt.plot(x_train,y_train,'ok')

# %% all fit show some
all_fit_coef = []

for i in range(0,n_train_size):
    get_fit = np.polyfit(x_train,y_train,i)
    get_func = np.poly1d(get_fit).c
    all_fit_coef.append(get_func)

# make all
all_fit_coef_zero = []
for fit in all_fit_coef:
    zeros = np.zeros(n_train_size)
    fit = np.r_[zeros[0:n_train_size-len(fit)], fit]
    all_fit_coef_zero.append(fit)

def get_av_fitted(deg):
    lower = int(np.floor(deg))
    upper = int(np.ceil(deg))

    return np.average([all_fit_coef_zero[lower], all_fit_coef_zero[upper]],weights=[(upper-deg),1-(upper-deg)],axis=0)
