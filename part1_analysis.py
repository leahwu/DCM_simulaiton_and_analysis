import DCMGenerator as dcm
import PowerLawDistribution as pld
import numpy as np
from AnalysisToolFunction import gen_coh_model
from AnalysisToolFunction import d_tolist
from TheoreticalFunctionTool import get_corr_new_version as get_corr
import matplotlib.pyplot as plt
import pandas as pd

def params_to_df(params):
    # write the basic info of the model to df, including:

    # params should include at least: alpha, beta, b, c, d, s, E, computed corr (and Giant component)

    df1 = pd.DataFrame(params, index=['value'])
    df1.name = 'parameters'

    # add corr
    df1['computed degree correlation'] = get_corr(params['alpha'], params['beta'], params['Expected degree'], params['d'])

    return df1


def sample_model_to_df(models):
    dfs = []
    i = 1

    df_corrs = pd.DataFrame(index=['sample degree correlation', 'p-value(degree)', 'sample rank correlation',
                                   'p-value(rank)'])
    for model in models:
        df_corrs['Sample' + repr(i)] = [model.graph_corr[0], model.graph_corr[1], model.BC_PR_corr[0],
                                              model.BC_PR_corr[1]]

        # in degree sequence, out degree sequence, pr, bc
        df2 = pd.DataFrame({'in_degree': model.d_in, 'out_degree': model.d_out, 'PR': d_tolist(model.page_rank),
                            'BC': d_tolist(model.betweenness_centrality)})
        df2.index.name = 'node index'
        df2.name = 'Sample' + repr(i) + '_in,out,pr,bc'


        #edge sequences
        df3 = pd.DataFrame(model.graph.edges(), columns=['from', 'to'])
        df3.name = 'Sample' + repr(i) + '_edge sequence'

        i += 1

        dfs.append(df2)
        dfs.append(df3)

    return dfs, df_corrs


def models_to_excel(file_path, models, params, spaces=2):
    dfs, dfs_corrs = sample_model_to_df(models)
    df1 = params_to_df(params)

    writer = pd.ExcelWriter(file_path, engine='xlsxwriter')
    row = 0
    for dataframe in [df1, dfs_corrs]:
        dataframe.to_excel(writer, sheet_name='params and corrs', startrow=row, startcol=0)
        row = row + len(dataframe.index) + spaces + 1

    for df in dfs:
        df.to_excel(writer, sheet_name=df.name)

    writer.save()


def multiple_dfs(df_list, sheetname, file_name, spaces):
    writer = pd.ExcelWriter(file_name,engine='xlsxwriter')
    row = 0
    for dataframe in df_list:
        dataframe.to_excel(writer,sheet_name=sheetname,startrow=row , startcol=0)
        row = row + len(dataframe.index) + spaces + 1
    writer.save()

"""
alpha = 3
beta = 3
exp_deg = 20

d_list = np.arange(0, 1.2, 0.2)

n = 5000

for d in d_list:
    for i in range(0, 19):
        model = gen_coh_model(alpha, beta, exp_deg, d, n)

        models.append(model)

"""
# TODO: model to excel, record edge lists, din, dout, pr, bc, corr, params
# TODO: plot the graphs 1) tail distribution, 2) pr v.s. bc 3)overall


def test():
    models1 = []
    models2 = []
    models3 = []
    models4 = []
    models5 = []
    alpha = 3
    beta = 3
    exp_deg = 20
    n = 5000
    for i in range(0, 19):
        m1 = gen_coh_model(alpha, beta, exp_deg, 0.2, n)
        models1.append(m1)

        m2 = gen_coh_model(alpha, beta, exp_deg, 0.4, n)
        models2.append(m2)

        m3 = gen_coh_model(alpha, beta, exp_deg, 0.6, n)
        models3.append(m3)

        m4 = gen_coh_model(alpha, beta, exp_deg, 0.8, n)
        models4.append(m4)

        m5 = gen_coh_model(alpha, beta, exp_deg, 1.0, n)
        models5.append(m5)

    return models1, models2, models4, models4, models4, models5


def get_rank_corr(models):
    rc = []
    for m in models:
        rc.append(m.BC_PR_corr[0])

    rc = np.array(rc)

    return rc