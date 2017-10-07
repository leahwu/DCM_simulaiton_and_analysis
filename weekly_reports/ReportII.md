# Report II

Luhuan Wu, Xiaohui Li

June 6, 2017.   



## 1. Introduction

In this week, there are four things we did:

1. We revise the way we generate the in-degree and bi-degree sequences by generating the unifrom distribution in [0, 1].
2. We calculate the conditions for the parameters alpha, beta for the algorithm to converge.
3. We come up with two ways to evalute the correlation between page rank and betweenness centrality.  
   - plots of pagerank and betweennes centrality to get direct observation
   - Statistical measurement: rank correlation.
4. We set step-wise parameters to observe in which interval, page rank would overlap, or have positive correlation with, betweenness centrality, and in which interval it does not.



## 2. Procedures

### 1. Generating bi-sequences

$$
P(D^+ = d^+, D^- = d^-) = P(Poisson(W^+) = d^+, Poisson(W^-)=d^-)\\\text{where }(W^+,W^-) \text{ are jointly regularly varying.}\\P(W^+ > x) = (\frac{x}{b})^{-\alpha},\qquad x >b\\P(W^- > x) = (\frac{x}{c})^{-\beta}, \qquad x >c \\\qquad (\alpha, \beta > 1)\\W^+ = a(W^-)^d\\
z=F(x) =1-P(W^->x)=1-(\frac{x}{c})^{-\beta}\\
\Rightarrow x=F^{-1}(z)=c(1-z)^{-\frac{1}{\beta}}
$$

So setting
$$
U \sim \text{Uniform}(0, 1), W^{-1}=F^{-1}(U)=c(1-U)^{-\frac{1}{\beta}}
$$
We get the desired random variable.

### 2. Convergence conditions

In _ReportI_, we have conducted the relationships between the parameters by using the distribution and equal expectation of
$$
(W^+, W^-)
$$
as given below:
$$
d =  \frac{\beta}{\alpha}\\
\text{If } \alpha \neq \beta,  \qquad \qquad b = (\frac{\alpha (\beta - 1)}{(\alpha-1)\beta})^{\frac{\beta}{\alpha - \beta} }a^{\frac{\alpha}{\alpha - \beta}}\\
\qquad \qquad \qquad  c =  (\frac{\alpha (\beta - 1)}{(\alpha-1)\beta})^{\frac{\alpha}{\alpha - \beta} }a^{\frac{\alpha}{\alpha - \beta}} \\
\text{If } \alpha = \beta, \text{ then }a = 1 \text{ and we could arbitralily choose } b=c.	\qquad \qquad \qquad (3)
$$
In Algorithm 2.2, if we want 
$$
\frac{\Delta_n}{n} \rightarrow 0 \qquad \qquad \text{as }n \rightarrow \infty
$$
we must have 
$$
E[(W^+ - W-)^{1 + \epsilon}] = 0   \qquad \text{ for any given fixed } \epsilon >0
$$
We choose one sufficient condition:
$$
\epsilon =1 \text{ that is }Var(W^+ - W^-) = E[a(W^-)^d -W^-]^2  < \infty \\
\Rightarrow \beta >2, \beta >2d, \beta >d+1
$$

### 3. Evaluation of the correlation between page rank and betweeness centrality

#### 3.0 networkx implementation for page rank and betweenness centrality

[page rank_document](https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.algorithms.link_analysis.pagerank_alg.pagerank.html)

