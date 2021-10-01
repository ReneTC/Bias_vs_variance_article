exec(open('main.py').read())
import matplotlib
matplotlib.use('Agg')
the_error = []
the_bias = []
the_variance = []
the_range = np.linspace(0,5,500)
for i in the_range:
    error = np.sum(((y_val - np.poly1d(get_av_fitted(i))(x_val))**2))
    the_error.append(error)

    expeted = np.mean(y_true(x_val))
    bias = np.mean(np.poly1d(get_av_fitted(i))(x_val)) - expeted
    variance = np.var(np.poly1d(get_av_fitted(i))(x_val))

    the_bias.append(bias)
    the_variance.append(variance)



j=0
for i in range(0,len(the_range)):
    fig, ax = plt.subplots( nrows=1, ncols=1 )
    plt.xlim([0,5])
    # ax.set_yscale('log')
    plt.xlabel("Complexity [Polynomial degree]")
    plt.ylabel("Error")
    plt.ylim([0,125])
    plt.plot(the_range[0:i+1],np.power(the_bias,2)[0:i+1],color=get_color(0.7),label = r"Bias²")
    plt.plot(the_range[0:i+1],the_variance[0:i+1],color=get_color(0.9),label = "Variance")
    plt.plot(the_range[0:i+1],np.power(the_bias,2)[0:i+1]+the_variance[0:i+1] + 10,color=get_color(0.5),label = "Total Error")
    plt.tight_layout()
    plt.savefig('res/res'+str(j).zfill(3)+'.png')
    j = j+1
