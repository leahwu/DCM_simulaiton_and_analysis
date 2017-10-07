import DCMGenerator as dcm
import numpy as np
import networkx as nx
import scipy.stats as st
import matplotlib.pyplot as plt

graph_lst = []
"""a = 1
alpha = 3
beta = 3
b_lst = range(10,101,1)
n = 5000
for i in b_lst:
    temp = []
    blst = []
    b_i = i/10
    blst.append(b_i)
    for i in range(50):
        temp.append(dcm.DCMGenerator(a, alpha, beta, n, 'Erased', b = b_i))
    graph_lst.append(temp)"""

alpha = 7
beta = 4
a = 4.5
n = 5000
graph_lst.append(dcm.DCMGenerator(a, alpha, beta, n, 'Erased'))