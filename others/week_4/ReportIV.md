# ReportIV

Luhuan Wu, Xiaohui Li

June 15, 2017

## 1. Correlation of in degree sequence and out degree sequence

First we have some calculations:
$$
\begin{align}
ED^+D^- &=E_{W^-}[E[D^+D^-|W^-]]\\
&=E_{W^-}a(W^-)^{d+1}\\
&=\int_c^\infty ax^{d+1}p_{W^-}(x)dx\\
&=\int_c^\infty ax^{d+1}\beta c^\beta x^{-\beta - 1}dx\\
&=a\beta c^\beta \int_c^\infty x^{d-\beta}dx\\
&= \frac{a \beta c^\beta c^{d-\beta + 1}}{\beta - d -1}\\
&= \frac{a \beta c^{d+1}}{\beta -d -1}\\
\end{align}
\\
ED^+ = ED^- = EW^+ = EW^- = \frac{\alpha b}{\alpha - 1}\\
E(W^-)^2=\int_c^\infty x^2\beta c^\beta x^{-\beta - 1}dx=\frac{\beta c^2}{\beta - 2}\\
E(D^-)^2 = E_{W^-}[E[(D^-)^2|W^-]]=E_{W^-}[Var(D^-)+(ED^-)^2|W^-]=E[W^-+(W^-)^2]\\
\Rightarrow Var(D^-) = E(D^-)^2-(ED^-)^2=E[W^-+(W^-)^2]-(EW^-)^2\\
\text{Similarly we could derive } Var(D^+) =E[W^++(W^+)^2]-(EW^+)^2\\
$$
Therefore we can calculate the correlation of in degree sequence and out degree sequence
$$
\rho = corr(D^+, D^-) =\frac{Cov(D+, D^-)}{\sqrt{Var(D^+)}\sqrt{Var(D^-)})}=\frac{ED^+D^--ED^+ED^-}{\sqrt{Var(D^+)}\sqrt{Var(D^-)}}=\\
$$
The correlation between sample in degree sequence and sample out degree sequence is:
$$
\hat{\rho}= \frac{\sum_{i=1}^n(d^+_i-\bar{d^+})(d^-_i-\bar{d^-})}{\sqrt{\sum_{i=1}^n(d^+_i-\bar{d^+})^2}\sqrt{ \sum_{i=1}^n(d^-_i-\bar{d^-})^2}}
$$
**Simulation results**

Setting 

```Python
a = 1
d = 1.3
beta = 3.5
```

We get the correlation of in degree sequence and out degree sequence is:

~~~Python
corr
Out[13]: 0.21391254956397346
~~~

Let n = # sample sequence size, m = simulation times.

When m = 200, n =2000, we have the sample correlation mean and sandard deviation:

~~~Python
corrs.mean()
Out[14]: 0.19637550355389841
corrs.std()
Out[15]: 0.05094615555985188
~~~

Setting

```Python
a = 0.5
d = 1.3
beta = 3.8
```

The correlation of in degree sequence and out degree sequence is:

~~~Python
corr
Out[2]: 0.6565165146993605
~~~

When m = 500, n =1000, we have the sample correlation mean and standard deviation:

~~~Python
corrs.mean()
Out[3]: 0.64077080219167792
corrs.std()
Out[4]: 0.065025909770299734
~~~

So the sample correlation does converge to theoretical correlation numerically.

## 2. Degree correlation, page rank and betweenness centrality

In this part we investigate how the rank correlation changes as degree correlation changes.

Here we define:

1. rank correlation: spearman's rank correlation between page rank and betweenness centrality.
2. degree correlation: correlation of in-degree sequence and out-degree sequence

We change the degree correlation by varying choices of beta with fixed a, and d. More specifically, we have 3 fixed (a, d):
$$
(1) \qquad  (a, d) = (1, 1)\\
(2) \qquad (a, d) = (0.5, 1.4)\\
(3) \qquad (a, d) = (2, 0.6)\\
$$
Where 
$$
P(D^+ = d^+, D^- = d^-) = P(Poisson(W^+) = d^+, Poisson(W^-)=d^-)\\\text{where }(W^+,W^-) \text{ are jointly regularly varying.}\\P(W^+ > x) = (\frac{x}{b})^{-\alpha},\qquad x >b\\P(W^- > x) = (\frac{x}{c})^{-\beta}, \qquad x >c \\\qquad (\alpha, \beta > 1)\\W^+ = a(W^-)^d
$$
Then in each fixed (a, d) set-up, we tune the parameter beta to vary from 2.5 to 6 with step 0.2, and select the models with expected degree larger than 2.

