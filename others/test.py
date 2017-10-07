import DCMGenerator as dcm_g
import time
import numpy as np
import matplotlib.pyplot as plt


def test1():
    # assign the parameters
    # [Special Case [Alpha = Beta]]
    a = 1.5  # the lower bound for W+

    alpha = 3  # the power for W+
    beta = 2.5  # the power for W+

    d = beta / alpha

    n = 2000 # graph size



    # generate simple directed configuration model
    dcm = dcm_g.DCMGenerator(a, d, beta, n, 'Erased')

    # plot the bi-degree sequence before and after adjusting to make equal sum
    dcm.test_equal_sum_algorithm()

    # plot the bi-degree distribution to compare with generated simple DCM degree distribution
    dcm.degrees_plot()

    #
    dcm.pr_vs_bc_plot()
    dcm.bc_vs_pr_plot()

    dcm.pr_vs_bc_plot(200)
    dcm.bc_vs_pr_plot(200)

    # calculate the rank corr of the dcm
    corr, pvalue = dcm.spearman_test()

    # check the overlapping in first k-ranked nodes
    overlap_percentage = []
    overlap_number = []
    for k in range(10, 2000, 100):
        num, per = dcm.overlaps(k)
        overlap_number.append(num)
        overlap_percentage.append(per)
        print(k, per)

    return dcm

def test2():
    f = open("results1.txt", 'w+')

    a_range = np.arange(0.6, 1.6, 0.2) # 5 choices

    #beta_range = np.arange(3.2,3.5,0.2) # 2.8, 3.0, 3.2, 3.4
    #d_range = np.arange(1.1, 1.3, 0.2) # 0.6, 0.8, 1.0, 1.2

    beta_range = np.arange(2.5, 3.5, 0.2)  # 2.5, 2.7, 2.9, 3.1, 3.3, # 5 choices
    d_range = np.arange(0.8, 1.3, 0.2)  # 0.8, 1.0, 1.2 # 3 choices
    n = 2000
# 5*5*3= 75
    models = {}
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

                models[i] = model

                s += '\n'
                i += 1

    f.write(s)
    f.close()

    return models

def test3():
    a = 0.6
    beta = 2.6
    d = 1
    n = 2000
    model = dcm_g.DCMGenerator(a, d, beta, n, 'Erased')





def test4():
        models = {}
        import matplotlib.pyplot as plt

        plt.figure()
        ave_deg = {}
        over_per_100 = {}
        over_per_200 = {}

        ave_bc = {}
        ave_pr = {}

        import operator

        for i in range(1, 76):
            model = models[i]
            ave_deg[i] = model.mean_in_degree
            over_per_100[i] = model.overlaps(100)[1]
            over_per_200[i] = model.overlaps(200)[1]

            bc_sort = sorted(model.betweenness_centrality.items(), key=operator.itemgetter(1), reverse=True)
            pr_sort = sorted(model.page_rank.items(), key=operator.itemgetter(1), reverse=True)

            bc_topk = [node[1] for node in bc_sort[0: 100]]
            pr_topk = [node[1] for node in pr_sort[0: 100]]
            ave_bc[i] = sum(bc_topk)/100
            ave_pr[i] = sum(pr_topk)/100

        ave_deg_sorted = sorted(ave_deg.items(), key=operator.itemgetter(1),reverse=True)
        ave_deg_hist = [node[1] for node in ave_deg_sorted]
        over_per_100_hist = [over_per_100[node[0]] for node in ave_deg_sorted]
        over_per_200_hist = [over_per_200[node[0]] for node in ave_deg_sorted]

        ave_bc_hist = [ave_bc[node[0]] for node in ave_deg_sorted]
        ave_pr_hist = [ave_pr[node[0]] for node in ave_deg_sorted]

        plt.plot(ave_deg_hist, over_per_100_hist, color='green', marker='o', label='k=100')
        plt.plot(ave_deg_hist, over_per_200_hist, color='blue', marker='v', label='k=200')

        plt.xlabel('average degree of nodes')
        plt.ylabel('overlapping percentage in tok k nodes')
        plt.legend()
        plt.title('relationship between overlapping percentage and ave degree of nodes')

        plt.figure()

        plt.plot(ave_deg_hist, ave_bc_hist, color='red', marker='o', label='page rank')
        plt.plot(ave_deg_hist, ave_pr_hist, color='cyan', marker='v', label='betweenness centrality')

        plt.xlabel('average degree of nodes')
        plt.ylabel('values')
        plt.legend()
        plt.title('relationship between ave top-100 page rank/betweenness_centrality and ave degree of nodes')



dcm = test1()



