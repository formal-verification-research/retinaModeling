import matplotlib.pyplot as plt
from matplotlib import cm
from numpy import zeros

from concentration import concentration
from chemoattractant import chemoattractant
from transition import transition
from normal_transition import normal_transition
from probability import probability
from movement import movement

size = 200
workspace = zeros((size, size))
m = 100
n = 10
tip = 1
source_m = 150
source_n = 200
k = .7
p_r = .25
p_l = .25
p_u = .25
p_d = .25
p_mn = 0
probabilities = [p_r, p_l, p_u, p_d, p_mn]
iterations = 0

memory = set((m, n))
locations = [[0,0], [0,1], [0,2], [0,-1], [0,-2], [-1,0], [-1,1], [-1,-1], [-2,0], [1,0], [1,1], [1,-1], [2,0]]
# locations = [mn0,r1,rr2,l3,ll4,u5,ur6,ul7,uu8,d9,dr10,dl11,dd12]

while iterations < 10000:
    chemo = []
    for i in locations:
        if (m+i[0], n+i[1]) in memory:
            conc = 0
        else:
            conc = concentration(m+i[0], n+i[1], source_m, source_n)
        chemo.append(chemoattractant(conc, tip))

    transitions = transition(chemo, k)
    normal_transitions = normal_transition(transitions)
    probabilities = probability(normal_transitions, probabilities)
    m, n = movement(probabilities, memory, workspace, m, n, size,iterations)

    iterations += 1

plt.imshow(workspace)
cm.get_cmap("jet")
plt.show()
