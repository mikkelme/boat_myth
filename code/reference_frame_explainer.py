from simulator import *
import matplotlib.pyplot as plt

import seaborn as sns
plt.style.use("bmh")
sns.color_palette("hls", 1)

import matplotlib
matplotlib.rc('xtick', labelsize=14)
matplotlib.rc('ytick', labelsize=14)
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

def plot_arrows(x, y, dir, color):
    """ plot arrows on
        specified positions """
    # scale = 0.6
    scale = 1
    arrow_length = 5*scale
    head_width = 4*scale
    num_arrows = 4

    dx = x[1] - x[0]
    dy = y[1] - y[0]
    x_array = x[0] + np.arange(num_arrows)/(num_arrows-1)*dx
    y_array = y[0] + np.arange(num_arrows)/(num_arrows-1)*dy
    Pos = np.array(list(zip(x_array, y_array)))

    head_length = arrow_length
    # dir = np.array(Pos[1] - Pos[0])
    if np.linalg.norm(dir) < 0.1:
        dir = np.array([0,1])
    dir_norm = dir/np.linalg.norm(dir)
    dir_arrow = dir_norm*arrow_length
    for i in range(len(Pos[:,0])-1):
        plt.arrow(Pos[i,0] - dir_arrow[0]/2, Pos[i,1] - dir_arrow[1]/2, dir_arrow[0], dir_arrow[1], head_width = head_width, head_length = arrow_length, length_includes_head = True, color = color)

def color_cycle(num_color):
    """ get coloer from matplotlib
        color cycle """
    color = plt.rcParams['axes.prop_cycle'].by_key()['color']
    return color[num_color]

def plot(pos_MB, pos_other):
    plt.figure(num=0, figsize = (6,6), facecolor='w', edgecolor='k')

    plt.subplot(2, 1, 1)
    x_MB = [pos_MB[0][0], pos_MB[1][0]]
    y_MB = [pos_MB[0][1], pos_MB[1][1]]
    dir_MB = np.array(np.array(pos_MB[1]) - np.array(pos_MB[0]))

    plt.plot(x_MB, y_MB, linestyle = "--", color = color_cycle(3), label = "HB")
    plot_arrows(x_MB, y_MB, dir_MB, color_cycle(3))


    color = [0, 1, 2, 4, 5, 6, 7, 8, 9]
    dir_other = np.zeros((len(pos_other),2))
    for i in range(len(pos_other)):
        x = [pos_other[i][0][0], pos_other[i][1][0]]
        y = [pos_other[i][0][1], pos_other[i][1][1]]
        dir_other[i] = np.array(np.array(pos_other[i][1]) - np.array(pos_other[i][0]))
        plt.plot(x, y, color = color_cycle(color[i]), linestyle = "--")
        plot_arrows(x, y, dir_other[i], color_cycle(color[i]))
    plt.xlabel(r"$x$", fontsize=14)
    plt.ylabel(r"$y$", fontsize=14)
    plt.legend(fontsize = 13)
    plt.axis("equal")

    axis = plt.gca()
    ylim = axis.get_ylim()
    xlim = axis.get_xlim()
    plt.fill_between([-100,100], -100, 100, alpha = 0.1, color = color_cycle(9) )
    axis.set_xlim(xlim)
    axis.set_ylim(ylim)




    plt.subplot(2, 1, 2)
    for i in range(len(pos_other)):
        x = np.array([pos_other[i][0][0], pos_other[i][1][0]]) - np.array(x_MB)
        y = np.array([pos_other[i][0][1], pos_other[i][1][1]]) - np.array(y_MB)
        plt.plot(x, y, color = color_cycle(color[i]), linestyle = "--")
        if x[0] == x[1] and y[0] == y[1]:
                    plt.plot(x, y, color = color_cycle(color[i]), Marker = "o")
        else:
            plot_arrows(x, y, dir_other[i], color_cycle(color[i]))

    plt.plot(0,0, markersize = 8, marker = "o", linestyle = "None", color = color_cycle(3), label = "HB")

    plt.xlabel(r"$x'$", fontsize=14)
    plt.ylabel(r"$y'$", fontsize=14)
    plt.legend(fontsize = 13)
    plt.axis("equal")

    axis = plt.gca()
    ylim = axis.get_ylim()
    xlim = axis.get_xlim()
    plt.fill_between([-100,100], -100, 100, alpha = 0.1, color = color_cycle(9) )
    axis.set_xlim(xlim)
    axis.set_ylim(ylim)









    # plt.xlabel(r"$x$", fontsize=14)
    # plt.ylabel(r"$y$", fontsize=14)
    # plt.legend(fontsize = 13)
    # plt.tight_layout(pad=1.1, w_pad=0.7, h_pad=0.2)
    # plt.savefig("../article/figures/figure.pdf", bbox_inches="tight")



if __name__ == "__main__":
    # pos_MB = [[0,10], [10, 30]]
    # pos_other =[    [[10,10], [30, 10]],
    #                 [[20,20], [10, 30]],
    #                 [[40, 10], [40, 10]],
    #                 [[-20,20], [-20, 0]],
    #                 [[-10,10], [0, 30]],
    #                 [[5,0], [-5, 5]]]
    # plot(pos_MB, pos_other)
    # plt.tight_layout(pad=1.1, w_pad=0.7, h_pad=0.2)
    # plt.subplots_adjust(hspace = 0.3)
    # # plt.savefig("../article/figures/reference_frame_explainer.pdf", bbox_inches="tight")
    # plt.show()


    pos_MB = np.array([[0,10], [10, 30]])
    a = 35
    sqrt2 = 1/np.sqrt(2)
    pos_other =np.array([    [[0,-a], [0, 0]],
                        [[sqrt2*a,-sqrt2*a], [0, 0]],
                        [[a,0], [0, 0]],
                        [[sqrt2*a,sqrt2*a], [0, 0]],
                        [[0,a], [0, 0]],
                        [[-sqrt2*a,sqrt2*a], [0, 0]],
                        [[-sqrt2*a,-sqrt2*a], [0, 0]],
                        [[-a,0], [0, 0]]])

    pos_other += pos_MB
    plot(pos_MB, pos_other)
    plt.tight_layout(pad=1.1, w_pad=0.7, h_pad=0.2)
    plt.subplots_adjust(hspace = 0.3)
    plt.savefig("../article/figures/reference_frame_explainer2.pdf", bbox_inches="tight")
    plt.show()
