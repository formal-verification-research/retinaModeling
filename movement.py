from random import random
import matplotlib.pyplot as plt
from matplotlib import cm


def movement(probabilities,memory,workspace,m,n,size,iterations):
    rand = random()
    rand2 = random()

    if rand <= probabilities[0] + probabilities[2] + probabilities[3] + probabilities[4]:
        if rand <= probabilities[0]:
            if n != size - 1:
                n += 1
        elif rand <= probabilities[0] + probabilities[1]:
            if n != 0:
                n -= 1
        elif rand <= probabilities[0] + probabilities[1] + probabilities[2]:
            if m != 0:
                m -= 1
        elif rand <= probabilities[0] + probabilities[2] + probabilities[3] + probabilities[4]:
            if m != size - 1:
                m += 1
        if (m, n) in memory:
            if rand2 <= .01:
                plt.imshow(workspace)
                cm.get_cmap("jet")
                plt.show()
                exit("after " + str(iterations) + " iterations the tip cell died upon encountering capillary")
        memory.add((m, n))

    workspace[m][n] = 100000

    return m, n
