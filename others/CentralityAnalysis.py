import DCMGenerator as dcm_g
import numpy as np
import networkx as nx
import scipy.stats as st
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


# define a remove impact function
## tool function
def max_dic(dic):
    v = list(dic.values())
    k = list(dic.keys())
    return k[v.index(max(v))]


def graph_centra(graph, type="btw"):
    N = nx.number_of_nodes(graph)
    if type == "btw":
        bc_dic = nx.betweenness_centrality(graph)
        bc_list = list(bc_dic.values())
        bcmax = max(bc_list)
        return (N * bcmax - sum(bc_list)) / (N-1)


def imp_remove(dcm, n, rule="pagerank"):
    # copy the graph for manipulation
    graph_copy = dcm.graph
    # the list of centrality
    central = [dcm.graph_centrality]
    if rule == "pagerank":
        rank_copy = dict(dcm.page_rank)
    elif rule == "btwcentrality":
        rank_copy = dict(dcm.betweenness_centrality)

    elim = []  # eliminated list
    for i in range(n):
        node_lab = max_dic(rank_copy)  # node label
        elim += [node_lab]
        rank_copy.pop(node_lab)

        # remove the node
        graph_copy.remove_nodes_from([node_lab])

        # add the graph centrality
        central += [graph_centra(graph_copy)]

    return central, elim

"""
central_1 = imp_remove(DCMlist[0],20)
central_10 = imp_remove(DCMlist[0], 20, rule = "btwcentrality")

# plot
plt2 = plt.figure(2)
plt.title('Graph centrality after eliminating highest ranking node Correlation: 0.968')
plt.xlabel('Eliminate nodes number')
plt.ylabel('Graph betweenness centrality')
plt.plot(central_10, color = 'blue', marker = 'o', markersize = "3")
plt.plot(central_1, color = 'red', marker = 'v', markersize = "3")
plt.legend(['Betweenness centrality', 'Pagerank'])
# check the correlation
st.pearsonr(central_1, central_10)
"""
"""
large_mean = dcm_g.DCMGenerator(4.5, 0.6, 3.8, 1000, 'Erased')

central_1, elim_1_pk = imp_remove(large_mean, 50)
central_10, elim_1_bc = imp_remove(large_mean, 50, rule = "btwcentrality")



little_mean = dcm_g.DCMGenerator(0.5, 1.8, 3.8, 1000, 'Erased')
lxh_little = little_mean.copy()
central_2, elim_2_pk = imp_remove(little_mean, 50)
central_20, elim_2_bc = imp_remove(little_mean, 50, rule = "btwcentrality")

little_mean.in_degree(elim_2_bc)
little_mean.in_degree(elim_2_bc)
"""


