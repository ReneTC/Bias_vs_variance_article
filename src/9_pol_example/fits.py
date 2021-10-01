exec(open('main.py').read())

# %% overview of training
fig, ax = plt.subplots( nrows=1, ncols=1 )
plt.ylim([0,40])

plt.plot(x,y_true(x),color="k")
plt.plot(x_train,y_train,'ok')


# %% interpolation example
fig, ax = plt.subplots( nrows=1, ncols=1 )
plt.ylim([0,40])
plt.plot(x,y_true(x),color="k")
plt.plot(x_train,y_train,'ok')
plt.plot(x,np.poly1d(get_av_fitted(3))(x),grey2)
plt.plot(x,np.poly1d(get_av_fitted(4))(x),grey2)
for i in range(1,10):
    plt.plot(x,np.poly1d(get_av_fitted(i/10+3))(x),grey2,alpha=0.5)


# %% bias variance calc
fig, ax = plt.subplots( nrows=1, ncols=1 )
plt.ylim([0,40])
plt.plot(x,y_true(x),color="k")
# plt.plot(x_train,y_train,'ok')
plt.plot(x_val,y_val,'or')

# dumb
plt.plot(x,np.poly1d(get_av_fitted(0))(x),get_color(0.7))
plt.plot(x_val,np.poly1d(get_av_fitted(0))(x_val),'o',color=get_color(0.7))

# too clever
plt.plot(x,np.poly1d(get_av_fitted(5))(x),get_color(0.9))
plt.plot(x_val,np.poly1d(get_av_fitted(5))(x_val),'o',color=get_color(0.9))

expeted = np.mean(y_true(x_val))
bias1 = np.mean(np.poly1d(get_av_fitted(0))(x_val))-expeted
variance1 = np.var(np.poly1d(get_av_fitted(0))(x_val))

bias2 = np.mean(np.poly1d(get_av_fitted(5))(x_val))-expeted
variance2 = np.var(np.poly1d(get_av_fitted(5))(x_val))

plt.text(4,25,"bias: "+str(np.around(bias1**2)) + ", var: "+str(np.around(variance1)),color=get_color(0.7))
plt.text(4,30,"bias: "+str(np.around(bias2**2)) + ", var: "+str(np.around(variance2)),color=get_color(0.9))

# plt.savefig('over_under.png')


# %% animation one draw true function
# j = 0
# import matplotlib
# matplotlib.use('Agg')
# for i in range(0,len(x)):
#     fig, ax = plt.subplots( nrows=1, ncols=1 )
#     plt.ylim([0,40])
#     plt.xlim([0,10])
#     plt.xlabel("Hours in sun")
#     plt.ylabel("Cell damage")
#     plt.plot(x[0:i+1],y_true(x)[0:i+1],color='k')
#     plt.tight_layout()
#     plt.savefig('draw_true_fuction/draw_true_fuction'+str(j).zfill(3)+'.png')
#     j = j+1

# %% animation pick data
# values = np.linspace(1,0,100)
# j = 0
# import matplotlib
# matplotlib.use('Agg')
# for i in range(0,100):
#     fig, ax = plt.subplots( nrows=1, ncols=1 )
#     plt.ylim([0,40])
#     plt.xlim([0,10])
#     plt.xlabel("Hours in sun")
#     plt.ylabel("Cell damage")
#     plt.plot(x,y_true(x),color="k")
#     plt.plot(x_train,y_train,'ok')
#     plt.plot(x_val,y_val,'o',color = get_color(0.5),alpha = 1)
#     plt.plot(x_val,y_val,'ok',alpha = values[i])
#     plt.tight_layout()
#     plt.savefig('draw_data_points/draw_data_points'+str(j).zfill(3)+'.png')
#     j = j+1

# %% animation fit 2  poly
# j = 0
# def ReLU(x):
#     return x * (x > 0)
#
# import matplotlib
# matplotlib.use('Agg')
# for i in range(0,200):
#     fig, ax = plt.subplots( nrows=1, ncols=1 )
#     plt.ylim([0,40])
#     plt.xlim([0,10])
#     plt.xlabel("Hours in sun")
#     plt.ylabel("Cell damage")
#     plt.plot(x,y_true(x),color="k")
#     plt.plot(x_train,y_train,'ok')
#     plt.plot(x[0:ReLU(i-100)+1],np.poly1d(get_av_fitted(5))(x)[0:ReLU(i-100)+1],get_color(0.9))
#     plt.plot(x[0:i+1],np.poly1d(get_av_fitted(0))(x)[0:i+1],get_color(0.7))
#     plt.tight_layout()
#     plt.savefig('fitting_2_poly/fitting_2_poly'+str(j).zfill(3)+'.png')
#     j = j+1

# %% add train set
# fig, ax = plt.subplots( nrows=1, ncols=1 )
# plt.ylim([0,40])
# plt.xlim([0,10])
# plt.xlabel("Hours in sun")
# plt.ylabel("Cell damage")
# plt.plot(x,y_true(x),color="k")
# plt.plot(x_train,y_train,'ok')
# plt.plot(x,np.poly1d(get_av_fitted(5))(x),get_color(0.9))
# plt.plot(x,np.poly1d(get_av_fitted(0))(x),get_color(0.7))
# plt.plot(x_val,y_val,'o',color = get_color(0.5),alpha = 1)
# # plt.legend(["True relation","Training set ","Test set","5 degree fit","0 degree fit"],loc='upper center',bbox_to_anchor=(0.5, 0.5),ncol=3, fancybox=True, shadow=True)
# plt.tight_layout()
# plt.savefig("with_test.png")


import matplotlib
fig, ax = plt.subplots( nrows=1, ncols=1 )
plt.ylim([0,40])
plt.xlim([0,10])
plt.xlabel("Hours in sun")
plt.ylabel("Cell damage")
plt.plot(x_val,y_val,'o',color = get_color(0.5),alpha = 1)
# plt.plot(x,y_true(x),color="k")
plt.plot(x_train,y_train,'ok')
plt.plot(x,np.poly1d(get_av_fitted(5))(x),get_color(0.9))
# plt.plot(x,np.poly1d(get_av_fitted(0))(x),get_color(0.7))
plt.tight_layout()
plt.savefig('Hej2.png')
