def transition(chemo, k):
    trans_Hplus = (1 / k) * (chemo[7] / (chemo[7] + chemo[10] + chemo[6] + chemo[3]))
    trans_Hminus = (1 / k) * (chemo[8] / (chemo[8] + chemo[12] + chemo[9] + chemo[5]))
    trans_Vplus = (1 / k) * (chemo[11] / (chemo[11] + chemo[14] + chemo[15] + chemo[13]))
    trans_Vminus = (1 / k) * (chemo[4] / (chemo[4] + chemo[1] + chemo[0] + chemo[2]))
    trans_Hplus_mn = (1 / k) * (chemo[8] / (chemo[8] + chemo[7] + chemo[4] + chemo[11]))
    trans_Hminus_mn = (1 / k) * (chemo[7] / (chemo[8] + chemo[7] + chemo[4] + chemo[11]))
    trans_Vplus_mn = (1 / k) * (chemo[4] / (chemo[8] + chemo[7] + chemo[4] + chemo[11]))
    trans_Vminus_mn = (1 / k) * (chemo[11] / (chemo[8] + chemo[7] + chemo[4] + chemo[11]))
    return [trans_Hplus, trans_Hminus, trans_Vplus, trans_Vminus, trans_Hplus_mn, trans_Hminus_mn,
            trans_Vplus_mn, trans_Vminus_mn]
