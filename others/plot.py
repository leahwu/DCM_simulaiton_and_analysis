import DCMGenerator as dcm_g
import time
import numpy as np
import matplotlib.pyplot as plt
import operator

def test5():
    ave_degree = [0.071, 0.3025, 2.946, 11.3135 ] # m13, m16,14, m9
    per_top50 = [0.08, 0.26, 0.38, 0.86, ]
    per_top100 = [0.12, 0.3, 0.43,0.81, ]
    per_top150 =[0.21, 0.31, 0.45, 0.83,]
    per_top200 = [0.42, 0.37, 0.47, 0.845, ]

    plt.figure()

    plt.plot(ave_degree, per_top50, color='green', marker='o', label='k=50')
    plt.plot(ave_degree, per_top100, color='red', marker='v', label='k=100')
    plt.plot(ave_degree, per_top150, color='yellow', marker='o', label='k=150')
    plt.plot(ave_degree, per_top200, color='blue', marker='v', label='k-200')

    plt.xlabel('average degree of nodes')
    plt.ylabel('overlapping percentage of top k nodes')

    plt.legend()
    plt.title('Overlapping percentage as average degree of nodes increases')

