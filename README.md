# DCM_simulaiton_and_analysis



Description of files in output_data.zip

The d(…)ASPL.csv data files saves the generated models’ ASPL values with eliminating node.

In total there are 6 files corresponding to 6 cases for degree of correlation. Respectively, the “0.0”, “0.25”, “0.5”, “0.75”, “1.0” and “same” represent where value d = 0.0, 0.25 … and the degree perfectly correlated case that in-degree equals to out-degree.

Specifically for each csv, the row index i denotes the i th ranking node subsequently being eliminated. The column lists the specific simulated model (sample1 to sample5 and the mean) using one of the ranking method (BC, PR, Total Degree, In Degree and Out Degree). The value is the ASPL after consecutively eliminating the i th node given particular model and ranking method.
