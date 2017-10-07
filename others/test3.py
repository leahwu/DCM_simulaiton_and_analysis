import DCMGenerator as dcm_g
import time
import numpy as np

def test3():
    f = open("results3.txt", 'w+')

    a_range = np.arange(1,4, 1) # 4 choices


    beta_range = np.arange(3)
    d_range = np.arange(1, 2, 0.5)  # 2 choices
    n = 2000
# 5*5*3= 75
    models3 = {}
    s = 'ALl the graph\'s size is ' + repr(n) + '.\n'
    i = 1
    for a in a_range:
        for beta in beta_range:
            for d in d_range:
                print(i)
                s += "Model"+ repr(i) +":\n"
                model = dcm_g.DCMGenerator(a, d, beta, n, 'Erased')
                s += '\n'

                s += "The params are:\n"
                for para in model.fg.params.items():
                    s += para[0] + ' = ' + "%0.5f" % para[1] + '\n'
                s += '\n'

                s += "Expectation of W^minus is " + repr(model.fg.e_w_minus) +'\n'
                s += "Expectation of W^plus is " + repr(model.fg.e_w_plus) + '\n'
                s += '\n'

                s += "Mean of original in-degree sequence is " + repr(model.mean_original_in_seq) + '\n'
                s += "Mean of original out-degree sequence is " + repr(model.mean_original_out_seq) + '\n'
                s += '\n'

                s += "After being modified by Algorithm 2.1, \n"
                s += "Mean of equal-sum in-degree sequence is " + repr(model.mean_equal_sum_in_seq) +'\n'
                s += "Mean of equal-sum out-degree sequence is " + repr(model.mean_equal_sum_out_seq) + '\n'
                s += '\n'

                s += "After removing self-loops and parallel edges:\n"
                s += "Mean of in-degree sequence is " + repr(model.mean_in_degree) + '\n'
                s += "Mean of out-degree sequence is " + repr(model.mean_out_degree) + '\n'
                s += '\n'

                s += "The percentage of overlapping nodes in top k ranked nodes by bc, and pr are:\n"
                s += "k\t : \t percentage of overlapping nodes \n"
                for k in range(50, 2000, 50):
                    s += repr(k) + '\t : \t' + repr(model.overlaps(k)[1]) + '\n'
                s += '\n'

                s += "Spearsman's rank correlation test:\n"
                corr, pvalue = model.spearman_test()
                s += "correlation = " + repr(corr) + ", pvalue = " + repr(pvalue) + "\n"

                models3[i] = model

                s += '\n'
                i += 1

    f.write(s)
    f.close()

    return models3

test3()