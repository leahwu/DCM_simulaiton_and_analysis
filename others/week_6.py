import DCMGenerator as dcm_g
import PowerLawDistribution as pld
import  validate as vd
import numpy as np
from math import sqrt
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
from statsmodels.distributions.empirical_distribution import ECDF
from math import log
from scipy import stats
import networkx as nx
import operator


def get_b(a, alpha, beta):
    """for alpha != beta"""
    if alpha == beta:
        raise ValueError('Compute the value of b for alpha != beta only!')
    return (alpha / (alpha - 1) * (beta - 1) / beta * a ** (alpha / beta)) ** (beta / (alpha - beta))


def test(a, alpha, beta, b=None, dependency=True):
    """
    test for correlation of the graph
    :param a: 
    :param alpha: 
    :param beta: 
    :param b: 
    :return: 
    """
    model = gen_model(a, alpha, beta, b=None, dependency=True)

    corr1 = pearsonr(model.d_in_original, model.d_out_original)[0]
    # corr2 = pearsonr(model.d_in, model.d_out)[0]
    corr3 = pearsonr(model.graph_din, model.graph_dout)[0]

    corr = get_corr(a, alpha, beta, b)

    rank_corr = model.spearman_test()[0]

    return corr, corr1, corr3, rank_corr, model


def gen_model(a, alpha, beta, b=None, dependency=True):
    model = dcm_g.DCMGenerator(a, alpha, beta, 2000, 'Erased', b=b, dependency=dependency)
    return model


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

    corr = (e_prod - e_d_in * e_d_out) / sqrt(var_d_in * var_d_out)

    return corr


def get_expected_degree(alpha, b):
    return b * alpha / (alpha - 1)


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


def get_std(seqs):
    std_seq = []
    for seq in seqs:
        std_seq.append(seq.std())

    return std_seq


def get_loglog(seq):
    """
    help get the tail distribution logx, logy of the seq
    :param seq: 
    :return: 
    """
    cdf = ECDF(seq)
    for x in cdf.x:
        if x <= 0:
            cdf.x = cdf.x[1:]
            cdf.y = cdf.y[1:]
    # eliminating the cdf = 1 term
    cdf.x = cdf.x[:-1]
    cdf.y = cdf.y[:-1]

    logx = [log(x) for x in cdf.x]
    logy = [log(1 - y) for y in cdf.y]

    return logx, logy


def abline(slope, intercept):
    """Plot a line from slope and intercept"""
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, '--')


def plot_tail(model):
    model.plot_tail_dist_loglog(list(model.page_rank.values()), 'page rank')
    model.plot_tail_dist_loglog(list(model.betweenness_centrality.values()), 'betweenness centrality')
    model.plot_tail_dist_loglog(model.graph_din, 'in-degree sequence')
    model.plot_tail_dist_loglog(model.graph_dout, 'out-degree sequence')
    plt.legend()


def linear_fit(x, y):
    # seq : list-like// graph.din, list(page_rank.values())
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    return slope, intercept


def d_tolist(d):
    return list(d.values())



def test_b(alpha, beta, m):
    a = 1  # not important for independent case

    models = []
    degree_corr = []
    rank_corr = []
    for b in range(5, 55, 5):
        r_c = 0
        d_c = 0
        for k in range(0, m):
            model = gen_model(a, alpha, beta, b=b, dependency=False)
            r_c += model.spearman_test()[0]
            d_c += pearsonr(model.graph_din, model.graph_dout)[0]

        r_c /= m
        d_c /= m

        models.append(model)
        rank_corr.append(r_c)
        degree_corr.append(d_c)

    degree_corr = np.array(degree_corr)
    rank_corr = np.array(rank_corr)

    return degree_corr, rank_corr, models


def max_dic(dic):
    v = list(dic.values())
    k = list(dic.keys())
    return k[v.index(max(v))]


def graph_remove(dcm, n, rule="pagerank"):
    #remove the top-n-ranked nodes subsequently

    # copy the graph for manipulation
    graph_copy = nx.Graph.copy(dcm.graph)
    # average shortest path, index 0 -original, index 1 - after removing top-ranked page rank(or bc)  node, and so on
    ave_sp = np.zeros(n + 1)
    ave_sp[0] = nx.average_shortest_path_length(dcm.graph)

    if rule == "pagerank":
        rank_copy = dict(dcm.page_rank)
    elif rule == "btwcentrality":
        rank_copy = dict(dcm.betweenness_centrality)
    elif rule == "totaldeg":
        rank_copy = dcm.total_degree
    elif rule == "indeg":
        rank_copy = dcm.in_degree

    elim = []  # eliminated list
    for i in np.arange(1, n + 1):
        node_label = max_dic(rank_copy)
        elim += [node_label]
        rank_copy.pop(node_label)
        graph_copy.remove_node(node_label)
        ave_sp[i] = nx.average_shortest_path_length(graph_copy)

    return graph_copy, elim, ave_sp


def graph_remove_indep(dcm, s, rule="pagerank"):
    #remove the top-s-ranked node independently

    # average shortest path, index 0 -original, index 1 - after removing top-ranked page rank(or bc)  node, and so on
    ave_sp = np.zeros(s + 1)
    ave_sp[0] = nx.average_shortest_path_length(dcm.graph)

    if rule == "pagerank":
        rank_copy = dict(dcm.page_rank)
    elif rule == "btwcentrality":
        rank_copy = dict(dcm.betweenness_centrality)
    #elif rule == "totaldeg":
     #   rank_copy =

    graphs = []

    elim = []  # eliminated list
    for i in np.arange(1, s + 1):
        # copy the graph for manipulation
        graph_copy = nx.Graph.copy(dcm.graph)

        node_label = max_dic(rank_copy)
        elim += [node_label]
        rank_copy.pop(node_label)

        graph_copy.remove_node(node_label)

        graphs.append(graph_copy)
        ave_sp[i] = nx.average_shortest_path_length(graph_copy)

    return graphs, elim, ave_sp


def plot_pr(model):
    plt.plot(sorted(list(model.page_rank.values()), reverse=True))


def test_2(model):
    graph_copy, elim, ave_sp = graph_remove(model, 1999)
    graph_copy_bc, elim_bc, ave_sp_bc = graph_remove(model, 1999, rule='btwcentrality')

    return graph_copy, elim, ave_sp, graph_copy_bc, elim_bc, ave_sp_bc


def test_3(model):
    graph_copy, elim, ave_sp = graph_remove_indep(model, 1999)
    graph_copy_bc, elim_bc, ave_sp_bc = graph_remove(model, 1999, rule='btwcentrality')

    return graph_copy, elim, ave_sp, graph_copy_bc, elim_bc, ave_sp_bc


def sort_dict(d):
    sort = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
    return sort

