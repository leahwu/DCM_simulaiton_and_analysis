import numpy as np
import PowerLawDistribution as pld
from scipy.stats import poisson
import networkx as nx
import scipy.stats as st
import matplotlib.pyplot as plt

def gene_one_pair(c, beta):
    """
    method to generate one sample (d+, d-)
    :return: tuple with a pair of d+ and d-
    """
    w_sample = pld.generate_w(c, beta)
    # derive the sample degree from W+ and W-
    d = int(poisson(mu=w_sample).rvs())
    return d

def rvs(n, c, beta):
    d_seq = np.zeros(n, dtype=np.int)
    for i in range(0, n):
        d_seq[i] = gene_one_pair(c,beta)

    # resample to get even sum
    while sum(d_seq)%2 == 1:
        d_seq[0] = gene_one_pair(c,beta)

    return d_seq

def Graph_generate(seq):
    # generate the multigraph
    cm = nx.configuration_model(seq)

    # remove parallel edges
    cm = nx.Graph(cm)

    # remove self-loops
    cm.remove_edges_from(cm.selfloop_edges())

    # remove the isolation part
    remove_list = [node for node in cm.nodes() if not ( node in list(max(nx.connected_components(cm), key=len))) ]
    cm.remove_nodes_from(remove_list)

    return cm

# exogeneous parameters
c = 4.33
beta = 30.74
n = 1000


def ranking_spear_corr(graph):
    pr = list(nx.pagerank(graph).values())
    bc = list(nx.betweenness_centrality(graph).values())
    rw = list(nx.current_flow_betweenness_centrality(graph).values())

    corr1, pvalue1 = st.spearmanr(pr, bc)
    corr2, pvalue2 = st.spearmanr(pr, rw)
    corr3, pvalue3 = st.spearmanr(bc, rw)


    return [corr1, corr2, corr3]


<<<<<<< HEAD
rankcorr1 = []
rankcorr2 = []
rankcorr3 = []

for i in range(100):
    graph_temp = Graph_generate( rvs(n,c,beta) )
    rankcorr1 += [ranking_spear_corr(graph_temp)[0]]
    rankcorr2 += [ranking_spear_corr(graph_temp)[1]]
    rankcorr3 += [ranking_spear_corr(graph_temp)[2]]

mean_rankcorr = [np.mean(rankcorr1), np.mean(rankcorr2), np.mean(rankcorr3)]


 # nodes = [str(node[0]) for node in pr_sort ]
pr = nx.pagerank(graph_temp)
bc = nx.betweenness_centrality(graph_temp)
rw = nx.current_flow_betweenness_centrality(graph_temp)
pr_sort = sorted(pr.items(), key=operator.itemgetter(1), reverse=True)

pr_scores = [node[1] for node in pr_sort]
bc_scores = [bc[node[0]] for node in pr_sort]
rw_scores = [rw[node[0]] for node in pr_sort]
plt.figure(1)
plt.plot(bc_scaled_scores[0: k], 'bx', markersize=3)
plt.plot(pr_scores[0: k], 'ro', markersize=1)
plt.plot(rw_scores[0:k], 'gv', markersize=1)


