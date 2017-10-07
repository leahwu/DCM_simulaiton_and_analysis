# ReportIII

Luhuan Wu, Xiaohui Li

June 12, 2017

## 1. Procedures

We test the parameters set:

~~~Python
a_range = np.arange(0.5, 5, 0.5)  
beta_range = np.arange(2.6, 6.0, 0.4)  
d_range = np.arange(0.6, 2.5, 0.4)
n = 2000 # graph size
~~~

with the restrictions that:
$$
\beta > 2d, \beta > d + 1
$$
In one simulation experiment, we get 158 models in total, and we repeat the simulation for 3 times.

We want to see the relationship between

- mean degree of in sequence

- correlation between in-degree sequence and out-degree sequence

  - calculated by pearson's correlation
    $$
    \rho_{xy} = \frac{\sum_{i=1}^n(x_i - \bar{x})(y_i-\bar{y})}{\sqrt{\sum_{i=1}^n(x_i-\bar{x})^2} \sqrt{\sum_{i=1}^n(y_i-\bar{y})^2}}
    $$
    ​

- correlation between distribution of in-degree sequence and out-degree sequence

- rank correlation between page rank and betweenness centrality

  - calculated by spearman's test

Since one simulation test takes time over 1 hours, we only carry out 3 simulation tests. However, we choose one parameter set and perform monte carlo simulation for 100 times to oberserve the changes in topology of the generated 100 graphs. We can find that the standard deviation of each indicator is significantly close to 0, and the plots of correlation between degree sequence, correlation between degree distribution and tail distribution of page rank and betweenness centrality are stable. So it is reasonable to conclude the result from limited number of simulations.

```python
m = 100 # simulation times 
 a=1
 d=1
beta = 3
n = 1000 # graph size
mean_in_degree.mean = 3.0133899999999998
mean_in_degree.std = 0.062115520604757057
mean_out_degree.mean = 3.0133899999999998
mean_out_degree.std = 0.062115520604757057
rank_corr.mean = 0.68347056501000647
rank_corr.std = 0.023911565464571523
degree_corr.mean = 0.46876618523851193
degree_corr.std = 0.095619158013208042
degree_dist_corr.mean = 0.99344912725957468
degree_dist_corr.std = 0.0036223674398349706
```

![monte_carlo_1](/Users/leah/summer_2017/Go_graphs/week3_images/extra/monte_carlo_1.png)

![monte_carlo_2](/Users/leah/summer_2017/Go_graphs/week3_images/extra/monte_carlo_2.png)

![monte_carlo_3](/Users/leah/summer_2017/Go_graphs/week3_images/extra/monte_carlo_3.png)

## 2. Overall results

After testing for 3 simulations, the results are similar. In the above we always list the numerical outcome of simulation experiment II, unless specified.

We find out that

1. Correlation of mean degree of in sequence and rank correlation is: 0.81575916026408302

   ~~~python
   st.pearsonr(mean_in_degree, rank_corr)
   Out[129]: (0.81575916026408302, 6.2862585534006831e-39)
   ~~~

   ![mean_rank](/Users/leah/summer_2017/Go_graphs/week3_images/mean_rank.png)

   To make the plot more obvious, we log sclae the mean_in_degree and 10 times the rank correlation:

   ![mean_rank_transfrom copy](/Users/leah/summer_2017/Go_graphs/week3_images/mean_rank_transfrom copy.png)

   In spite of this strong correlation, we further investigate into specific models and find out that the mean-in-degree is not the cause for changes in pr and bc correlation.

2. Correlation between rank correlation and degree sequence correlation is positive,

   Correlation between rank correlation and degree distribution correlation is negative,

   Correlation between degree sequence correlation and degree distribution correlation is negative.

   ~~~python
   st.pearsonr(rank_corr, degree_corr)
   Out[130]: (0.75489721279463329, 2.2158379823272034e-30)
   st.pearsonr(rank_corr, degree_dist_corr)
   Out[131]: (-0.80254656595813345, 8.0185868478995638e-37)
   st.pearsonr(degree_dist_corr, degree_corr)
   Out[132]: (-0.63391504054881398, 3.8898782090839996e-19)
   ~~~

