import DCMGenerator as dcm
import PowerLawDistribution as pld
import  validate as vd
import numpy as np
from math import sqrt
import scipy.stats as st
import matplotlib.pyplot as plt
from scipy import stats
import networkx as nx
import operator
import pandas as pd


def max_dic(dic):
    v = list(dic.values())
    k = list(dic.keys())
    return k[v.index(max(v))]

def get_b(a, alpha, beta):
    """for alpha != beta"""
    if alpha == beta:
        raise ValueError('Compute the value of b for alpha != beta only!')
    return (alpha / (alpha - 1) * (beta - 1) / beta * a ** (alpha / beta)) ** (beta / (alpha - beta))

def get_corr(a, alpha, beta, b=None):

    if b is None:
        b = get_b(a, alpha, beta)

    d = beta / alpha

    c = alpha / (alpha - 1) * b * (beta - 1) / beta

    e_d_in = b * alpha / (alpha - 1)
    print(e_d_in)

    e_d_out = c * beta / (beta - 1)
    print(e_d_out)

    e_w_plus_square = alpha * b ** 2 / (alpha - 2)
    print("e_wp_2", e_w_plus_square)

    e_w_minus_square = beta * c ** 2 / (beta - 2)
    print("e_wm_2", e_w_minus_square)

    e_prod = a * beta * c ** (d + 1) / (beta - d - 1)
    print("e_prod", e_prod)

    var_d_in = e_d_in + e_w_plus_square - e_d_in ** 2
    var_d_out = e_d_out + e_w_minus_square - e_d_out ** 2

    corr = (e_prod - e_d_in * e_d_out) / sqrt(var_d_in * var_d_out)

    return corr


def graph_remove(digraph, s, rule="pagerank"):
    """
    
    :param digraph: 
    :param s: top s nodes to be removed
    :param rule: 
    :return: tuples:
    digraph: the original graph
    graph_copy: the graph after eliminating top s ranked nodes
    elim: the label of nodes being eliminated
    scc_node: number of nodes in the largest scc
    """

    #remove the top-n-ranked nodes subsequently
    # number of nodes leads to disconnectivity
    count_discon = 0
    # copy the graph for manipulation
    graph_copy = nx.Graph.copy(digraph)
    # average shortest path, index 0 -original, index 1 - after removing top-ranked page rank(or bc)  node, and so on
    ave_sp = []
    ave_sp.append(nx.average_shortest_path_length(digraph))
    # rankcopy
    if rule == "pagerank":
        rank_copy = nx.pagerank(digraph)
    elif rule == "btwcentrality":
        rank_copy = nx.betweenness_centrality(digraph)
    elif rule == "totaldeg":
        rank_copy = digraph.degree()
    elif rule == "indeg":
        rank_copy = digraph.in_degree()
    elif rule == "outdeg":
        rank_copy = digraph.out_degree()

    elim = []  # eliminated list
    scc_node = [] # number of nodes in the largest strongly components

    for i in range(s):
        node_label = max_dic(rank_copy)
        elim += [node_label]
        rank_copy.pop(node_label)
        graph_copy.remove_node(node_label)

        #largest Strongly Connected Components
        scc_i = max(nx.strongly_connected_component_subgraphs(graph_copy), key=len)  # the largest scc

        ave_sp.append(nx.average_shortest_path_length(scc_i))
        scc_node.append(scc_i.number_of_nodes())

    return digraph, graph_copy, elim, ave_sp, scc_node


def graph_remove_indep(digraph, s,  rule="pagerank"):
    #remove the top-s-ranked node independently
    # number of nodes leads to disconnectivity
    count_discon = 0
    # average shortest path, index 0 -original, index 1 - after removing top-ranked page rank(or bc)  node, and so on
    ave_sp = []
    ave_sp.append(nx.average_shortest_path_length(digraph))

    if rule == "pagerank":
        rank_copy = nx.pagerank(digraph)
    elif rule == "btwcentrality":
        rank_copy = nx.betweenness_centrality(digraph)
    elif rule == "totaldeg":
        rank_copy = digraph.degree()
    elif rule == "indeg":
        rank_copy = digraph.in_degree()
    elif rule == "outdeg":
        rank_copy = digraph.out_degree()


    elim = []  # eliminated list
    for i in np.arange(1, s + 1):
        # copy the graph for manipulation
        graph_copy = nx.Graph.copy(digraph)

        node_label = max_dic(rank_copy)
        elim += [node_label]
        rank_copy.pop(node_label)
        graph_copy.remove_node(node_label)

        #largest strongly connected component
        scc_i = max(nx.strongly_connected_component_subgraphs(graph_copy), key=len)

        ave_sp.append(nx.average_shortest_path_length(scc_i))

    return digraph, graph_copy, elim, ave_sp


