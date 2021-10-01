exec(open('main.py').read())
import matplotlib
# matplotlib.use('Agg')
the_range = np.linspace(0,1,200)
the_error = np.exp(-3*the_range)
x = the_range-0.5
the_val_error = np.exp(10*x**2+0*x-1)

the_error
j = 0

# %%
for i in range(0,len(the_range)):
    fig, ax = plt.subplots( nrows=1, ncols=1 )
    plt.xlim([0,1])
    # ax.set_yscale('log')
    plt.xlabel("Complexity")
    plt.ylabel("Error")
    plt.ylim([0,1])

    plt.plot(the_range[0:i+1],the_error[0:i+1],grey2)
    plt.tight_layout()
    plt.savefig('train_error_graph_theory/train_error_graph_theory'+str(j).zfill(3)+'.png')
    j = j+1