We run simulations 20 times for each set of parameters to get the average value and the simulation results are listed below.

![models1_ave_corr](/Users/leah/summer_2017/Go_graphs/week_4/models1_ave_corr.png)

![models1_0](/Users/leah/summer_2017/Go_graphs/week_4/models1_0.png)

![models1_17](/Users/leah/summer_2017/Go_graphs/week_4/models1_17.png)

![models2_ave_corr](/Users/leah/summer_2017/Go_graphs/week_4/models2_ave_corr.png)

![models2_0](/Users/leah/summer_2017/Go_graphs/week_4/models2_0.png)

![models2_15](/Users/leah/summer_2017/Go_graphs/week_4/models2_15.png)

![models1_ave_corr](/Users/leah/summer_2017/Go_graphs/week_4/models3_ave_corr.png)

We choose one simulation result for a = 2, d = 0.6,  beta varies from 2.5 to 5.9 and plot the bc against pr.

the rank correlaiton of total 18 models are:

```Python
    [ 0.68239678,  0.67444708,  0.64796285,  0.64939729,  0.67010538,
    0.63575507,  0.65615248,  0.66411198,  0.66392807,  0.66349164,
    0.62837785,  0.69885686,  0.70056125,  0.65651333,  0.67814845,
    0.66234847,  0.65735303,  0.64345396]
```
models3[0]: rank correlation : 0.682

![models3_0](/Users/leah/summer_2017/Go_graphs/week_4/models3_0.png)

models3[10]: rank correlation: 0.628

![models3_10](/Users/leah/summer_2017/Go_graphs/week_4/models3_10.png)

models3[12]: rank correlation(highest): 0.70056

![models3_17](/Users/leah/summer_2017/Go_graphs/week_4/models3_12.png)

models3[17]: rank correlation: 0.643

![models3_17](/Users/leah/summer_2017/Go_graphs/week_4/models3_17.png)

![models1_num_con](/Users/leah/summer_2017/Go_graphs/week_4/models1_ave_num_con.png)

![models2_num_con](/Users/leah/summer_2017/Go_graphs/week_4/models2_ave_num_con.png)

![models3_num_con](/Users/leah/summer_2017/Go_graphs/week_4/models3_ave_num_con.png)

The detailed information are listed before:

(The results below are the average value over 20 simulations)

(1) a = 1, d = 1

| beta                                    | 2.5   | 2.7    | 2.9    | 3.1    | 3.3    | 3.5    | 3.7   | 3.9   | 4.1   | 4.3    | 4.5   | 4.7    | 4.9    | 5.1    | 5.3   | 5.5   | 5.7    | 5.9    |
| --------------------------------------- | ----- | ------ | ------ | ------ | ------ | ------ | ----- | ----- | ----- | ------ | ----- | ------ | ------ | ------ | ----- | ----- | ------ | ------ |
| alpha                                   | 2.5   | 2.7    | 2.9    | 3.1    | 3.3    | 3.5    | 3.7   | 3.9   | 4.1   | 4.3    | 4.5   | 4.7    | 4.9    | 5.1    | 5.3   | 5.5   | 5.7    | 5.9    |
| b                                       | 2     | 2      | 2      | 2      | 2      | 2      | 2     | 2     | 2     | 2      | 2     | 2      | 2      | 2      | 2     | 2     | 2      | 2      |
| c                                       | 2     | 2      | 2      | 2      | 2      | 2      | 2     | 2     | 2     | 2      | 2     | 2      | 2      | 2      | 2     | 2     | 2      | 2      |
| expected degree                         | 3.29  | 3.2375 | 3.0535 | 2.9345 | 2.899  | 2.8275 | 2.762 | 2.745 | 2.676 | 2.6145 | 2.554 | 2.556  | 2.527  | 2.5255 | 2.45  | 2.499 | 2.4145 | 2.446  |
| degree correlation                      | 0.727 | 0.627  | 0.539  | 0.464  | 0.401  | 0.348  | 0.303 | 0.266 | 0.235 | 0.209  | 0.186 | 0.167  | 0.150  | 0.136  | 0.124 | 0.113 | 0.103  | 0.095  |
| rank correlation                        | 0.705 | 0.660  | 0.709  | 0.707  | 0.650  | 0.682  | 0.655 | 0.657 | 0.682 | 0.635  | 0.629 | 0.625  | 0.633  | 0.655  | 0.620 | 0.616 | 0.620  | 0.582  |
| number of strongly connected components | 298.1 | 308.25 | 321.75 | 332.4  | 356.85 | 367.7  | 383.7 | 395.7 | 398.7 | 415    | 414.1 | 426.05 | 425.95 | 437.05 | 450.7 | 459.4 | 464.2  | 465.35 |

