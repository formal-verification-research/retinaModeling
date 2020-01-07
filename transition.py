

def transition(chemo, k):
    trans_Hplus = (1 / k) * (chemo[0] / (chemo[0] + chemo[4] + chemo[7] + chemo[11]))
    trans_Hminus = (1 / k) * (chemo[0] / (chemo[0] + chemo[2] + chemo[6] + chemo[10]))
    trans_Vplus = (1 / k) * (chemo[0] / (chemo[0] + chemo[10] + chemo[11] + chemo[12]))
    trans_Vminus = (1 / k) * (chemo[0] / (chemo[0] + chemo[6] + chemo[7] + chemo[8]))
    trans_Hplus_mn = (1 / k) * (chemo[1] / (chemo[1] + chemo[3] + chemo[5] + chemo[9]))
    trans_Hminus_mn = (1 / k) * (chemo[3] / (chemo[1] + chemo[3] + chemo[5] + chemo[9]))
    trans_Vplus_mn = (1 / k) * (chemo[5] / (chemo[1] + chemo[3] + chemo[5] + chemo[9]))
    trans_Vminus_mn = (1 / k) * (chemo[9] / (chemo[1] + chemo[3] + chemo[5] + chemo[9]))
    return [trans_Hplus, trans_Hminus, trans_Vplus, trans_Vminus, trans_Hplus_mn, trans_Hminus_mn,\
           trans_Vplus_mn, trans_Vminus_mn]
