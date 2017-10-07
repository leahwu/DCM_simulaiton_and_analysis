# Report IV

Luhuan Wu, Xiaohui Li

6.27, 2017

## 1. Relations between degree correlation and rank correlation

![corr_1](/Users/leah/summer_2017/Go_graphs/week_5/corr_1.png)

Alpha = beta = 5, a = d = 1

| b                  | 1     | 6     | 11    | 16    | 21    | 26    | 31    | 36    | 41    | 46    | 51    |
| ------------------ | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| expected degree    | 1.25  | 7.5   | 13.75 | 20.0  | 26.25 | 32.5  | 38.75 | 45.0  | 51.25 | 57.5  | 63.75 |
| degree correlation | 0.08  | 0.33  | 0.48  | 0.57  | 0.64  | 0.68  | 0.72  | 0.75  | 0.77  | 0.79  | 0.81  |
| rank correlation   | 0.599 | 0.721 | 0.771 | 0.797 | 0.818 | 0.835 | 0.846 | 0.853 | 0.863 | 0.869 | 0.874 |

![corr_2](/Users/leah/summer_2017/Go_graphs/week_5/corr_2.png)

alpha = 4, beta = 3, d = 0.75

| a                  | 1.3  | 1.6  | 1.9   | 2.2   | 2.5   | 2.8   | 3.1   |
| ------------------ | ---- | ---- | ----- | ----- | ----- | ----- | ----- |
| b                  | 2.01 | 4.60 | 9.15  | 16.45 | 27.43 | 43.17 | 64.86 |
| c                  | 1.78 | 4.09 | 8.14  | 14.62 | 24.39 | 38.37 | 57.65 |
| expected degree    | 2.67 | 6.14 | 12.20 | 21.94 | 36.58 | 57.56 | 86.48 |
| degree correlation | 0.34 | 0.53 | 0.68  | 0.79  | 0.85  | 0.90  | 0.92  |
| rank correlation   | 0.63 | 0.71 | 0.76  | 0.83  | 0.86  | 0.89  | 0.91  |

## 2. Power law index of page rank and betweenness centrality 



![power_law_1](/Users/leah/summer_2017/Go_graphs/week_5/power_law_5.png)

![power_law_1](/Users/leah/summer_2017/Go_graphs/week_5/power_law_1.png)

![power_law_4](/Users/leah/summer_2017/Go_graphs/week_5/power_law_4.png)

![power_law_3](/Users/leah/summer_2017/Go_graphs/week_5/power_law_3.png)

![tail_dist_comp_3](/Users/leah/summer_2017/Go_graphs/week_5/tail_dist_comp_3.png)

![power_law_2](/Users/leah/summer_2017/Go_graphs/week_5/power_law_2.png)

| alpha                                  | 3     | 5     | 7     | 7     | 7     | 7     | 4     |
| -------------------------------------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| beta                                   | 3     | 5     | 7     | 4     | 4     | 4     | 3     |
| a                                      | 1     | 1     | 1     | 3.5   | 4.5   | 5.5   | 3.1   |
| b                                      | 51    | 51    | 51    | 15.57 | 27.98 | 44.69 | 64.86 |
| c                                      | 51    | 51    | 51    | 13.62 | 24.48 | 39.10 | 57.65 |
| d                                      | 1     | 1     | 1     | 0.57  | 0.57  | 0.57  | 1.4   |
| expected degree                        | 76.5  | 63.75 | 59.5  | 18.16 | 32.64 | 55.61 | 86.48 |
| degree correlation                     | 0.96  | 0.81  | 0.63  | 0.48  | 0.61  | 0.70  | 0.92  |
| rank correlation                       | 0.88  | 0.88  | 0.82  | 0.71  | 0.78  | 0.81  | 0.91  |
| page rank power law index              | -3.03 | -5.04 | -7.00 |       | -7.76 |       | -4.49 |
| betweenness centrality power law index | -1.55 | -2.51 | -3.65 |       | -2.64 |       | -1.76 |



## 3. Degree correlation

When alpha = beta (that is d = 1 and a = 1),

as beta increases, pho (correlation) decreases;

as  b increases, pho increases
$$
\rho = corr(D^+, D^-) = \frac{Cov(D+, D^-)}{\sqrt{Var(D^+)}\sqrt{Var(D^-)})}=\frac{ED^+D^--ED^+ED^-}{\sqrt{Var(D^+)}\sqrt{Var(D^-)}}\\
=\frac{\frac{a \beta c^{d+1}}{\beta -d -1}-(\frac{b\alpha}{\alpha - 1})^2}{\sqrt{Var(D^+)}\sqrt{Var(D^-)}}
$$
where
$$
Var(D^-) = E(D^-)^2-(ED^-)^2=E[W^-+(W^-)^2]-(EW^-)^2 \\
E(W^-)^2=\int_c^\infty x^2\beta c^\beta x^{-\beta - 1}dx=\frac{\beta c^2}{\beta - 2}\\
EW^- = \frac{\alpha b}{\alpha - 1}
$$
