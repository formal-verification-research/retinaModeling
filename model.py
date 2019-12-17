import matplotlib.pyplot as plt
from matplotlib import cm
from numpy import zeros
from random import random

from concentration import concentration
from chemoattractant import chemoattractant


size = 200
workspace = zeros((size, size))
m = 100
n = 10
tip = 1
source_m = 150
source_n = 200
k = .7
p_mn = 0
p_r = .25
p_l = .25
p_u = .25
p_d = .25
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

    trans_Hplus = (1 / k) * (chemo[0] / (chemo[0] + chemo[4] + chemo[7] + chemo[11]))
    trans_Hminus = (1 / k) * (chemo[0] / (chemo[0] + chemo[2] + chemo[6] + chemo[10]))
    trans_Vplus = (1 / k) * (chemo[0] / (chemo[0] + chemo[10] + chemo[11] + chemo[12]))
    trans_Vminus = (1 / k) * (chemo[0] / (chemo[0] + chemo[6] + chemo[7] + chemo[8]))
    trans_Hplus_mn = (1 / k) * (chemo[1] / (chemo[1] + chemo[3] + chemo[5] + chemo[9]))
    trans_Hminus_mn = (1 / k) * (chemo[3] / (chemo[1] + chemo[3] + chemo[5] + chemo[9]))
    trans_Vplus_mn = (1 / k) * (chemo[5] / (chemo[1] + chemo[3] + chemo[5] + chemo[9]))
    trans_Vminus_mn = (1 / k) * (chemo[9] / (chemo[1] + chemo[3] + chemo[5] + chemo[9]))

    ntrans_Hplus = trans_Hplus / (trans_Hplus + trans_Hminus + trans_Vplus + trans_Vminus)
    ntrans_Hminus = trans_Hminus / (trans_Hplus + trans_Hminus + trans_Vplus + trans_Vminus)
    ntrans_Vplus = trans_Vplus / (trans_Hplus + trans_Hminus + trans_Vplus + trans_Vminus)
    ntrans_Vminus = trans_Vminus / (trans_Hplus + trans_Hminus + trans_Vplus + trans_Vminus)

    ntrans_Hplus_mn = trans_Hplus_mn / (trans_Hplus_mn + trans_Hminus_mn + trans_Vplus_mn + trans_Vminus_mn)
    ntrans_Hminus_mn = trans_Hminus_mn / (trans_Hplus_mn + trans_Hminus_mn + trans_Vplus_mn + trans_Vminus_mn)
    ntrans_Vplus_mn = trans_Vplus_mn / (trans_Hplus_mn + trans_Hminus_mn + trans_Vplus_mn + trans_Vminus_mn)
    ntrans_Vminus_mn = trans_Vminus_mn / (trans_Hplus_mn + trans_Hminus_mn + trans_Vplus_mn + trans_Vminus_mn)

    delta_pmn = ntrans_Hplus * p_r + ntrans_Hminus * p_l + ntrans_Vplus * p_u + ntrans_Vminus * p_d - (
                ntrans_Hplus_mn + ntrans_Hminus_mn + ntrans_Vplus_mn + ntrans_Vminus_mn) * p_mn

    p_mn = p_mn + delta_pmn
    p_r = p_r - ntrans_Hplus * delta_pmn
    p_l = p_l - ntrans_Hminus * delta_pmn
    p_u = p_u - ntrans_Vplus * delta_pmn
    p_d = p_d - ntrans_Vminus * delta_pmn

    rand = random()

    if rand <= p_u:
        if m != 0:
            m -= 1
            workspace[m][n] = 100000
            memory.add((m, n))
    elif rand <= p_u + p_d:
        if m != size-1:
            m += 1
            workspace[m][n] = 100000
            memory.add((m, n))
    elif rand <= p_u + p_d + p_l:
        if n != 0:
            n -= 1
            workspace[m][n] = 100000
            memory.add((m, n))
    elif rand <= p_u + p_d + p_l + p_r:
        if n != size -1:
            n += 1
            workspace[m][n] = 100000
    else:
        workspace[m][n] = 100000

    iterations += 1


plt.imshow(workspace)
cm.get_cmap("jet")
plt.show()