(2) a = 0.5, d = 1.4

| beta                                    | 2.9    | 3.1   | 3.3    | 3.5   | 3.7    | 3.9   | 4.1   | 4.3    | 4.5   | 4.7    | 4.9    | 5.1    | 5.3    | 5.5    | 5.7   | 5.9   |
| --------------------------------------- | ------ | ----- | ------ | ----- | ------ | ----- | ----- | ------ | ----- | ------ | ------ | ------ | ------ | ------ | ----- | ----- |
| alpha                                   | 2.071  | 2.214 | 2.357  | 2.500 | 2.643  | 2.786 | 2.929 | 3.071  | 3.214 | 3.357  | 3.500  | 3.642  | 3.786  | 3.929  | 4.071 | 4.214 |
| b                                       | 2.473  | 2.700 | 2.898  | 3.073 | 3.227  | 3.365 | 3.488 | 3.599  | 3.700 | 3.790  | 3.873  | 3.949  | 4.019  | 4.084  | 4.144 | 4.199 |
| c                                       | 3.133  | 3.335 | 3.509  | 3.659 | 3.789  | 3.903 | 4.005 | 4.095  | 4.176 | 4.250  | 4.316  | 4.376  | 4.432  | 4.823  | 4.529 | 4.572 |
| 'expected degree                        | 5.1895 | 5.015 | 5.0565 | 5.121 | 5.2745 | 5.096 | 5.266 | 5.3125 | 5.497 | 5.4925 | 5.4545 | 5.5085 | 5.4815 | 5.5945 | 5.488 | 5.556 |
| degree correlation                      | 0.475  | 0.602 | 0.609  | 0.587 | 0.555  | 0.521 | 0.488 | 0.455  | 0.425 | 0.396  | 0.369  | 0.345  | 0.323  | 0.302  | 0.283 | 0.266 |
| rank correlation                        | 0.769  | 0.763 | 0.764  | 0.757 | 0.741  | 0.729 | 0.748 | 0.752  | 0.716 | 0.756  | 0.745  | 0.724  | 0.700  | 0.705  | 0.731 | 0.736 |
| number of strongly connected components | 109.05 | 85.3  | 76.25  | 59.95 | 54.5   | 47.4  | 44.7  | 44.9   | 37.75 | 33.85  | 33.75  | 32.05  | 30.75  | 29.4   | 27.5  | 25.65 |

(3)a = 2, d = 0.6

