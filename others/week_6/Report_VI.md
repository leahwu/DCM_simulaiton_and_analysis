# Report VI

Luhuan Wu, Xiaohui Li

July 5, 2017

## 1. Degree correlation = 0

We set W+ and W- to be generated independently.

![independent_2](/Users/leah/summer_2017/Go_graphs/week_6/independent_2.png)



![independent_3](/Users/leah/summer_2017/Go_graphs/week_6/independent_3.png)



## 2. Effects of removing top-ranked node(s)

#### Some definitions:

#### 1. Average_shortest_path_length of a graph G

The average shortest path length is
$$
a = \sum_{s,t}\frac{d(s,t)}{n(n-1)}
$$
where `V` is the set of nodes in `G`, `d(s, t)` is the shortest path from `s` to `t`, and `n` is the number of nodes in `G`.

#### 2. Average_neighbor_degree

The average degree of a node ![i](https://networkx.github.io/documentation/development/_images/math/62494ad46772c68b86d00123a1ea8f195a7864b2.png) is

![k_{nn,i} = \frac{1}{|N(i)|} \sum_{j \in N(i)} k_j](https://networkx.github.io/documentation/development/_images/math/ef382473d588681f1efa5156fdf589c8cc3d7fb0.png)

where ![N(i)](https://networkx.github.io/documentation/development/_images/math/5486e833a7f69f104ffb21e651fcca1121198746.png) are the neighbors of node ![i](https://networkx.github.io/documentation/development/_images/math/62494ad46772c68b86d00123a1ea8f195a7864b2.png) and ![k_j](https://networkx.github.io/documentation/development/_images/math/63573bae78a0bdd80c2c5ddcc06797b6e56471fc.png) is the degree of node ![j](https://networkx.github.io/documentation/development/_images/math/976b652be33ea6b747a03babbb113160506846d0.png) which belongs to ![N(i)](https://networkx.github.io/documentation/development/_images/math/5486e833a7f69f104ffb21e651fcca1121198746.png).

There are 2 parameters of this measure:

- **source** (*string (“in”|”out”)*) – Directed graphs only. Use “in”- or “out”-degree for source node.
- **target** (*string (“in”|”out”)*) – Directed graphs only. Use “in”- or “out”-degree for target node.

### 1)Model 1

**alpha=beta=5, b=c=10, a=d=1, Expected degree = 12.3, Degree Correlation=0.4**

We **remove from the original graph **the nodes that are **top 150 pagerank-ranked subsequently**, which means we remove the rank-1 page-rank node, and then remove rank-2 page-rank node, and so on and on.

And then we **remove from the original graph** the nodes that are**top 150 betweenness-centrality-ranked subsequently** .

The plot shows the changes in graph's **average shortest path length**.

![rm_1](/Users/leah/summer_2017/Go_graphs/week_6/rm_1.png)

We remove the node of **first 150 page rank independently**.

![rm_indep_1](/Users/leah/summer_2017/Go_graphs/week_6/rm_indep_1.png)

| Node label                               | 1747                                    | 849     | 968     | 1433                                    |
| ---------------------------------------- | --------------------------------------- | ------- | ------- | --------------------------------------- |
| removing effect on ave_sp_length         | Largest                                 | Second  | Third   | Smallest                                |
| ave_sp_length after removing it          | 3.28709(100.00187% of the original one) | 3.28509 | 3.28419 | 3.28121(100.00008% of the original one) |
| page rank order                          | 1                                       | 2       | 3       | 149                                     |
| in-degree                                | 49                                      | 46      | 40      | 19                                      |
| out-degree                               | 52                                      | 36      | 29      | 7                                       |
| total degree                             | 101                                     | 82      | 69      | 26                                      |
| ave. neighbor degree (source: in, target: in) | 14.49                                   | 11.06   | 10.475  | 5.42                                    |
| ave. neighbor degree (source: in, target: out) | 14.08                                   | 10.07   | 9.875   | 4.26                                    |
| ave. neighbor degree (source: out, target: in) | 13.65                                   | 14.14   | 14.45   | 14.71                                   |
| ave. neighbor degree (source: out, target: out) | 13.27                                   | 12.86   | 13.62   | 11.57                                   |



### 2)Model 2

**alpha=7, beta=4, a=4.5, d=0.57, b=27.98, c=24.48**

**Expected degree = 32.42, Degree correlation = 0.62**

![rm_2](/Users/leah/summer_2017/Go_graphs/week_6/rm_2.png)

![rm_indep_2](/Users/leah/summer_2017/Go_graphs/week_6/rm_indep_2.png)

| Node label                               | 1115                                    | 957     | 1630    | 708                                    |
| ---------------------------------------- | --------------------------------------- | ------- | ------- | -------------------------------------- |
| removing effect on ave_sp_length         | Largest                                 | Second  | Third   | Smallest                               |
| ave_sp_length after removing it          | 2.56152(100.00099% of the original one) | 2.56129 | 2.56065 | 2.55902(100.0012% of the original one) |
| page rank order                          | 1                                       | 2       | 3       | 225                                    |
| in-degree                                | 39                                      | 30      | 25      | 40                                     |
| out-degree                               | 27                                      | 58      | 16      | 18                                     |
| total degree                             | 66                                      | 88      | 41      | 58                                     |
| ave. neighbor degree (source: in, target: in) | 26.59                                   | 66.2    | 22.0    | 14.35                                  |
| ave. neighbor degree (source: in, target: out) | 31.67                                   | 65.27   | 22.08   | 12.125                                 |
| ave. neighbor degree (source: out, target: in) | 38.41                                   | 34.24   | 34.375  | 31.89                                  |
| ave. neighbor degree (source: out, target: out) | 45.74                                   | 33.76   | 34.5    | 26.94                                  |



### 3) Model 3: W+ and W- are generated independently

**alpha=beta=3, b=c=15, Expected degree = 22.3**

![rm_3](/Users/leah/summer_2017/Go_graphs/week_6/rm_3.png)

![rm_indep_3](/Users/leah/summer_2017/Go_graphs/week_6/rm_indep_3.png)



| Node label                               | 1199                                   | 595     | 1164     | 1671    | 128                                    |
| ---------------------------------------- | -------------------------------------- | ------- | -------- | ------- | -------------------------------------- |
| removing effect on ave_sp_length         | Largest                                | Second  | Smallest | 8th     | 4th                                    |
| ave_sp_length after removing it          | 2.80538(100.0524% of the original one) | 2.80524 | 2.80389  | 2.80496 | 2.80513(99.99916% of the original one) |
| page rank order                          | 69                                     | 59      | 242      | 1       | 2                                      |
| in-degree                                | 54                                     | 53      | 24       | 136     | 131                                    |
| out-degree                               | 61                                     | 56      | 9        | 18      | 21                                     |
| total degree                             | 115                                    | 109     | 33       | 154     | 152                                    |
| ave. neighbor degree (source: in, target: in) | 31.82                                  | 33.60   | 10.67    | 4.99    | 4.76                                   |
| ave. neighbor degree (source: in, target: out) | 25.63                                  | 23.53   | 7.0      | 2.86    | 3.63                                   |
| ave. neighbor degree (source: out, target: in) | 28.16                                  | 31.80   | 28.44    | 37.72   | 29.71                                  |
| ave. neighbor degree (source: out, target: out) | 22.69                                  | 22.27   | 18.67    | 21.61   | 22.69                                  |