![result](/Users/leah/summer_2017/Go_graphs/week3_images/result.png)

correlation of degree distirbution varies from 0.87409202256697371 to 0.99960502861299561.

correlation of degree sequence varies from 0.022920331371940932 to 0.93310820292999586.

rank correlation varies from  0.58763471703073589 to  0.84779853194963295.

mean degree of in sequence varies from 2.076 to 42.1775.

![rank_degree_dist](/Users/leah/summer_2017/Go_graphs/week3_images/rank_degree_dist.png)

![rank_degree](/Users/leah/summer_2017/Go_graphs/week3_images/rank_degree.png)

3. - As the correlation of degree distribution gets larger, the gap between tail distirbution plot of PR and BC gets larger;

   ![dist_comparison_5_models](/Users/leah/summer_2017/Go_graphs/week3_images/dist_comparison_5_models.png)

   m60, m48, m59, m39, m26 are models in degreasing order of correlation of in and out degree sequence distribution.

   - As the correlation of degree sequence gets larger, the gap between tail distirbution plot of PR and BC gets smaller.

   ![3_models_compare](/Users/leah/summer_2017/Go_graphs/week3_images/extra/3_models_compare.png)

   m103, m140, m37 are models in increasing of correlation of degree sequence.

4. Since the range of degree sequence [0.87409202256697371, 0.99960502861299561] is much larger than the range of degree distribution [0.022920331371940932 to 0.93310820292999586], we consider the former one is a more indicative for rank correlation. In addition, we find thee is a positive correlation between rank correlation and degree sequence correlation ,we therefore speculate that there should be a strong positive correlation of such in **undirected graph**, since in that case we can condiser an undirected edge is both in-edge and out-edge. The simulation results confirm this conjecture.

## 3. Further insepection of specific models

### 3.1 mean-in-degree and rank correlation

Although there is storng positive correlation between mean in degree and rank correlation, which is  0.81575916026408302, we further choose the model with biggest mean in degree and smallest mean in degree over 158 models to obsert the ranking correlation.

**model7**, mean in degree : 2.076

![m7](/Users/leah/summer_2017/Go_graphs/week3_images/m7.png)

**model156**: mean in degree: 42.1775.

![m156](/Users/leah/summer_2017/Go_graphs/week3_images/m156.png)



### 3.2 Rank correlation and Degree sequence distribution correlation

m60, m48, m59, m39, m26 are models in degreasing order of correlation of in and out degree sequence distribution.

![dist_comparison_5_models](/Users/leah/summer_2017/Go_graphs/week3_images/dist_comparison_5_models.png)

From the figure above, we could find out that:

As correlation between in and out degree sequence distribution gets smaller, the gap between page rank plot and betweenness centrality plot gets wider. 

Choosing three models that has decreasing correlation of in and out degree sequence distribution(from least, to meadin, to largest of all 158 models), we could see the correlation between page rankd and betweenness centrality gets closer to 1, as the figures below suggest.

![figure_1](/Users/leah/summer_2017/Go_graphs/week3_images/figure_1.png)

![figure_3](/Users/leah/summer_2017/Go_graphs/week3_images/figure_3.png)

![figure_5](/Users/leah/summer_2017/Go_graphs/week3_images/figure_5.png)

![figure_2](/Users/leah/summer_2017/Go_graphs/week3_images/figure_2.png)

![figure_4](/Users/leah/summer_2017/Go_graphs/week3_images/figure_4.png)

![figure_6](/Users/leah/summer_2017/Go_graphs/week3_images/figure_6.png)

## 3.3 Rank correlation and Degree sequence correlation

The result of simulation test 1.

![2corr_1](/Users/leah/summer_2017/Go_graphs/week3_images/extra/2corr_1.png)

![2corr_2](/Users/leah/summer_2017/Go_graphs/week3_images/extra/2corr_2.png)

**Model 103**

**The Least Correlation between in-degree sequence and out-degree sequence** :

