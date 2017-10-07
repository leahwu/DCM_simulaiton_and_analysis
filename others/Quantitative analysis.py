import plotly.plotly as py
from scipy import stats
from plotly.tools import FigureFactory as FF
from DCMGenerator import *


n = 2000

# Generate list of DCM
## 1) Erased Case
dcm_erased_ls = []
for j in range(16):
    dcm_erased_ls.append([DCMGenerator(1, 1 + 0.2 * i, 2.5 + 0.5 * j, n, 'Erased')for i in range(5)])

# Spearman Correlation
## Erased
spear_corr_matrix = [["Correlation"]+["d = "+str(1 + 0.2*i) for i in range(5)]]
for j in range(16):
    spear_corr_matrix.append(["beta = "+ str(2.5 + 0.5*j)]+ [round(dcm_erased_ls[j][i].spearman_test()[0],4) for i in range(5)])

corr_table = FF.create_table(spear_corr_matrix, index=True)
for i in range(len(corr_table.layout.annotations)):
    corr_table.layout.annotations[i].font.size = 18
py.iplot(corr_table, filename='corr_table')


# KS test for graph bi-degree with bi-degree sequence

# Erased In-degree
ks_in_eras_matrix = [["In P-val"]+["d = "+str(1 + 0.2*i) for i in range(5)]]
for j in range(16):
    ks_in_eras_matrix.append(["beta = "+ str(2.5 + 0.5*j)]+ [round(stats.ks_2samp(dcm_erased_ls[j][i].d_in_original, dcm_erased_ls[j][i].graph_din)[1], 4) for i in range(5)])

ks_in_eras_table = FF.create_table(ks_in_eras_matrix, index=True)

for i in range(len(ks_in_eras_table.layout.annotations)):
    ks_in_eras_table.layout.annotations[i].font.size = 18
py.iplot(ks_in_eras_table, filename='ks_in_eras_table')


#Wilcoxon
in_wil_eras_matrix = [["In Wil P-val"]+["d = "+str(1 + 0.2*i) for i in range(5)]]
for j in range(16):
    in_wil_eras_matrix.append(["beta = "+ str(2.5 + 0.5*j)]+ [round(stats.wilcoxon(dcm_erased_ls[j][i].d_in_original, dcm_erased_ls[j][i].graph_din)[1], 4) for i in range(5)])

in_wil_eras_table = FF.create_table(in_wil_eras_matrix, index=True)

for i in range(len(in_wil_eras_table.layout.annotations)):
    in_wil_eras_table.layout.annotations[i].font.size = 18
py.iplot(in_wil_eras_table, filename='in_wil_eras_table')



# Erased Out-degree
ks_out_eras_matrix = [["Out P-val"]+["d = "+str(1 + 0.2*i) for i in range(5)]]
for j in range(16):
    ks_out_eras_matrix.append(["beta = "+ str(2.5 + 0.5*j)]+ [round(stats.ks_2samp(dcm_erased_ls[j][i].d_out_original, dcm_erased_ls[j][i].graph_dout)[1],4) for i in range(5)])

ks_out_eras_table = FF.create_table(ks_out_eras_matrix, index=True)

for i in range(len(ks_out_eras_table.layout.annotations)):
    ks_out_eras_table.layout.annotations[i].font.size = 18
ks_out_eras_table.layout.update({'title': 'Erased Out-degree KS p-value'})
py.iplot(ks_out_eras_table, filename='ks_out_eras_table')


#Wilcoxon out
out_wil_eras_matrix = [["In Wil P-val"]+["d = "+str(1 + 0.2*i) for i in range(5)]]
for j in range(16):
    out_wil_eras_matrix.append(["beta = "+ str(2.5 + 0.5*j)]+ [round(stats.wilcoxon(dcm_erased_ls[j][i].d_out_original, dcm_erased_ls[j][i].graph_dout)[1], 4) for i in range(5)])

out_wil_eras_table = FF.create_table(out_wil_eras_matrix, index=True)

for i in range(len(out_wil_eras_table.layout.annotations)):
    out_wil_eras_table.layout.annotations[i].font.size = 18
py.iplot(out_wil_eras_table, filename='out_wil_eras_table')


# Erased PR_BC
ks_PR_BC_eras_matrix = [["PR_BC_KS"]+["d = "+str(1 + 0.2*i) for i in range(5)]]
for j in range(16):
    ks_PR_BC_eras_matrix.append(["beta = "+ str(2.5 + 0.5*j)]+ [round(stats.ks_2samp(list(dcm_erased_ls[j][i].page_rank),[elem/sum(list(dcm_erased_ls[j][i].betweenness_centrality)) for elem in list(dcm_erased_ls[j][i].betweenness_centrality)])[1],4) for i in range(5)])

ks_PR_BC_eras_table = FF.create_table(ks_PR_BC_eras_matrix, index=True)

for i in range(len(ks_out_eras_table.layout.annotations)):
    ks_PR_BC_eras_table.layout.annotations[i].font.size = 18
py.iplot(ks_PR_BC_eras_table, filename='ks_out_eras_table')


# wilcoxon test
ks_wilcox_eras_matrix = [["PR_BC_Wil"]+["d = "+str(1 + 0.2*i) for i in range(5)]]
for j in range(16):
    ks_wilcox_eras_matrix.append(["beta = "+ str(2.5 + 0.5*j)]+ [round(stats.wilcoxon(list(dcm_erased_ls[j][i].page_rank),[elem/sum(list(dcm_erased_ls[j][i].betweenness_centrality)) for elem in list(dcm_erased_ls[j][i].betweenness_centrality)])[1],4) for i in range(5)])

ks_wilcox_eras_table = FF.create_table(ks_wilcox_eras_matrix, index=True)

for i in range(len(ks_out_eras_table.layout.annotations)):
    ks_wilcox_eras_table.layout.annotations[i].font.size = 18
py.iplot(ks_wilcox_eras_table, filename='ks_wilcox_eras_table')