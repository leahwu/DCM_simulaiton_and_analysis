import DCMGenerator as dcm_g
import numpy as np
import scipy.stats as st
import PowerLawDistribution as pld
from math import sqrt

a = 0.5

d = 1.3

beta = 3.8

alpha = beta / d

b = (alpha / (alpha - 1) * (beta - 1) / beta * a ** (alpha / beta)) ** (beta / (alpha - beta))

c = (b / a) ** (alpha / beta)

EDd = a * beta * c**(d+1) / (beta - d - 1)

ED = alpha * b / (alpha - 1)

EW_square = alpha * b**2 / (alpha - 2)
Ew_square = beta * c**2 / (beta - 2)

var_D = ED + EW_square - ED**2
var_d = ED + Ew_square - ED**2

corr = (EDd - ED * ED) / sqrt(var_D * var_d)

m = 500
corrs = np.zeros(m)
d_in_mean = np.zeros(m)
d_out_mean = np.zeros(m)
expected_Dd = np.zeros(m)

n = 1000

model = pld.PowerLaw(a, d, beta)
for i in range(0, m):
    d_in, d_out = model.rvs(n)
    d_in_mean[i] = d_in.mean()
    d_out_mean[i] = d_out.mean()
    #expected_Dd[i] = np.dot(d_in, d_out) / len(d_in)
    corrs[i] = st.pearsonr(d_in, d_out)[0]

mean = corrs.mean()