def cons_mean_graph(alpha, d, E, n=2000, algo="Erased", iden=False, dependency = True):
    # use alpha, d, and E three parameters to derive graph
    beta = alpha * d
    b = E * (alpha - 1)/alpha
    c = E * (beta - 1)/beta
    a = b / c ** (beta/alpha)
    print("The corresponding a should be", a)
    # calculate the correlation of in-/ out- deg sequence
    theo_corr = get_corr(a, alpha, beta, b)
    print("Correlation: ",theo_corr)

    gen_dcm = dcm.DCMGenerator(a, alpha, beta, n, algo, b=b, iden=iden, dependency = dependency)

    return gen_dcm.graph

def test_connected():
    alpha = 3
    d = 1.5
    E = range(5,201,1)
    num_compo = []
    num_giant_node = []
    giant_component = []
    for e in E:
        mean = e/10
        digraph_e = cons_mean_graph(alpha, d, mean)
        num_compo.append(nx.number_strongly_connected_components(digraph_e))
        Gcc = sorted(nx.strongly_connected_component_subgraphs(digraph_e), key=len, reverse=True)
        G0 = Gcc[0]
        num_giant_node.append(G0.number_of_nodes())
        giant_component.append(G0)
    return num_compo, num_giant_node, giant_component


def test_corr(alpha=3, mean=3):
    E = mean
    d_lst = range(10001,100001,1)

    corr = []
    for d in d_lst:
        d_e = d/10000
        beta = alpha * d_e
        b = E * (alpha - 1) / alpha
        c = E * (beta - 1) / beta
        a = b / c ** (beta / alpha)
        corr_d = get_corr(a, alpha, beta, b=b)
        corr.append(corr_d)
    return corr


def sort_dict(d):
    sort = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
    return sort

def plot_result(result):
    # get the avgshortpath
    path_pk = result[0][2]
    path_bc = result[1][2]
    path_tot = result[2][2]
    path_in = result[3][2]
    path_out = result[4][2]
    plt.plot(path_pk)
    plt.plot(path_bc)
    plt.plot(path_tot)
    plt.plot(path_in)
    plt.plot(path_out)
    plt.legend(['Page rank', 'Btw centrality', "Total degree", "In degree",'Out degree'])
    plt.suptitle('Average short path after eliminating node based upon different ranking')
    plt.title('Giant Component Size:  Expected mean:   Correlation: ')



def test_empirical_corr(result):
    graph = result[0][0]
    d_in = [v for v in graph.in_degree().values()]
    d_out = [v for v in graph.out_degree().values()]
    corr, p = st.pearsonr(d_in, d_out)
    return corr

def test_plot(result):
    path_pr = result[0][2]
    path_bc = result[1][2]
    path_tot = result[2][2]
    path_in = result[3][2]
    path_out = result[4][2]

    plt.plot(path_pr)
    plt.plot(path_bc)
    plt.plot(path_tot)
    plt.plot(path_in)
    plt.plot(path_out)


    plt.suptitle('Different ranking node effect on average short path [Perfectly correlated]')
    plt.title('Giant size:   Expected mean:  Correlation: ')
    plt.xlabel("Node eliminated")
    plt.ylabel('Average short path')
    plt.legend(['Page rank', 'Btw Centrality', 'Total degree', 'In degree', 'Out degree'])


def gen_coh_model(alpha, beta, E, d, n=2000):
    """
    :param alpha: 
    :param beta: 
    :param E: 
    :param d: 
    :param n: 
    :return: generate coherent model
    """
    return dcm.DCMGenerator(alpha, beta, E, d, n)


