import math
import matplotlib.pyplot as plt
import PowerLawDistribution as pld
import numpy as np


def get_corr(alpha, beta, E, d):
    s = beta/alpha
    c = E * (beta - 1) / beta

    a = c **((alpha - beta) / alpha) * (beta * (alpha - 1)) / (alpha * (beta - 1))

    b = E * (alpha - 1) / alpha


    E_W_1s = beta / (beta - 1 - s) * c ** (1 + s)
    Var_W_s = beta / (beta - 2 * s) * c ** (2 * s) - (beta * c ** s / (beta - s)) ** 2


    Cov_Dplus_Dminus = d * (a * E_W_1s - E ** 2)

    Var_Dplus = a ** 2 * (d ** 2 + (1 - d) ** 2) * Var_W_s + E
    Var_Dminus = beta / (beta - 2 ) * c ** 2 - E ** 2 + E


    corr = Cov_Dplus_Dminus / ((Var_Dplus) ** (1/2) * (Var_Dminus) ** (1/2))


    return corr


def test_corr(alpha, beta, E):
    d_lst = np.arange(0, 1.01, 0.01)
    corr_lst = []

    for d in d_lst:
        cor_d = get_corr(alpha, beta, E, d)
        corr_lst.append(cor_d)

    return corr_lst


def get_corr_new_version(alpha, beta, E, d):
    s = beta / alpha
    c = E * (beta - 1) / beta

    a = c ** ((alpha - beta) / alpha) * (beta * (alpha - 1)) / (alpha * (beta - 1))

    # E[(W-)^(s+1)]
    E_W_s_plus_1 = beta / (beta - 1 - s) * c ** (1 + s)
    # E[(W-)^(2s)]
    E_W_2s = beta / (beta - 2 * s) * c ** (2 * s)
    # E[(W-)^s]
    E_W_s = beta / (beta - s) * c ** s

    #E[(W^+)^2]
    E_Wplus_2 = a**2 * (d**2 + (1 - d)**2) * E_W_2s + 2 * a**2 * d * (1 - d) * E_W_s**2

    Cov_Dplus_Dminus = a*d*E_W_s_plus_1 + a * (1-d)*E_W_s*E - E**2

    Var_Dplus = E_Wplus_2 - E**2 + E
    Var_Dminus = beta / (beta - 2) * c ** 2 - E ** 2 + E

    corr = Cov_Dplus_Dminus / ((Var_Dplus) ** (1 / 2) * (Var_Dminus) ** (1 / 2))

    return corr

