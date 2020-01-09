from random import random


def movement(probabilities,memory,workspace,m,n,size):
    rand = random()

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
        memory.add((m, n))

    workspace[m][n] = 100000

    return m, n
