import DCMGenerator as dcm_g
import numpy as np
from math import sqrt
from math import log
import scipy.stats as st
import matplotlib.pyplot as plt
from statsmodels.distributions.empirical_distribution import ECDF
import operator
import networkx as nx


def get_corr(a, d, beta):

    alpha = beta / d

    if d == 1:
        b = 2

    else:
        b = (alpha / (alpha - 1) * (beta - 1) / beta * a ** (alpha / beta)) ** (beta / (alpha - beta))

    c = (b / a) ** (alpha / beta)

    EDd = a * beta * c ** (d + 1) / (beta - d - 1)

    ED = alpha * b / (alpha - 1)

    EW_square = alpha * b ** 2 / (alpha - 2)
    Ew_square = beta * c ** 2 / (beta - 2)
    print("EW_square: ", EW_square)
    print("Ew_sqaure: ", EW_square)

    var_D = ED + EW_square - ED ** 2
    var_d = ED + Ew_square - ED ** 2

    print("var_D: ", var_D)
    print("var_d: ", var_d)

    corr = (EDd - ED * ED) / sqrt(var_D * var_d)

    return corr


def validate_params(d, beta):
    if beta > 2 and beta > 2 * d and beta > d + 1:
        return True
    else:
        return False


def get_expected_degree(a, d, beta):
    alpha = beta / d

    if d == 1:
        b = 2
    else:
        b = (alpha / (alpha - 1) * (beta - 1) / beta * a ** (alpha / beta)) ** (beta / (alpha - beta))


    ED = alpha * b / (alpha - 1)

    return ED



# alpha = beta / d
def test2(a, d):

    beta_range = np.arange(2.5, 6, 0.2)  # 2.5, 3, 3.5, 4, 4.5, 5, 5.5

    n = 2000  # graph size

    degree_corr = []
    sample_degree_corr = []
    rank_corr = []

    models = {}
    i = 0

    beta_valid = []
    for beta in beta_range:
        if not validate_params(d, beta):
            continue
        if get_expected_degree(a, d, beta) < 2:
            continue

        beta_valid.append(beta)
        model = dcm_g.DCMGenerator(a, d, beta, 2000, 'Erased')
        degree_corr.append(get_corr(a, d, beta))
        sample_degree_corr.append(st.pearsonr(model.graph_din, model.graph_dout)[0])
        rank_corr.append(model.spearman_test()[0])

        models[i] = model
        i += 1

    degree_corr = np.array(degree_corr)
    sample_degree_corr = np.array(sample_degree_corr)
    rank_corr = np.array(rank_corr)

    return models, degree_corr, sample_degree_corr, rank_corr, beta_valid

def plot_corr(degree_corr, sample_degree_corr, rank_corr, beta_valid):

    plt.figure()
    plt.plot(beta_valid ,degree_corr, marker='o', label='degree correlation')
    plt.plot(beta_valid, sample_degree_corr, marker='v', label='sample degree correlation')
    plt.plot(beta_valid, rank_corr, marker='<', label='rank correlation')

    plt.xlabel('beta')

def plot_tail_pr(models, mode):
    if mode == 'original':
        for m in models.values():
            m.plot_tail_dist(list(m.page_rank.values()))
    elif mode == 'logy':
        for m in models.values():
            m.plot_tail_dist_log(list(m.page_rank.values()))
    elif mode == 'loglog':
        for m in models.values():
            m.plot_tail_dist_loglog(list(m.page_rank.values()))


def plot_tail_bc(models, mode):
    if mode == 'original':
        for m in models.values():
            m.plot_tail_dist(list(m.betweenness_centrality.values()))
    elif mode == 'logy':
        for m in models.values():
            m.plot_tail_dist_log(list(m.betweenness_centrality.values()))
    elif mode == 'loglog':
        for m in models.values():
            m.plot_tail_dist_loglog(list(m.betweenness_centrality.values()))


def plot_tail_din(models, mode):
    if mode == 'original':
        for m in models.values():
            m.plot_tail_dist(m.graph_din)
    elif mode == 'logy':
        for m in models.values():
            m.plot_tail_dist_log(m.graph_din)
    elif mode == 'loglog':
        for m in models.values():
            m.plot_tail_dist_loglog(m.graph_din)


def get_legend(models):
    handles = []
    for m in models.values():
        handles.append('alpha = ' + "%0.2f"%m.fg.params['alpha']
                       + ', beta = ' + "%0.2f"%m.fg.params['beta'])
    return handles


def plot_seqs(list_dicts):
    """
    Plot list_of_dicts in decreasing order of the first one
    Note that the first one is drawn at last
    :param list_dict: list of dicts
    :return: sorted first dict
    """
    seq_0 = list_dicts[0]
    scores = []
    seq_0_sort = sorted(seq_0.items(), key=operator.itemgetter(1), reverse=True)

    for d in list_dicts:
        scores.append([d[node[0]] for node in seq_0_sort])

    for i in range(1, len(scores)):
        plt.plot(scores[i])

    plt.plot(scores[0])

    return seq_0_sort


