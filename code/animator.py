from plotter import *
from matplotlib.animation import FuncAnimation

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


# def animator(MB_pos, OB_pos, right_coast = 10):
#     MB_end = MB_pos[-1]
#     OB_end = OB_pos[-1]
#     fig1 = plt.figure(num=1, facecolor='w', edgecolor='k')
#     ax1 = plt.axes(xlim=(-1, right_coast), ylim=(-60, 60))
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
#     plt.plot(MB_end[0], MB_end[1], "o", label = "End Point 1")
#     plt.plot(OB_end[0], OB_end[1], "o", label = "End Point 2")
#     plt.legend()
#     plt.show()
#
#
#     MB_pos2, OB_pos2 = MB_pos - MB_pos, OB_pos - MB_pos
#     MB_end = MB_pos2[-1]
#     OB_end = OB_pos2[-1]
#     fig2 = plt.figure(num=2, facecolor='w', edgecolor='k')
#     ax2 = plt.axes(xlim=(-1, right_coast), ylim=(-60, 60))
#     MB_line, = ax2.plot([], [], "o", label = "Main Boat")
#     OB_line, = ax2.plot([], [], "o", label = "Other Boat")
#     eye_line, = ax2.plot([], [], lw = 2, color = "black", label = "eye_line")
#     def animate2(i):
#         MB_line.set_data(MB_pos2[i,0], MB_pos2[i,1])
#         OB_line.set_data(OB_pos2[i,0], OB_pos2[i,1])
#         m = (OB_pos2[i,1] - MB_pos2[i,1])/(OB_pos2[i,0] - MB_pos2[i,0])
#         x = np.array([MB_pos2[i,0], MB_pos2[i,0] + right_coast])
#         y = np.array([MB_pos2[i,1], MB_pos2[i,1] + m*right_coast])
#         eye_line.set_data(x, y)
#         return MB_line, OB_line, eye_line
#
#     anim2 = FuncAnimation(fig2, animate2, frames=len(MB_pos2), interval=100, blit=True)
#     plt.plot(MB_end[0], MB_end[1], "o", label = "End Point 1")
#     plt.plot(OB_end[0], OB_end[1], "o", label = "End Point 2")
#     plt.legend()
#     plt.show()

# if __name__ == "__main__":
#
#     if False: #plotter
#         MB_start = (0,0)
#         OB_start = (50,40)
#         MB_end = (0, 40)
#         OB_end = (10, 40)
#         MB_pos, OB_pos = simulator(MB_start, OB_start, MB_end, OB_end)
#         coast_center = (100, 100)
#         coast_angle = deg_to_rad(90)
#         plotter(MB_pos, OB_pos, coast_center, coast_angle)
#         plt.show()
#
#     if False: #HB_plotter
#         MB_start = (0,0)
#         OB_start = (50,40)
#         MB_end = (0, 40)
#         OB_end = (0, 40)
#         MB_pos, OB_pos = simulator(MB_start, OB_start, MB_end, OB_end)
#         coast_center = (100, 100)
#         coast_angle = deg_to_rad(90)
#         HB_plotter(MB_pos, OB_pos, coast_center, coast_angle)
#         plt.show()
#
#     if True: #subplotter
#         #Crash 1
#         # MB_start = [(0,0), (0,0), (0,0), (0,0)]
#         # OB_start = [(20,0), (40,20), (50,40), (50,60)]
#         # MB_end = [(0, 40), (0, 40), (0, 40), (0, 40)]
#         # OB_end = [(0, 40), (0, 40), (0, 40), (0, 40)]
#         # coast_center = [(100,100), (100,100), (100,100), (100,100)]
#         # coast_angle = deg_to_rad(np.array([90, 90, 90, 90]))
#         # subplotter(MB_start, OB_start, MB_end, OB_end, coast_center, coast_angle)
#         # plt.savefig("../article/figures/subplot_C1.pdf", bbox_inches="tight")
#         # plt.show()
#
#         #Crash 2
#         # MB_start = [(0,0), (0,0), (0,0), (0,0)]
#         # OB_start = [(50,40), (50,70), (30,80), (0.1,80)]
#         # MB_end = [(0, 40), (0, 40), (0, 40), (0, 40)]
#         # OB_end = [(0, 40), (0, 40), (0, 40), (0, 40)]
#         # coast_center = [(100,110), (100,110), (100,110), (100,150)]
#         # coast_angle = deg_to_rad(np.array([180, 180, 180, 180]))
#         # subplotter(MB_start, OB_start, MB_end, OB_end, coast_center, coast_angle)
#         # plt.savefig("../article/figures/subplot_C2.pdf", bbox_inches="tight")
#         # plt.show()
#
#         # Non Crash 1
#         MB_start = [(0,0), (0,0), (0,0), (0,0)]
#         OB_start = [(30,0), (40,40), (30,60), (10,80)]
#         MB_end = [(0, 40), (0, 40), (0, 40), (0, 40)]
#         OB_end = [(10, 30), (10, 40), (10, 45), (10, 45)]
#         coast_center = [(100,100), (100,100), (100,120), (100,120)]
#         coast_angle = deg_to_rad(np.array([90, 90, 180, 180]))
#         subplotter(MB_start, OB_start, MB_end, OB_end, coast_center, coast_angle)
#         plt.savefig("../article/figures/subplot_NC1.pdf", bbox_inches="tight")
#         plt.show()
#

# animator(MB_pos, OB_pos, 10)
