import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
plt.style.use("bmh")
sns.color_palette("hls", 1)

import matplotlib
matplotlib.rc('xtick', labelsize=14)
matplotlib.rc('ytick', labelsize=14)
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

def d(theta, v, omega_k):
    d = v*np.sin(theta)/omega_k
    return d


#Dimensionless
plt.figure(num=0, facecolor='w', edgecolor='k')
v = 1
omega_k = 1
theta = np.linspace(0, np.pi, int(1e4))

plt.plot(theta/np.pi, d(theta, v, omega_k))
plt.gca().set_xticks(np.linspace(0,1,5))
plt.xlabel(r"$\theta_{HB}$ [$\pi$]", fontsize = 14)
plt.ylabel(r"$\min (d)$ $[\omega_k/v_{HB}]$", fontsize = 14)
#plt.savefig("../article/figures/limit_dimensionless.pdf", bbox_inches="tight")


#With dimension
plt.figure(num=1, facecolor='w', edgecolor='k')
v = 2 # [m/s]
omega_k = 0.0024 #[rad]


plt.plot(theta/(2*np.pi)*360, d(theta, v, omega_k))
plt.gca().set_xticks(np.linspace(0,180,7))
plt.xlabel(r"$\theta_{HB}$ [$^{\circ}$]", fontsize = 14)
plt.ylabel(r"$\min(d)$ [m]", fontsize = 14)
#plt.savefig("../article/figures/limit_dimension.pdf", bbox_inches="tight")


#With dimension
plt.figure(num=2, facecolor='w', edgecolor='k')
v = 2 # [m/s]
omega_k = 0.0024 #[rad]

def s(theta, beta, v, omega_k):
    s = d(theta, v, omega_k)*np.sin(theta + beta)
    s_return = np.where(s > 0, s, None)
    return s_return

beta = np.linspace(0, 90, 5)
#beta = [0, np.pi/6]
for i in range(len(beta)):
    plt.plot(theta/(2*np.pi)*360, s(theta, beta[i]/360*2*np.pi, v, omega_k), label = r"$\beta = $%g$^{\circ}$" %(beta[i]))
    #print("90", beta[i], s(90/360*2*np.pi, beta[i]/360*2*np.pi, v, omega_k))
plt.gca().set_xticks(np.linspace(0,180,7))
plt.xlabel(r"$\theta_{HB}$ [$^{\circ}$]", fontsize = 14)
plt.ylabel(r"$\min(s_{kyst})$ [m]", fontsize = 14)
leg = plt.legend()
leg.set_title('Kystvinkel:')
#plt.savefig("../article/figures/limit_coastdis.pdf", bbox_inches="tight")


#With dimension
plt.figure(num=3, facecolor='w', edgecolor='k')
v = 2 # [m/s]
omega_k = 0.0024 #[rad]

def s(theta, beta, v, omega_k):
    s = d(theta, v, omega_k)*np.sin(theta + beta)
    s_return = np.where(s > 0, s, None)
    return s_return

beta = np.linspace(0, 90, 5)
for i in range(len(beta)):
    plt.plot(theta/(2*np.pi)*360, s(theta, beta[i]/360*2*np.pi, v, omega_k), alpha = 0.3,  label = r"$\beta = $%g$^{\circ}$" %(beta[i]))
plt.plot(theta/(2*np.pi)*360, d(theta, v, omega_k), label = r"$\beta$ = 90$^{\circ}$ - $\theta_{HB}$")

points = [0, 30, 60, 90]
for i in points:
    x, y = i, d(i/360*2*np.pi, v, omega_k)
    plt.plot(x,y, "o", color = "black")
    plt.text(x + 3, y, f"{y:.0f} m" )

plt.gca().set_xticks(np.linspace(0,180,7))
plt.xlabel(r"$\theta_{HB}$ [$^{\circ}$]", fontsize = 14)
plt.ylabel(r"$\min(s_{kyst})$ [m]", fontsize = 14)
leg = plt.legend()
leg.set_title('Kystvinkel:')
plt.savefig("../article/figures/limit_coastdis_betamax.pdf", bbox_inches="tight")






plt.show()
