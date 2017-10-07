import DCMGenerator as dcm_g
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
from statsmodels.distributions.empirical_distribution import ECDF
from math import log
# tail distribution of page rank and betweenness centrality

# the correlation between in-degree distribution and out-degree distribution

# assign the parameters
    # [Special Case [Alpha = Beta]]

def test1():
    a = 1.5  # the lower bound for W+

    alpha = 3  # the power for W+
    beta = 2.5  # the power for W+

    d = beta / alpha

    n = 2000 # graph size

    # generate simple directed configuration model
    model = dcm_g.DCMGenerator(a, d, beta, n, 'Erased')

    model.bc_vs_pr_dist()

    corr, pvalue = model.corr_in_and_out()

    model.bc_vs_pr_plot(200)
    model.bc_vs_pr_plot(2000)

    model.pr_vs_bc_plot(200)
    model.pr_vs_bc_plot(2000)

def test2():
    """
    We need beta > 2, beta > 2 * d, beta > d + 1 for finite variance
    :return: qualified models
    """

    f = open('week3_5.txt', 'w+')

    a_range = np.arange(0.5, 5, 0.5)  # 8 choices

    beta_range = np.arange(2.6, 6.0, 0.4)  # 9 choices
    d_range = np.arange(0.6, 2.5, 0.4)  # 6 choices

    n = 2000

    models = {}
    s = 'ALl the graph\'s size is ' + repr(n) + '.\n'

    rank_corr = []
    degree_corr = []
    degree_dist_corr = []
    mean_in_degree = []
    i = 0
    for a in a_range:
        for beta in beta_range:
            for d in d_range:
                if not (beta > 2 * d and beta > d + 1):
                    continue

                model = dcm_g.DCMGenerator(a, d, beta, n, 'Erased')
                if model.mean_in_degree < 2:
                    continue

                print(i)
                s += "Model" + repr(i) + ":\n"

                s += '\n'

                s += "The params are:\n"
                for para in model.fg.params.items():
                    s += para[0] + ' = ' + "%0.5f" % para[1] + '\n'
                s += '\n'

                s += "Expectation of W^minus is " + repr(model.fg.e_w_minus) + '\n'
                s += "Expectation of W^plus is " + repr(model.fg.e_w_plus) + '\n'
                s += '\n'

                s += "Mean of in-degree sequence is " + repr(model.mean_in_degree) + '\n'
                s += "Mean of out-degree sequence is " + repr(model.mean_out_degree) + '\n'
                s += '\n'
                mean_in_degree.append(model.mean_in_degree)

                s += "Spearsman's rank correlation test:\n"
                corr, pvalue = model.spearman_test()
                rank_corr.append(corr)
                s += "correlation = " + repr(corr) + ", pvalue = " + repr(pvalue) + "\n"
                s += '\n'

                s += "Correlation between in-degree sequence and out-degree sequence is: \n"
                corr, pvalue = model.corr_in_and_out()
                degree_corr.append(corr)
                s += "corr = " + repr(corr) + ", pvalue = " + repr(pvalue) + "\n"

                s += "Correlation between distribution of in-degree sequence and out-degree sequence is: \n"
                corr, pvalue = model.corr_dist_in_and_out()
                degree_dist_corr.append(corr)
                s += "corr = " + repr(corr) + ", pvalue = " + repr(pvalue) + "\n"

                models[i] = model

                s += '\n'
                i += 1

    corr = st.pearsonr(rank_corr, degree_corr)
    s += "Correlation between rank_corr and degree_corr is:\n"
    s += repr(corr) + '\n'

    corr = st.pearsonr(rank_corr, degree_dist_corr)
    s += "Correlation between rank_corr and degree_dist_corr is:\n"
    s += repr(corr) + '\n'

    f.write(s)
    f.close()

    return models, rank_corr, degree_corr, degree_dist_corr, mean_in_degree


# models, rank_corr, degree_corr = test2()

