import matplotlib.pyplot as plt
from matplotlib import cm
from numpy import zeros

from concentration import concentration
from chemoattractant import chemoattractant
from transition import transition
from normal_transition import normal_transition
from probability import probability
from movement import movement

size = 50
workspace = zeros((size, size))
m = size // 2
n = 0
tip = 1
source_m = size // 2
source_n = size - 1
k = .07
p_r = .25
p_l = .25
p_u = .25
p_d = .25
p_mn = 0
probabilities = [p_r, p_l, p_u, p_d, p_mn]
iterations = 0

memory = {(m, n)}
locations = [[-1.5,0],[-1,-0.5],[-1,0.5],[-0.5,-1],[-0.5,0],[-0.5,1],[0,-1.5],[0,-0.5],[0,0.5],[0,1.5],[0.5,-1],
             [0.5,0],[0.5,1],[1,-0.5],[1,0.5],[1.5,0]]

while iterations < 200000:
    chemo = []
    for i in locations:
        if (m + i[0], n + i[1]) in memory:
            conc = 0
        else:
            conc = concentration(m + i[0], n + i[1], source_m, source_n)
        chemo.append(chemoattractant(conc, tip))

    transitions = transition(chemo, k)
    normal_transitions = normal_transition(transitions)
    probabilities = probability(normal_transitions, probabilities)
    m, n = movement(probabilities, memory, workspace, m, n, size, iterations)

    iterations += 1

plt.imshow(workspace)
cm.get_cmap("jet")
plt.show()