def test_shortpath_marginal_2(graph, s):
    """
    
    :param graph:
    :param s: top s nodes to be removed
    :return: 
    """
    result = []
    # digraph
    digraph_whole = graph

    Gcc = nx.strongly_connected_component_subgraphs(digraph_whole)
    digraph_giant = max(Gcc, key=len)
    print("GiantComponent: ", digraph_giant.number_of_nodes())

    oldgraph, graph_pr, elim_pr, shortpath_pr, scc_node_pr = graph_remove(digraph_giant, s=s, rule="pagerank")
    oldgraph, graph_bc, elim_bc, shortpath_bc, scc_node_bc = graph_remove(digraph_giant, s=s, rule="btwcentrality")
    oldgraph, graph_total, elim_total, shortpath_total, scc_node_total = graph_remove(digraph_giant, s=s,
                                                                                      rule="totaldeg")
    oldgraph, graph_indeg, elim_indeg, shortpath_indeg, scc_node_indeg = graph_remove(digraph_giant, s=s, rule="indeg")
    oldgraph, graph_outdeg, elim_outdeg, shortpath_outdeg, scc_node_outdeg = graph_remove(digraph_giant, s=s,
                                                                                          rule="outdeg")

    result.append([graph_pr, elim_pr, shortpath_pr, scc_node_pr])
    result.append([graph_bc, elim_bc, shortpath_bc, scc_node_bc])
    result.append([graph_total, elim_total, shortpath_total, scc_node_total])
    result.append([graph_indeg, elim_indeg, shortpath_indeg, scc_node_indeg])
    result.append([graph_outdeg, elim_outdeg, shortpath_outdeg, scc_node_outdeg])
    result.append(oldgraph)

    return result


def plot_ave(result):
    plt.plot(result[0][2], label='page rank')
    plt.plot(result[1][2], label='betweenness centrality')
    plt.plot(result[2][2], label='total degree')
    plt.plot(result[3][2], label='in degree')
    plt.plot(result[4][2], label='out degree')

    plt.legend()
    plt.ylabel('Average shortest path length')
    plt.xlabel('Rank of the nodes eliminated subsequently')


# wrtie to excel function

def to_df(result, i):
    # write into a DataFrame
    # i stands for result[j][i] the i_th item

    l = len(result[0][i])
    df = pd.DataFrame({'PR': result[0][i], 'BC': result[1][i],
                       'total_degree': result[2][i],
                       'in_degree': result[3][i],
                       'out_degree': result[4][i]}, index=np.arange(1, l + 1, 1))
    df.index.name = '#nodes being removed'
    if i == 1:
        df.name = 'index of the removed node'
    if i == 2:
        df.name = 'ave_short_path_length'
    if i == 3:
        df.name = '#nodes in largest scc'
    return df


def d_tolist(d):
    # convert the values of a dict to a list
    return list(d.values())


def multiple_dfs(df_list, sheets, file_name, spaces):
    writer = pd.ExcelWriter(file_name,engine='xlsxwriter')
    row = 0
    for dataframe in df_list:
        dataframe.to_excel(writer,sheet_name=sheets,startrow=row , startcol=0)
        row = row + len(dataframe.index) + spaces + 1
    writer.save()


def model_to_df(model, params, giant=None):
    # write the basic info of the model to df, including:

    # params should include at least: alpha, beta, b, c, d, s, E, computed corr (and Giant component)

    df1 = pd.DataFrame(params, index=['value'])
    df1.name = 'parameters'

    # add corr
    df1['sample degree corr'] = model.corr_in_and_out()[0]
    df1['p-value for sample degree corr'] = model.corr_in_and_out()[1]
    if giant is not None:
        df1['size of giant component'] = giant

    # in degree sequence, out degree sequence, pr, bc
    df2 = pd.DataFrame({'in_degree': model.d_in, 'out_degree': model.d_out, 'PR': d_tolist(model.page_rank),
                       'BC': d_tolist(model.betweenness_centrality)})
    df2.index.name = 'node index'
    df2.name = 'in, out, pr, and bc'


    #edge sequences
    df3 = pd.DataFrame(model.graph.edges(), columns=['from', 'to'])
    df3.name = 'edge sequence'


    return df1, df2, df3


def model_to_excel(file_path, model, result, params, giant=None):
    dfs = model_to_df(model, params, giant)
    writer = pd.ExcelWriter(file_path)
    for df in dfs:
        df.to_excel(writer, sheet_name=df.name)

    for i in [1, 2, 3]:
        df = to_df(result, i)

        df.to_excel(writer, sheet_name=df.name)

    writer.save()