def test3():
    """
    Using Monte-carlo to test the result of certain parameters
    :return: mean, s.d.
    """
    m = 100 # simulation times
    a=1
    d=1
    beta = 3
    n = 1000 # graph size
    models = {}
    mean_in_degree = np.zeros(m)
    mean_out_degree = np.zeros(m)
    rank_corr = np.zeros(m)
    degree_corr = np.zeros(m)
    degree_dist_corr = np.zeros(m)
    for i in range(0, m):
        print("Simultation " + repr(i))

        model = dcm_g.DCMGenerator(a, d, beta, n, 'Erased')
        mean_in_degree[i] = model.mean_in_degree
        mean_out_degree[i] = model.mean_out_degree
        corr, p = model.spearman_test()
        rank_corr[i] = corr

        corr, p = model.corr_in_and_out()
        degree_corr[i] = corr

        corr, p = model.corr_dist_in_and_out()
        degree_dist_corr[i] = corr

        models[i] = model

    return models, mean_in_degree, mean_out_degree, rank_corr, degree_corr, degree_dist_corr


def sort2seq(seq1, seq2):
    """
    Plot 2 sequences in increasing order of seq1
    :param seq1: 
    :param seq2: 
    :return: sorted seq1, seq2, out-place sort
    """

    xy = zip(seq1, seq2)
    xy_sort = sorted(xy)
    xx = [a[0] for a in xy_sort]
    yy = [a[1] for a in xy_sort]
    plt.plot(xx)
    plt.plot(yy)
    return xx, yy


def plot_tail_dist(d, name):
    """
    Plot the tail distribution of data
    1-F(x), where F(x) is the empirical distribution of data
    :param d: self.page_rank or self.betweenness_centrality, type: dictionary
    :param name: name of d   
    :return: void
    """

    data = list(d.values())
    cdf = ECDF(data)
    size = len(data)

    plt.plot(cdf.x[:size - 1], [log(yy) for yy in (1 - cdf.y)[:size - 1]], label=name, marker='<', markerfacecolor='none',
             markersize=1)


def plot_bc_pr_dist(model):
    """
            Plot the tail distribution of page rank and betweenness centrality
            :return: Void
            """
    #plt.figure()
    plot_tail_dist(model.betweenness_centrality, 'betweenness centrality')
    plot_tail_dist(model.page_rank, 'page rank')
    plt.legend()

    txt = ''
    for para in model.fg.params.items():
        txt += para[0] + ' = ' + "%0.2f" % para[1] + ' '

    plt.title(txt)
    plt.title('Log Tail distribution\n' + txt)

    #plt.show()


def plot_dist_in_and_out(model):
    corr, p_value = model.corr_dist_in_and_out()

    #plt.figure()

    model.plot_helper(model.graph_din, 'red', 'o', 5)
    model.plot_helper(model.graph_dout, 'cyan', 'v', 5)

    plt.legend(['In-degree sequence', 'Out-degree sequence'])
    plt.xlabel('Degree')
    plt.ylabel('Number of nodes')
    plt.xlim([0, 40])

    txt = ''
    for para in model.fg.params.items():
        txt += para[0] + ' = ' + "%0.2f" % para[1] + ' '

    plt.title("Correlation: " + repr(corr) + " p-value: " + repr(p_value) + '\n' + txt)


def plot_in_and_out(model):
    corr, p_value = model.corr_in_and_out()

    plt.figure(1)
    sort2seq(model.graph_din, model.graph_dout)

    plt.legend(['in-degree sequence', 'out-degree sequence'])
    plt.xlabel('node')
    plt.ylabel('degree')

    txt = ''
    for para in model.fg.params.items():
        txt += para[0] + ' = ' + "%0.2f" % para[1] + ' '

    plt.title("Correlation: " + repr(corr) + " p-value: " + repr(p_value) + '\n' + txt)

    plt.figure(2)
    sort2seq(model.graph_dout, model.graph_din)

    plt.legend(['out-degree sequence', 'in-degree sequence'])
    plt.xlabel('node')
    plt.ylabel('degree')

    txt = ''
    for para in model.fg.params.items():
        txt += para[0] + ' = ' + "%0.2f" % para[1] + ' '

    plt.title("Correlation: " + repr(corr) + " p-value: " + repr(p_value) + '\n' + txt)