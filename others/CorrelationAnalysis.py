import DCMGenerator as dcm
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
import powerlaw

# b = 10
alpha = 4
beta = 3
b = 5

graph_lst_same_5000 = []



## Theo Correlation calculation tool
def get_b(a, alpha, beta):
    """for alpha != beta"""
    if alpha == beta:
        raise ValueError('Compute the value of b for alpha != beta only!')
    return (alpha / (alpha - 1) * (beta - 1) / beta * a ** (alpha / beta)) ** (beta / (alpha - beta))


def get_corr(a, alpha, beta, b=None):

    if b is None:
        b = get_b(a, alpha, beta)

    d = beta / alpha

    c = (b / a) ** (alpha / beta)

    e_d_in = b * alpha / (alpha - 1)
    e_d_out = c * beta / (beta - 1)

    e_w_plus_square = alpha * b ** 2 / (alpha - 2)
    e_w_minus_square = beta * c ** 2 / (beta - 2)

    e_prod = a * beta * c ** (d + 1) / (beta - d - 1)
    var_d_in = e_d_in + e_w_plus_square - e_d_in ** 2
    var_d_out = e_d_out + e_w_minus_square - e_d_out ** 2

    corr = (e_prod - e_d_in * e_d_out) / np.sqrt(var_d_in * var_d_out)

    return corr

def power_test(graph):
    in_deg = graph.d_in
    out_deg = graph.d_out

    plt.suptitle('Power-law distribution of In and Out degree for large graph')
    plt.title('alpha = 4, beta = 3, a = 3.1, corr = 0.92')
    fig1 = powerlaw.plot_ccdf(in_deg, color='r')
    powerlaw.plot_ccdf(out_deg, color='b')
    fitin = powerlaw.Fit(in_deg)
    fitout = powerlaw.Fit(out_deg)
    fitin.power_law.plot_ccdf(color='r', linestyle='--', ax = fig1)
    fitout.power_law.plot_ccdf(color='b', linestyle='--', ax = fig1)
    plt.legend(['In degree', 'Out degree', 'Fitted in degree', 'Fitted out degree'])

def test4(a, alpha, beta, b=None):
    """
    test for correlation of the graph
    :param a:
    :param alpha:
    :param beta:
    :param b:
    :return:
    """

    model = dcm.DCMGenerator(a, alpha, beta, 2000, 'Erased', b=b)

    corr1 = st.pearsonr(model.d_in_original, model.d_out_original)[0]
    # corr2 = pearsonr(model.d_in, model.d_out)[0]
    corr3 = st.pearsonr(model.graph_din, model.graph_dout)[0]

    corr = get_corr(a, alpha, beta, b)

    rank_corr = model.spearman_test()[0]

    return corr, corr1, corr3, rank_corr, model


def large_test():
    corr_thm = []
    corr_orig = []
    corr_graph = []
    models = []
    rank_corr = []

    alpha = 4
    beta = 3
    a_range = np.arange(1.3, 3.3, 0.3)

    m = 50

def test4(a, alpha, beta, b=None):
    model = dcm.DCMGenerator(a, alpha, beta, 2000, 'Erased')

    corr1 = st.pearsonr(model.d_in_original, model.d_out_original)[0]
        # corr2 = pearsonr(model.d_in, model.d_out)[0]
    corr3 = st.pearsonr(model.graph_din, model.graph_dout)[0]

    corr = get_corr(a, alpha, beta, b)

    rank_corr = model.spearman_test()[0]
    return corr, corr1, corr3, rank_corr, model

corr_thm = []
corr_orig = []
corr_graph = []
rank_corr = []
models = []
for a in a_range:
    rank_corr_i = []
    corr_orig_i = []
    corr_graph_i = []
    model = None
    c = 0
    for i in range(0,m):
        c, c_orig, c_graph, r_c, model = test4(a, alpha, beta)
        rank_corr_i.append( r_c )
        corr_orig_i.append( c_orig )
        corr_graph_i.append( c_graph )

    c_orig_i = np.array(corr_orig_i)
    c_graph_i = np.array(corr_graph_i)
    rank_corr_i = np.array(rank_corr_i)

    corr_thm.append(c)
    corr_orig.append(c_orig_i)
    corr_graph.append(c_graph_i)
    rank_corr.append(rank_corr_i)

    models.append(model)
    print('finish loops')

corr_thm = np.array(corr_thm)


def get_mean(seqs):
    """
    seqs should be like: [[],[],[]]
    :param seqs:
    :return:
    """
    mean_seq = []
    for seq in seqs:
        mean_seq.append(seq.mean())

    return mean_seq

rank_corr_mean = get_mean(rank_corr)
corr_orig_mean = get_mean(corr_orig)