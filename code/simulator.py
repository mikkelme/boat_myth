import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


import seaborn as sns
plt.style.use("bmh")
sns.color_palette("hls", 1)

import matplotlib
matplotlib.rc('xtick', labelsize=14)
matplotlib.rc('ytick', labelsize=14)
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'


def simulator(MB_start, OB_start, MB_end, OB_end, T = 10, dt = 0.1):
    K = int(T/dt + 1)
    MB_pos = np.zeros((K,2)) #MB = Main Boat
    OB_pos = np.zeros((K,2)) #OB = Other Boat
    t = np.zeros(K)

    MB_pos[0] = MB_start
    OB_pos[0] = OB_start
    MB_vel = (MB_end - MB_pos[0])/T
    OB_vel = (OB_end - OB_pos[0])/T
    for k in range(K - 1):
        MB_pos[k+1] = MB_pos[k] + MB_vel*dt
        OB_pos[k+1] = OB_pos[k] + OB_vel*dt
        t[k+1] = t[k] + dt
    return MB_pos, OB_pos

# def animator(MB_pos, OB_pos, right_coast = 10):
#     MB_end = MB_pos[-1]
#     OB_end = OB_pos[-1]
#
#     fig, (ax1, ax2) = plt.subplots(2,1)
#
#     # ax1 = plt.axes(xlim=(-1, right_coast), ylim=(-60, 60))
#     MB_line, = ax1.plot([], [], "o", label = "Main Boat")
#     OB_line, = ax1.plot([], [], "o", label = "Other Boat")
#     eye_line, = ax1.plot([], [], lw = 2, color = "black", label = "eye_line")
#     def animate1(i):
#         MB_line.set_data(MB_pos[i,0], MB_pos[i,1])
#         OB_line.set_data(OB_pos[i,0], OB_pos[i,1])
#         m = (OB_pos[i,1] - MB_pos[i,1])/(OB_pos[i,0] - MB_pos[i,0])
#         x = np.array([MB_pos[i,0], MB_pos[i,0] + right_coast])
#         y = np.array([MB_pos[i,1], MB_pos[i,1] + m*right_coast])
#         eye_line.set_data(x, y)
#         return MB_line, OB_line, eye_line
#
#     anim1 = FuncAnimation(fig1, animate1, frames=len(MB_pos), interval=100, blit=True)
#     anim.append(anim1)
#     plt.plot(MB_end[0], MB_end[1], "o", label = "End Point 1")
#     plt.plot(OB_end[0], OB_end[1], "o", label = "End Point 2")
#     plt.legend()
#     plt.show()


def animator(MB_pos, OB_pos, right_coast = 10):
    MB_end = MB_pos[-1]
    OB_end = OB_pos[-1]
    fig1 = plt.figure(num=1, facecolor='w', edgecolor='k')
    ax1 = plt.axes(xlim=(-1, right_coast), ylim=(-60, 60))
    MB_line, = ax1.plot([], [], "o", label = "Main Boat")
    OB_line, = ax1.plot([], [], "o", label = "Other Boat")
    eye_line, = ax1.plot([], [], lw = 2, color = "black", label = "eye_line")
    def animate1(i):
        MB_line.set_data(MB_pos[i,0], MB_pos[i,1])
        OB_line.set_data(OB_pos[i,0], OB_pos[i,1])
        m = (OB_pos[i,1] - MB_pos[i,1])/(OB_pos[i,0] - MB_pos[i,0])
        x = np.array([MB_pos[i,0], MB_pos[i,0] + right_coast])
        y = np.array([MB_pos[i,1], MB_pos[i,1] + m*right_coast])
        eye_line.set_data(x, y)
        return MB_line, OB_line, eye_line

    anim1 = FuncAnimation(fig1, animate1, frames=len(MB_pos), interval=100, blit=True)
    plt.plot(MB_end[0], MB_end[1], "o", label = "End Point 1")
    plt.plot(OB_end[0], OB_end[1], "o", label = "End Point 2")
    plt.legend()
    plt.show()


    MB_pos2, OB_pos2 = MB_pos - MB_pos, OB_pos - MB_pos
    MB_end = MB_pos2[-1]
    OB_end = OB_pos2[-1]
    fig2 = plt.figure(num=2, facecolor='w', edgecolor='k')
    ax2 = plt.axes(xlim=(-1, right_coast), ylim=(-60, 60))
    MB_line, = ax2.plot([], [], "o", label = "Main Boat")
    OB_line, = ax2.plot([], [], "o", label = "Other Boat")
    eye_line, = ax2.plot([], [], lw = 2, color = "black", label = "eye_line")
    def animate2(i):
        MB_line.set_data(MB_pos2[i,0], MB_pos2[i,1])
        OB_line.set_data(OB_pos2[i,0], OB_pos2[i,1])
        m = (OB_pos2[i,1] - MB_pos2[i,1])/(OB_pos2[i,0] - MB_pos2[i,0])
        x = np.array([MB_pos2[i,0], MB_pos2[i,0] + right_coast])
        y = np.array([MB_pos2[i,1], MB_pos2[i,1] + m*right_coast])
        eye_line.set_data(x, y)
        return MB_line, OB_line, eye_line

    anim2 = FuncAnimation(fig2, animate2, frames=len(MB_pos2), interval=100, blit=True)
    plt.plot(MB_end[0], MB_end[1], "o", label = "End Point 1")
    plt.plot(OB_end[0], OB_end[1], "o", label = "End Point 2")
    plt.legend()
    plt.show()

