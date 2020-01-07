

def probability(normal_transition, probability):

    delta_pmn = normal_transition[0] * probability[0] + normal_transition[1] * probability[1] + normal_transition[2] *\
                probability[2] + normal_transition[3] * probability[3] - (normal_transition[4] + normal_transition[5] +
                                                                          normal_transition[6] + normal_transition[7]) \
                * probability[4]

    p_mn = probability[4] + delta_pmn
    p_r = probability[0] - normal_transition[0] * delta_pmn
    p_l = probability[1] - normal_transition[1] * delta_pmn
    p_u = probability[2] - normal_transition[2] * delta_pmn
    p_d = probability[3] - normal_transition[3] * delta_pmn
    return [p_r, p_l, p_u, p_d, p_mn]