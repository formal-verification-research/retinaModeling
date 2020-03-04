from scipy import spatial
import math
from numpy import zeros
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def concentration(m, n, m_source, n_source):
    diffusion_coeff = 0.360                  # mm ^ 2/hr from Fronteirs of oncology paper
    decay = 0.65                             # /hr from Fronteirs of oncology paper
    step_size = .02                          # mm from Fronteirs of oncology paper
    production = 20 * 0.02                   # pg / mm ^ 2 hr Journal of Biological Engineering paper
    radius = spatial.distance.euclidean((m, n), (m_source, n_source))*step_size
    concentration = (production / (2 * ((diffusion_coeff * decay) ** 0.5))) * \
                    (math.exp(-1*((decay / diffusion_coeff) ** 0.5) * radius))      # concentration in pg / mm3
    return concentration

'''
grid = zeros((50, 50))
A = []
chemo = []
for i in range(50):
    for j in range(50):
        grid[i][j] = concentration(i, j, 25, 49)
        n4 = 0.4494
        n5 = 1.2250
        n7 = 2.2250

        kf1 = 1.69
        kf2 = kf1 * 100
        kr1 = 0.02
        kr2 = kr1 / 100
        kp = 0.6667
        Rf = 0.02

        xo = 0.05
        K = 2
        Dp = 1.44 * (10**-4)

        gamma = (2 * kr2 + kp) / (n5 * n7 * kf2)
        theta = Rf

        alpha = (kr1 * Rf) / (2 * kf1 * grid[i][j] + kr1)
        beta = (n4 * (kp - 2 * kr1)) / (2 * kf1 * grid[i][j]+ kr1)
        delta = n4 + beta

        proportion = (-2 * alpha * delta - gamma + theta * beta + math.sqrt(
            (2 * alpha * delta + gamma - theta * beta) ** 2 + 4 * alpha * beta * (n4 + delta) * (theta - alpha))) / \
            (2 * beta * (n4 + delta))

        #A.append(proportion)

        #chemo.append(math.exp((xo * K / Dp) * (K - (K + proportion) * math.exp(-proportion / K))))

    #plt.plot(A,chemo)
    #plt.show()
'''
fig = plt.figure()
ax = plt.gca(projection='3d')

X = np.arange(0, 50, 1)
Y = np.arange(0, 50, 1)
X, Y = np.meshgrid(X, Y)

Z = zeros((50,50))
for i in range(50):
    for j in range(50):
        Z[i][j] = concentration(i, j, 25, 49)

surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('concentration')
plt.show()




'''
for i in np.linspace(0,101,1000):
    n4 = 0.4494
    n5 = 1.2250
    n7 = 2.2250

    kf1 = 1.69
    kf2 = kf1 * 100
    kr1 = 0.02
    kr2 = kr1 / 100
    kp = 0.6667
    Rf = 0.02

    xo = 0.05
    K = 2
    Dp = 1.44 * (10 ** -4)

    gamma = (2 * kr2 + kp) / (n5 * n7 * kf2)
    theta = Rf

    alpha = (kr1 * Rf) / (2 * kf1 * i + kr1)
    beta = (n4 * (kp - 2 * kr1)) / (2 * kf1 * i + kr1)
    delta = n4 + beta

    proportion = (-2 * alpha * delta - gamma + theta * beta + math.sqrt(
        (2 * alpha * delta + gamma - theta * beta) ** 2 + 4 * alpha * beta * (n4 + delta) * (theta - alpha))) / \
                 (2 * beta * (n4 + delta))
    A.append(proportion)


start = np.arange(0, 100, 0.1).tolist()
plt.plot(start,A)
plt.xlabel("concentration of free vegf pg/mm^3")
plt.ylabel("activated receptor concentration pg/mm^3")
plt.show()
'''

'''
B = []
for i in np.linspace(0,11,100):
    n4 = 0.4494
    n5 = 1.2250
    n7 = 2.2250

    kf1 = 1.69
    kf2 = kf1 * 100
    kr1 = 0.02
    kr2 = kr1 / 100
    kp = 0.6667
    Rf = 0.02

    xo = 0.05
    K = 2
    Dp = 1.44 * (10 ** -4)

    gamma = (2 * kr2 + kp) / (n5 * n7 * kf2)
    theta = Rf

    alpha = (kr1 * Rf) / (2 * kf1 * i + kr1)
    beta = (n4 * (kp - 2 * kr1)) / (2 * kf1 * i + kr1)
    delta = n4 + beta

    proportion = (-2 * alpha * delta - gamma + theta * beta + math.sqrt(
        (2 * alpha * delta + gamma - theta * beta) ** 2 + 4 * alpha * beta * (n4 + delta) * (theta - alpha))) / \
                 (2 * beta * (n4 + delta))
    B.append(proportion)

start = np.arange(0, 10, 0.1).tolist()
plt.plot(start,B)
plt.xlabel("concentration of free vegf pg/mm^3")
plt.ylabel("activated receptor concentration pg/mm^3")
plt.show()
'''

'''
C = []
for i in np.linspace(0,3,20):
    n4 = 0.4494
    n5 = 1.2250
    n7 = 2.2250

    kf1 = 1.69
    kf2 = kf1 * 100
    kr1 = 0.02
    kr2 = kr1 / 100
    kp = 0.6667
    Rf = 0.02

    xo = 0.05
    K = 2
    Dp = 1.44 * (10 ** -4)

    gamma = (2 * kr2 + kp) / (n5 * n7 * kf2)
    theta = Rf

    alpha = (kr1 * Rf) / (2 * kf1 * i + kr1)
    beta = (n4 * (kp - 2 * kr1)) / (2 * kf1 * i + kr1)
    delta = n4 + beta

    proportion = (-2 * alpha * delta - gamma + theta * beta + math.sqrt(
        (2 * alpha * delta + gamma - theta * beta) ** 2 + 4 * alpha * beta * (n4 + delta) * (theta - alpha))) / \
                 (2 * beta * (n4 + delta))
    C.append(proportion)

start = np.arange(0, 2, 0.1).tolist()
plt.plot(start,C)
plt.xlabel("concentration of free vegf pg/mm^3")
plt.ylabel("activated receptor concentration pg/mm^3")
plt.show()
'''

'''
chemo = []
xo = 0.05
K = 2
Dp = 1.44 * (10**-4)
A = np.arange(0, 0.02, 0.01).tolist()
for i in np.arange(0, 0.02, 0.01).tolist():
    chemo.append(math.exp((xo * K / Dp) * (K - (K + i) * math.exp(-i / K))))

plt.plot(A,chemo)
plt.xlabel("activated receptor concentration pg/mm^3")
plt.ylabel("chemoattractance")
plt.show()
'''