def intercept(A, B, center, angle):
    Ax, Ay = A[0], A[1]
    Bx, By = B[0], B[1]
    m = (By - Ay)/(Bx - Ax)
    b = Ay - m*Ax

    x_inter = (-b + center[1] - np.tan(angle)*center[0])/(m - np.tan(angle))
    y_inter = m*x_inter + b
    # print(x_inter, y_inter)

    return x_inter, y_inter

def coast_line(center, angle, length):
    # num_points
    # m = tan(angle)
    # y =
    point1 = [length/2*np.cos(angle) + center[0], length/2*np.sin(angle) + center[1]]
    point2 = [-length/2*np.cos(angle) + center[0], -length/2*np.sin(angle) + center[1]]
    zip = np.array([[point1[0], point2[0]], [point1[1], point2[1]]])
    return zip

def deg_to_rad(angle):
    return angle/360*2*np.pi

def color_cycle(num_color):
    color = plt.rcParams['axes.prop_cycle'].by_key()['color']
    return color[num_color]

def plot_arrows(Pos, color):
    arrow_length = 5
    head_length = arrow_length
    dir = np.array(Pos[1] - Pos[0])
    dir_norm = dir/np.linalg.norm(dir)
    dir_arrow = dir_norm*arrow_length

    for i in range(len(Pos[:,0])):
        plt.arrow(Pos[i,0] - dir_arrow[0]/2, Pos[i,1] - dir_arrow[1]/2, dir_arrow[0], dir_arrow[1], width = 1, head_length = arrow_length, length_includes_head = True, color = color)

def plotter(MB_pos, OB_pos):
    intercept_points = True

    coast_center = (100, 100)
    coast_angle = deg_to_rad(90)
    coast_length = 500
    coast_color = "darkorange"
    coast_color = color_cycle(4) # 4, 8
    num_points = 4
    idx = np.linspace(0, len(MB_pos) - 1, num_points).astype('int')

    plt.figure(num=0, facecolor='w', edgecolor='k')

    #Plot boat path
    plt.plot(MB_pos[idx,0], MB_pos[idx,1], linestyle = "--" , color = color_cycle(3), label = "HB")
    plt.plot(OB_pos[idx,0], OB_pos[idx,1], linestyle = "--" , color = color_cycle(1), label = "KB")

    #Plot coast
    zip = coast_line(coast_center, coast_angle, coast_length)
    plt.plot(zip[0], zip[1], color = color_cycle(4), alpha = 0.5,  label = "Kyst")

    #Plot boath arrows
    if np.linalg.norm(MB_pos[idx[-1]] - OB_pos[idx[-1]]) < 0.1:
        plot_arrows(MB_pos[idx[:-1]], color_cycle(3))
        plot_arrows(OB_pos[idx[:-1]], color_cycle(1))
        plt.plot(MB_pos[idx[-1],0], MB_pos[idx[-1],1], "o", marker = "X", markersize = 8, color = color_cycle(4), label = "Kollisionspunkt")
    else:
        plot_arrows(MB_pos[idx], color_cycle(3))
        plot_arrows(OB_pos[idx], color_cycle(1))


    ax = plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()


    #Plot intercept lines
    if intercept_points:
        label = "Skæringspunkt"
        for i in range(num_points):
            diff = np.min(np.abs(MB_pos[idx[i]] - OB_pos[idx[i]]))
            tol = 0.01
            if diff > tol:
                if i == 1:
                    label = "_" + label
                x,y = intercept((MB_pos[idx[i],0], MB_pos[idx[i],1]), (OB_pos[idx[i],0], OB_pos[idx[i],1]), coast_center, coast_angle)
                plt.plot(x,y, 'o', marker = "x", color = "black", label = label)
                plt.plot((MB_pos[idx[i],0], x), (MB_pos[idx[i],1], y), linestyle = "--", marker = None, alpha = 0.5, color = 'black')


    plt.axis('equal')
    plt.xlim(xlim[0], xlim[1] + 110)
    plt.ylim(ylim[0], ylim[1])

    #Fill coast
    x_fill = [200 , zip[0][1], zip[0][0]]
    y1 = [zip[1][1], zip[1][1], zip[1][0]]
    y2 = [zip[1][0], zip[1][0], zip[1][0]]
    plt.fill_between(x_fill, y1, y2, alpha = 0.25, color = coast_color )

    #Fill water
    x_fill = [-200 , zip[0][1], zip[0][0]]
    plt.fill_between(x_fill, y1, y2, alpha = 0.1, color = color_cycle(9) )


    plt.xlim(-5, 120)
    plt.ylim(-5, 100)
    plt.xlabel("x [m]", fontsize = 14)
    plt.ylabel("y [m]", fontsize = 14)
    plt.legend(loc = "best", fontsize = 13)
    plt.savefig("../article/figures/eksempel1.pdf", bbox_inches="tight")
    plt.show()

if __name__ == "__main__":

    MB_start = (0,0)
    OB_start = (50,30)
    MB_end = (0, 40)
    OB_end = (0, 40)

    MB_pos, OB_pos = simulator(MB_start, OB_start, MB_end, OB_end)
    plotter(MB_pos, OB_pos)
    # animator(MB_pos, OB_pos, 10)
