import DCMGenerator as dcm
import TheoreticalFunctionTool as tft
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np

alpha = 2.1
beta  = 2.1
E = 3

def hist(alpha, beta, E, d, n = 5000):
    corr_deg_lst = []
    corr_BP_lst = []
    mean_lst = []

    for i in range(100):
        dcm_d = dcm.DCMGenerator(alpha, beta, E, d, n)
        corr_deg_d = dcm_d.graph_corr
        corr_bcpr_d = dcm_d.BC_PR_corr
        mean_d = dcm_d.mean_in_degree

        corr_deg_lst.append(corr_deg_d)
        corr_BP_lst.append(corr_bcpr_d)
        mean_lst.append(mean_d)

    return [corr_deg_lst, corr_BP_lst, mean_lst]

def inter_corr(alpha, beta, E, n = 5000, rep = 10):
    deg_corr = []
    theo_corr = []

    BC_PR_corr = []

    for d in range(0,104,4):
        deg_corr_d_i = []
        BC_PR_corr_d_i = []
        for i in range(rep):
            dcm_d = dcm.DCMGenerator(alpha, beta, E, d/100, n)

            deg_corr_d_unit = dcm_d.graph_corr[0]
            BC_PR_corr_d_unit =dcm_d.BC_PR_corr[0]

            deg_corr_d_i.append(deg_corr_d_unit)
            BC_PR_corr_d_i.append(BC_PR_corr_d_unit)

        deg_corr_d_mean = np.mean(deg_corr_d_i)
        BC_PR_corr_d_mean = np.mean(BC_PR_corr_d_i)

        theo_corr.append(tft.get_corr(alpha, beta, E, d / 100))
        deg_corr.append(deg_corr_d_mean)
        BC_PR_corr.append(BC_PR_corr_d_mean)

    return [deg_corr, BC_PR_corr, theo_corr]