| beta                                    | 2.5    | 2.7    | 2.9    | 3.1    | 3.3    | 3.5    | 3.7   | 3.9   | 4.1   | 4.3   | 4.5   | 4.7    | 4.9    | 5.1   | 5.3   | 5.5    | 5.7   | 5.9   |
| --------------------------------------- | ------ | ------ | ------ | ------ | ------ | ------ | ----- | ----- | ----- | ----- | ----- | ------ | ------ | ----- | ----- | ------ | ----- | ----- |
| alpha                                   | 4.166  | 4.500  | 4.833  | 5.167  | 5.500  | 5.833  | 6.167 | 6.500 | 6.833 | 7.167 | 7.500 | 7.833  | 8.167  | 8.500 | 8.833 | 9.167  | 9.500 | 9.833 |
| b                                       | 3.968  | 4.120  | 4.247  | 4.355  | 4.448  | 4.529  | 4.598 | 4.660 | 4.715 | 4.764 | 4.809 | 4.850  | 4.886  | 4.920 | 4.950 | 4.979  | 5.004 | 5.029 |
| c                                       | 3.132  | 3.335  | 3.509  | 3.658  | 3.789  | 3.903  | 4.005 | 4.095 | 4.176 | 4.250 | 4.316 | 4.376  | 4.432  | 4.482 | 4.529 | 4.572  | 4.612 | 4.649 |
| expected degree                         | 5.2445 | 5.2015 | 5.3825 | 5.4485 | 5.5405 | 5.4345 | 5.503 | 5.54  | 5.529 | 5.496 | 5.562 | 5.6115 | 5.5505 | 5.524 | 5.619 | 5.6595 | 5.623 | 5.627 |
| degree correlation                      | 0.487  | 0.452  | 0.414  | 0.376  | 0.341  | 0.309  | 0.281 | 0.256 | 0.234 | 0.214 | 0.196 | 0.180  | 0.166  | 0.154 | 0.142 | 0.132  | 0.123 | 0.115 |
| rank correlation                        | 0.682  | 0.674  | 0.648  | 0.649  | 0.670  | 0.636  | 0.656 | 0.664 | 0.664 | 0.663 | 0.628 | 0.699  | 0.701  | 0.657 | 0.678 | 0.662  | 0.657 | 0.643 |
| number of strongly connected components | 53.65  | 45.25  | 38.4   | 34.25  | 33.5   | 31.9   | 28.85 | 25.3  | 25.7  | 23    | 23.5  | 20.75  | 22     | 20.45 | 21.6  | 19.6   | 20    | 19.3  |

## 3. Poisson tail

![models1_tail_dist](/Users/leah/summer_2017/Go_graphs/week_4/models1_tail_dist.png)

![models2_tail_dist](/Users/leah/summer_2017/Go_graphs/week_4/models2_tail_dist.png)

![models3_tail_dist](/Users/leah/summer_2017/Go_graphs/week_4/models3_tail_dist.png)



We take lambda = 3.29, and generate 1000 poission random variables, plot its tail distribution against the tail distribution of in degree sequence which has expected degree 3.29.

![poisson tail](/Users/leah/summer_2017/Go_graphs/week_4/poisson tail.png)

![poisson_tail2](/Users/leah/summer_2017/Go_graphs/week_4/poisson_tail2.png)

## 4. Rank correlation and expected degree

Expected degree : 2.076

![m7](/Users/leah/summer_2017/Go_graphs/week3_images/m7.png)

Expected degree: 42.1775.

![m156](/Users/leah/summer_2017/Go_graphs/week3_images/m156.png)

## 5. Graph centrality

![WechatIMG331497990136_.pic](/Users/leah/summer_2017/Go_graphs/week_4/WechatIMG331497990136_.pic.jpg)

![WechatIMG341497990138_.pic](/Users/leah/summer_2017/Go_graphs/week_4/WechatIMG341497990138_.pic.jpg)

![WechatIMG351497990139_.pic](/Users/leah/summer_2017/Go_graphs/week_4/WechatIMG351497990139_.pic.jpg)

![WechatIMG391497991581_.pic_hd](/Users/leah/summer_2017/Go_graphs/week_4/WechatIMG391497991581_.pic_hd.jpg)

![Screen Shot 2017-06-20 at 2.50.57 PM](/Users/leah/summer_2017/Go_graphs/week_4/Screen Shot 2017-06-20 at 2.50.57 PM.png)

## 6. Random-walk betweenness centrality

![WechatIMG321497948164_.pic](/Users/leah/summer_2017/Go_graphs/week_4/WechatIMG321497948164_.pic.jpg)

![WechatIMG361497990147_.pic](/Users/leah/summer_2017/Go_graphs/week_4/WechatIMG361497990147_.pic.jpg)

![WechatIMG371497990148_.pic](/Users/leah/summer_2017/Go_graphs/week_4/WechatIMG371497990148_.pic.jpg)

![WechatIMG381497990152_.pic](/Users/leah/summer_2017/Go_graphs/week_4/WechatIMG381497990152_.pic.jpg)