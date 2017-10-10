# DCM_simulaiton_and_analysis

This project aims to simulate and analyze Directed Configuration Model. A complete introduction and report on the project is in [Final_Report.pdf](https://github.com/leahwu/DCM_simulaiton_and_analysis/blob/master/FinalReport.pdf). 

The algorithm to simulate DCM is described in the paper [Directed Random Graphs with Given Degree Distributions]( https://arxiv.org/pdf/1207.2475.pdf)(Ningyuan Chen and Mariana Olvera-Cravioto, July 12, 2012). And the [codes]( https://github.com/leahwu/DCM_simulaiton_and_analysis/tree/master/codes)(Python) are mainly implemented by [networkx package](https://networkx.github.io/documentation/networkx-1.11/).

The research is conducted with the guidance from professor [Mariana Olvera-Cravioto](http://olvera.ieor.berkeley.edu/). The github contents are created by Luhuan Wu and Xiaohui Li. 

Lastly, we would like to express our sincere gratitude to our nice project supervisor professor Mariana.

## Description of files:

## Folder: final_images

This includes the images being used in final_report.

## Folder: weekly_reports

This includes the reports on weekly progress.

## Folder: codes

This includes all the python functions in applying numerical simulation and analysis. Specifically, the *DCMGenerator.py* is the core function in generating the **DCM graph** from valid sample **degree sequences**, which are yielded from *PowerLawDistribution.py* and *ValidDegree.py*. *AnalysisToolFunction.py* offers analytical tools in computation and data analysis of the main research study procedure. 

All the scripts are written in Python 3.5. Note the ASPL study part may be very time consuming since ASPL computation runs in exponential theta N. Also the DCM generation may be quite long given large difference between in and out-degree power index, which causes the algorithm to take much more time. 

## Folder: Output_data

Note that using the edge sequence data, one could recover the graph.

### Folder: part1\_case1 and part2\_case2

*case1(2)_info.xlsx* is a small excel file that stores **the parameter of the model, and the degree correlation and rank correlation of each of 20 samples, and their average**, in 6 dependency levels(d=0, 0.2, 0.4, 0.6, 0.8, 1.0).

*result_i_.xlsx* (i=1,2,3,4,5,6) stores the detailed information of 20 samples in a dependency level, which includes **in and out degree sequence, PR, BC and edge sequence**. Those are **large files (around 100.MB)** that take time to download and open.

### Folder: models3_wiki_vote_simulation

There are 10 samples independently generated from a model used to simulate the Wiki_vote networkd, the detailed information of which are  *model_i_.xlsx*(i=1,2,3,4,5,6,7), including **parameters, in-degree, out-degree, PR, BC, edge sequence, label of the removed node, AverageShortestPathLength(ASPL) and number of the nodes being removed in each time subsequently**. Specifically for the sheet containing the last item: label of the nodes being removed subsequently, the index denotes the i th ranking node subsequently being eliminated. The corresponding value to a specific measure(PC, BR, etc) denotes the label of the node in the graph ( all the nodes are labeled from 0 to n - 1 where n is the size of the graph).

### Folder: models2_ASPL_analysis 

The *d(…)ASPL.csv* files save the generated models’ **ASPL values** with eliminating node.

In total there are 6 files corresponding to 6 cases for degree of correlation. Respectively, the “0.0”, “0.25”, “0.5”, “0.75”, “1.0” and “same” represent where value d = 0.0, 0.25 … and the degree perfectly correlated case that in-degree equals to out-degree.

Specifically for each csv, the row index i denotes the i th ranking node subsequently being eliminated. The column lists the specific simulated model (sample1 to sample5 and the mean) using one of the ranking method (BC, PR, Total Degree, In Degree and Out Degree). The value is the ASPL after consecutively eliminating the i th node given particular model and ranking method.

### Folder: wiki_vote

*wiki-Vote.txt* are downloaded from [here](https://snap.stanford.edu/data/wiki-Vote.html), which stores the edge sequence of Wiki-vote network.

*din.txt*, *dout.txt*, bc.txt* and *pr.txt* stores the in-degree sequence, out-degreequence, BC and PR values of the nodes.

*ASPL.xlsx* stores the information in Node-elimination experiment, including **index of the removed node, AverageShortestPathLength(ASPL) and number of the nodes being removed in each time subsequently**.