[betweenness centrality_document](https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.algorithms.centrality.betweenness_centrality.html?highlight=betweenness%20centrality#networkx.algorithms.centrality.betweenness_centrality):

> Betweenness centrality of a node ![v](https://networkx.github.io/documentation/networkx-1.10/_images/math/53c4a26799ff6cdae6f13d6b1fcf961660d83169.png) is the sum of the fraction of all-pairs shortest paths that pass through ![v](https://networkx.github.io/documentation/networkx-1.10/_images/math/53c4a26799ff6cdae6f13d6b1fcf961660d83169.png):
> $$
> c_B(v) = \sum_{s,t \in V} \frac{\sigma(s,t|v)}{\sigma(s,t)}
> $$
> where ![V](https://networkx.github.io/documentation/networkx-1.10/_images/math/ea879891318d7d3a04f0d3a7b0ad892a9b63c8e8.png) is the set of nodes, ![\sigma(s, t)](https://networkx.github.io/documentation/networkx-1.10/_images/math/f724eb676c09147ce1219ad0322502ba9136ce5a.png) is the number of shortest ![(s, t)](https://networkx.github.io/documentation/networkx-1.10/_images/math/a89084d7e1d70e18f88801fc46310063a5410644.png)-paths, and ![\sigma(s, t|v)](https://networkx.github.io/documentation/networkx-1.10/_images/math/f8be1c463f76d2bf1d7c06ea64d9ae7877f657ce.png) is the number of those paths passing through some node ![v](https://networkx.github.io/documentation/networkx-1.10/_images/math/53c4a26799ff6cdae6f13d6b1fcf961660d83169.png) other than ![s, t](https://networkx.github.io/documentation/networkx-1.10/_images/math/11ea1225465563f6ec492f643e46328d31d8c3f0.png). If ![s = t](https://networkx.github.io/documentation/networkx-1.10/_images/math/8ca592c5a04ef883ff9b192f44aa5edda9da03de.png), ![\sigma(s, t) = 1](https://networkx.github.io/documentation/networkx-1.10/_images/math/cc560c61381cf8c03e64b279f8bde36e3df96352.png), and if ![v \in {s, t}](https://networkx.github.io/documentation/networkx-1.10/_images/math/256407d40e389f52991c0d7b415e3487ee9dc6cd.png), ![\sigma(s, t|v) = 0](https://networkx.github.io/documentation/networkx-1.10/_images/math/c7d3eb38e416b28a38660834405a9c99d97ad661.png)

#### 3.1 Plots

We define two ways to plot the nodes to help us observe the correlation.

1. We plot the page rank of nodes in decreasing order, and then plot those nodes' betweenness centrality in order.
2. We plot the betweenness centrality of nodes in decreasing order, and then plot those nodes' page rank in order.

#### 3.2 Statistical measures 

##### 3.2.1 Rank correlation — Spearsman's test

>In [statistics](https://en.wikipedia.org/wiki/Statistics), a **rank correlation** is any of several statistics that measure an **ordinal association**—the relationship between [rankings](https://en.wikipedia.org/wiki/Ranking) of different [ordinal](https://en.wikipedia.org/wiki/Ordinal_data) variables or different rankings of the same variable, where a "ranking" is the assignment of the labels "first", "second", "third", etc. to different observations of a particular variable. A **rank correlation coefficient** measures the degree of similarity between two rankings, and can be used to assess the [significance](https://en.wikipedia.org/wiki/Statistical_significance) of the relation between them.
>
> —- <cite>[Wikipedia_Rank correlation][1]</cite>

We use [Spearsman's test][2] to measure the rank correlation between page rank and betweenness centrality. It basically measures  to the distance between the nodes' page-rank ranking and betweenness-centrality ranking.

Spearsman's test of two ranked data sequence evaluated by different ranking algorithms return two values: _correlation_ and _p-value_, while the corresponding null hypothesis is that two ranked data are statistically independent, which means two ranking algorithm has no correlation. 

The smaller the p-value, it's more likely to reject null hypothesis. 

A correlation of +1 or −1 occurs when each of the variables is a perfect monotone function of the other.

So we feed the page rank of nodes and betweenness centrality of nodes to Spearsman's test and observe the correlation and p-value to judge the correlation between two page rank and betweenness centrality.

##### 3.2.2 Measuring overlapping nodes

Given the graph size n, we calculate the overlapping number of nodes, m, of first k page-rank-ranked nodes and first betweenness-centrality-ranked nodes, and thereby get the _**percentage of overlapping nodes**_ p = m/k. That is
$$
p = \frac{\text{# nodes in both top k page-rank-ranked and top k b-c-ranked nodes}}{k}
$$

### 3. Set up parameters intervals to generate the models

According to the relationship of the parameters, we actually only need to set up 3 parameters to get the total 6. So we set the parameters intervals as follows:

```python
a_range = np.arange(0.6, 1.6, 0.2) # 5 choices: 0.6, 0.8, 1.0, 1.2, 1.4
beta_range = np.arange(2.5, 3.5, 0.2)  # 4 choices: 2.5, 2.7, 2.9, 3.1
d_range = np.arange(0.8, 1.3, 0.2)  # 3 choices: 0.8, 1.0, 1.2
```



## 3. Results and Analysis

### 3.1 Statistical test  

#### 1) K-S test

the **Kolmogorov–Smirnov test** (**K–S test** or **KS test**) is a nonparametric test of the equality of one-dimensional probability distributions that can be used  to compare two samples (two-sample K–S test).

#### 2) Wilcoxon signed-rank test

The **Wilcoxon signed-rank test** is a non-parametric hypothesis test used when comparing two related samples, matched samples, or repeated measurements on a single sample to assess whether their population mean ranks differ. 

### 3.1 Comparison of degree sequence

 We use the above statistical test to check whether the generated simple graph have asumptotically the same distribution as previous bi-degree sequence distribution.

#### a. In-degree



#### b. Out-degree



We could find that both tests' p-value in both in-degree and out-degree are not small enough to reject the null hypothesis, this gives sense to receive the alternative that the two samples (graph bi-degree sequence and original bi-degree sequence) are generated from the same distribution.



### 3.2 Correlation between page rank and betweenness centrality.

We test for different parameters as describeds in _2.3_, and we get 75 models. We list the information of:

1. _parameters_
2. _average of W^+, W^-_
3. _average degree_ of in-degree sequences and out-degree sequences
4. The _percentage of overlapping nodes_ in top k ranked nodes by betweenness centrality and page rank
5. Spearsman's rank correlation test's _correlation_ and _p-value_.

The detailed result is listed in [result.txt][result]

#### 3.2.1 Relationships between average degree and percentage of overlapping nodes

We sorted the average degree of nodes of the 75 models in decreasing order, and then plot the average degree of nodes and repsective percentage of overlapping nodes in this order.

![relationship](https://raw.githubusercontent.com/leahwu/Go_graphs/master/week2_images/relationship_between.png)



As we can see from the picture, as the average degree of nodes increase, the percentage of overlapping nodes in top 100 / 200 nodes increases.

This suggests that when the average degree of nodes increases, two rankings by page rand and betweeness centrality tend to overlap more.

#### 3.2.2 Further investigation into models of varying average degree of nodes

To make further investigation, we choose 4 modes which are labeled as m13, m16, m14, m9. The parameters and average degree of nodes of them are

|      | a    | b     | c     | alpha | beta | d    | average degree of nodes |
| ---- | ---- | ----- | ----- | ----- | ---- | ---- | ----------------------- |
| m13  | 0.6  | 0.056 | 0.051 | 4.125 | 3.3  | 0.8  | 0.071                   |
| m16  | 0.8  | 0.198 | 0.175 | 3.125 | 2.5  | 0.8  | 0.3025                  |
| m14  | 1    | 2     | 2     | 3.3   | 3.3  | 1    | 2.946                   |
| m9   | 0.6  | 6.598 | 7.734 | 2.4   | 2.9  | 1.2  | 11.3135                 |

We plot the relationship between overlapping percentage of top-k nodes and average degree of nodes as below:

![4_models](https://raw.githubusercontent.com/leahwu/Go_graphs/master/week2_images/overlapping_per.png)

From the plot we could see a clear positive correlation when k = 50, 100, 150, 200.

This concides with the fact we derived above:

When the average degree of nodes increases, two rankings by page rand and betweeness centrality tend to overlap more.

Now we want to find out why when the average degree is rather low, say in m13, 0.071, the percentage of overlapping is low, and why it turns out the other way around when the average degree is high. We make the plots of relationship between page rank and betweenness centrality.

**m13, average degree of nodes = 0.071 **

![m13](https://raw.githubusercontent.com/leahwu/Go_graphs/master/week2_images/m13.png)

We can see that when all page_rank is near 0, while most but 2 betweenness centrality is 0. So actually, their rankings should overlap in most cases. The problem why it differs from our precious result lies in python's sort treats the order of objects of same values. That is to say

{node1: 0, node2: 0, node3: 0} is a different ranking from {node2: 0, node1:0 ,node3: 0}.

**m16, average degree of noes = 0.3025**

![m16](https://raw.githubusercontent.com/leahwu/Go_graphs/master/week2_images/m16.png)

**m14, average degree of nodes = 2.946**

![m14](https://raw.githubusercontent.com/leahwu/Go_graphs/master/week2_images/m14.png)

**m9, average degree of nodes = 11.3125**

![m9_1](https://raw.githubusercontent.com/leahwu/Go_graphs/master/week2_images/m9.png)

![m9_2](https://raw.githubusercontent.com/leahwu/Go_graphs/master/week2_images/m9_2.png)

![m9_3](https://raw.githubusercontent.com/leahwu/Go_graphs/master/week2_images/m9_3.png)

![m9_4](https://raw.githubusercontent.com/leahwu/Go_graphs/master/week2_images/m9_4.png)



In the plots above we could see a strong positive correlation between page rank and betweenness centrality when the average degree of nodes are high(>10). But when average degree of nodes decrease, the correlation decreases, but is still positive. When the average degree of nodes is very close to 0 (0.071), most of the nodes's page rank and betweenness centrality is close to 0, which overlaps again.

## 4. Conclusion

#### a. Appropriate algorithm

Given WLLN's requirement for finite second moment constraint the parameters, we could generate the sample bi-degree sequence following the distribution at a fast enough speed. The simple directed configuration model generated from erased algorithm has the asympotically same degree distribution as the original bi-degree sequence degree distribution.



#### b. Betweeness centrality and page rank

Betweeness centrality and page rank ranking is statistically dependent.

- When the average degree of the nodes is away from zero, and when it gets higher, the overlapping percentage tends to be higher.

  But when the average degree of nodes is very close to 0, most of the nodes's page rank and betweenness centrality is close to 0, which overlaps again.

  ​



[1]: https://en.wikipedia.org/wiki/Rank_correlation
[2]: https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient
[result]: https://github.com/leahwu/Go_graphs/blob/master/results2.txt

####  


​			
​		
​	





