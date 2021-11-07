exec(open('main.py').read())
import matplotlib
matplotlib.use('Agg')
the_error = []
j = 0
the_range = np.linspace(0,5,500)
the_color = np.linspace(0.7,0.9,500)
for i in the_range:
    fig, ax = plt.subplots( nrows=1, ncols=1 )
    plt.ylim([0,40])
    plt.xlim([0,10])
    plt.xlabel("Hours in sun")
    plt.ylabel("Cell damage")
    plt.plot(x_train,y_train,'ok')
    col = get_color(the_color[j])
    plt.plot(x,np.poly1d(get_av_fitted(i))(x),color = col)
    error = np.sum(((y_train - np.poly1d(get_av_fitted(i))(x_train))**2))
    the_error.append(error)

    plt.title("Polynomial degree: " + str(np.format_float_positional(i,precision=3)))
    plt.savefig('train_error_02/train_error_02'+str(j).zfill(3)+'.png', bbox_inches='tight')
    j = j+1
j = 0
# for i in range(0,len(the_range)):
#     fig, ax = plt.subplots( nrows=1, ncols=1 )
#     plt.xlim([0,7])
#     ax.set_yscale('log')
#     plt.ylim([0,1000])
#     plt.plot(the_range[0:i+1],the_error[0:i+1],grey2,alpha=0.5)
#     plt.savefig('train_error_graph/train_error_graph'+str(j).zfill(3)+'.png', bbox_inches='tight')
#     j = j+1
# to_gif('train_error_theory')