def test3(a_range, d_range, beta_range):
    # let d varies

    models = {}
    shot = 0

    params_valid = {}
    params_valid['a'] = []
    params_valid['d'] = []
    params_valid['alpha'] = []
    params_valid['beta'] = []

    degree_corr = []
    sample_degree_corr = []
    rank_corr = []

    i = 0
    for a in a_range:
        for d in d_range:
            for beta in beta_range:
                print("Shot:", shot)
                shot += 1
                if not validate_params(d, beta):
                    continue
                if get_expected_degree(a, d, beta) < 1.5 or get_expected_degree(a, d, beta) > 60:
                    continue

                alpha = beta / d

                params_valid['a'].append(a)
                params_valid['d'].append(d)
                params_valid['alpha'].append(alpha)
                params_valid['beta'].append(beta)

                model = dcm_g.DCMGenerator(a, d, beta, 2000, 'Erased')

                degree_corr.append(get_corr(a, d, beta))
                sample_degree_corr.append(st.pearsonr(model.graph_din, model.graph_dout)[0])
                rank_corr.append(model.spearman_test()[0])

                models[i] = model
                i += 1

    degree_corr = np.array(degree_corr)
    sample_degree_corr = np.array(sample_degree_corr)
    rank_corr = np.array(rank_corr)

    return models, degree_corr, sample_degree_corr, rank_corr, params_valid


def test3():
    a_range = np.arange(0.5, 3, 0.3)
    d_range = np.arange(0.5, 2, 0.3)
    beta_range = np.arange(2.5, 5, 0.3)

    params_valid = {}
    params_valid['a'] = []
    params_valid['d'] = []
    params_valid['alpha'] = []
    params_valid['beta'] = []

    shot = 0
    for a in a_range:
        for d in d_range:
            for beta in beta_range:
                print("Shot:", shot)
                shot += 1
                if not validate_params(d, beta):
                    continue
                if get_expected_degree(a, d, beta) < 1.5 or get_expected_degree(a, d, beta) > 60:
                    continue

                alpha = beta / d

                params_valid['a'].append(a)
                params_valid['d'].append(d)
                params_valid['alpha'].append(alpha)
                params_valid['beta'].append(beta)

    return params_valid


def test4(a, d):

    samples = 0
    degrees = 0
    ranks = 0

    for i in range(0, 20):
        models, degree_corr, sample_degree_corr, rank_corr, params_valid = test2(a, d)
        samples += sample_degree_corr
        degrees += degree_corr
        ranks += rank_corr

    samples = samples / 20
    degrees = degrees / 20
    ranks = ranks / 20

    return samples, degrees, ranks


def test5():
    a1 = 1
    d1 = 1
    beta = 2.5

    m = 20
    num_con = []

    for i in range(0, m):
        model = dcm_g.DCMGenerator(a1, d1, beta, 2000, 'Erased')
        num_con.append(nx.number_strongly_connected_components(model.graph))

    num_con = np.array(num_con)

    return num_con


def test6():
    a1 = 1
    d1 = 1
    a2 = 0.5
    d2 = 1.4
    a3 = 2
    d3 = 0.6
    beta_range = beta_range = np.arange(2.5, 6, 0.2)

    num_con1 = 0
    num_con2 = 0
    num_con3 = 0

    rank_corr1 = 0
    rank_corr2 = 0
    rank_corr3 = 0

    m = 20

    for i in range(0, m):
        num_con, rank_corr = test7(a1, d1)
        num_con1 += num_con
        rank_corr1 += rank_corr

        num_con, rank_corr = test7(a2, d2)
        num_con2 += num_con
        rank_corr2 += rank_corr

        num_con, rank_corr = test7(a3, d3)
        num_con3 += num_con
        rank_corr3 += rank_corr

    num_con1 = num_con1 / m
    num_con2 = num_con2 / m
    num_con3 = num_con3 / m

    rank_corr1 = rank_corr1 / m
    rank_corr2 = rank_corr2 / m
    rank_corr3 = rank_corr3 / m

    return num_con1, num_con2, num_con3, rank_corr1, rank_corr2, rank_corr3


def test7(a, d):
    beta_valid = []

    beta_range = np.arange(2.5, 6, 0.2)

    i = 0

    num_con = []  # number of strongly connected components
    rank_corr = []
    for beta in beta_range:
        if not validate_params(d, beta):
            continue
        if get_expected_degree(a, d, beta) < 2:
            continue

        beta_valid.append(beta)
        model = dcm_g.DCMGenerator(a, d, beta, 2000, 'Erased')
        num_con.append(nx.number_strongly_connected_components(model.graph))
        rank_corr.append(model.spearman_test()[0])

        i += 1

    num_con = np.array(num_con)
    rank_corr = np.array(rank_corr)

    return num_con, rank_corr


def test8():
    alpha = 3
    beta = 3
    a_range = np.arange(1, 3, 0.3)
    d = 1

    n = 2000

    degree_corr = []
    rank_corr = []

    models = {}
    i = 0

    a_valid = []
    for a in a_range:
        print(i)
        if not validate_params(d, beta):
            continue
        if get_expected_degree(a, d, beta) < 2:
            continue

        a_valid.append(a)
        model = dcm_g.DCMGenerator(a, d, beta, 2000, 'Erased')
        degree_corr.append(get_corr(a, d, beta))
        rank_corr.append(model.spearman_test()[0])

        models[i] = model
        i += 1

    degree_corr = np.array(degree_corr)
    rank_corr = np.array(rank_corr)

    return models, degree_corr, rank_corr, a_valid



