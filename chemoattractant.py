import math


def chemoattractant(concentration, tip):
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
    K = .013
    Dp = 1.44 * (10**-4)

    gamma = (2 * kr2 + kp) / (n5 * n7 * kf2)
    theta = Rf * tip

    alpha = (kr1 * Rf) / (2 * kf1 * concentration + kr1)
    beta = (n4 * (kp - 2 * kr1)) / (2 * kf1 * concentration + kr1)
    delta = n4 + beta

    A = (-2 * alpha * delta - gamma + theta * beta + math.sqrt(
        (2 * alpha * delta + gamma - theta * beta) ** 2 + 4 * alpha * beta * (n4 + delta) * (theta - alpha))) / \
        (2 * beta * (n4 + delta))

    chemo = math.exp((xo * K / Dp) * (K - (K + A) * math.exp(-A / K)))

    return chemo