0.044718105348935430

![m103_2](/Users/leah/summer_2017/Go_graphs/week3_images/extra/m103_2.png)

![m103_1](/Users/leah/summer_2017/Go_graphs/week3_images/extra/m103_1.png)

![m103_2](/Users/leah/summer_2017/Go_graphs/week3_images/extra/m103_tail_dist.png)

![m103_3](/Users/leah/summer_2017/Go_graphs/week3_images/extra/m103_3.png)

![m103_4](/Users/leah/summer_2017/Go_graphs/week3_images/extra/m103_4.png)

~~~Python
Spearsman's rank correlation test:
correlation = 0.61738611373679264, pvalue = 1.752035270814187e-210
~~~

**Model 37**

**The median correlation between in-degree sequence and out-degree sequence**:

0.32488658335085691

![m37_2](/Users/leah/summer_2017/Go_graphs/week3_images/extra/m37_2.png)

![m37_1](/Users/leah/summer_2017/Go_graphs/week3_images/extra/m37_1.png)

![m37_tail_dist](/Users/leah/summer_2017/Go_graphs/week3_images/extra/m37_tail_dist.png)

![m37_3](/Users/leah/summer_2017/Go_graphs/week3_images/extra/m37_3.png)

![m37_4](/Users/leah/summer_2017/Go_graphs/week3_images/extra/m37_4.png)

```
pearsman's rank correlation test:
correlation = 0.659347253368334, pvalue = 8.4941213542280846e-250
```



**model140**

**The Highest Correlation between in-degree sequence and out-degree sequence** :

0.84605658710738418

![m140_1](/Users/leah/summer_2017/Go_graphs/week3_images/extra/m140_2.png)

![m140_1](/Users/leah/summer_2017/Go_graphs/week3_images/extra/m140_1.png)

![m140_tail_dist](/Users/leah/summer_2017/Go_graphs/week3_images/extra/m140_tail_dist.png)

![m140_3](/Users/leah/summer_2017/Go_graphs/week3_images/extra/m140_3.png)

![m140_4](/Users/leah/summer_2017/Go_graphs/week3_images/extra/m140_4.png)

```
Spearsman's rank correlation test:
correlation = 0.85050471562617891, pvalue = 0.0
```

### Comparison:

![3_models_compare](/Users/leah/summer_2017/Go_graphs/week3_images/extra/3_models_compare.png)

|      | degree_corr         | rank_corr           | degree_dist_corr    |
| ---- | ------------------- | ------------------- | ------------------- |
| m103 | 0.04471810534893543 | 0.61738611373679264 | 0.99521686806398157 |
| m37  | 0.32488658335085691 | 0.659347253368334   | 0.99790203298044999 |
| m140 | 0.84605658710738418 | 0.85050471562617891 | 0.86526730290117526 |



## 4. Undirected models

We consider the case where in-degree and out-degree is perfectly correlated, i.e. they are the same, and the graph could be simplified as an undirected graph. For the undirected models, we test the parameters set:

~~~Python
c = 4.33
beta = 30.74
n=1000 # graph size
m = 100 # simulation times
~~~

The ranking correlation of betwenness centrality and page rank

![model0](/Users/leah/summer_2017/Go_graphs/week3_images/model0.png) 

The mean of spearman correlation between page rank and betweenness centrality is 0.9587.



#### 5. Graph centrality

From Freeman 79's paper, we further consider the graph betweenness centrality. And we repsectively eliminate individual node ranking highest in page rank and betweenness centrality, see the infect on the graph centrality from removing the node.

We firstly test the distribution of graph centrality in simple graph.   

![histogram for graph centrality](/Users/leah/summer_2017/Go_graphs/week3_images/histogram for graph centrality.png)

The variance is small enough that we could accept it as less volatile.

We check the graph centrality after removal the first 50 node of 1000 in total, and compare the betweenness centrality with page rank.

![Graph_centrality](/Users/leah/summer_2017/Go_graphs/week3_images/Graph_centrality.png)

The graph centrality highly correlated with each other and show the same trend.  