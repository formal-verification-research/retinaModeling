

def normal_transition(transition):
    normal_transition = []
    move_total = transition[0] + transition[1] + transition[2] + transition[3]
    stay_total = transition[4] + transition[5] + transition[6] + transition[7]
    for i in range(len(transition)):
        if i < 4:
            if move_total == 0:
                normal_transition.append(0)
            else:
                normal_transition.append(transition[i]/move_total)
        else:
            if stay_total == 0:
                normal_transition.append(0)
            else:
                normal_transition.append(transition[i]/stay_total)
    return normal_transition