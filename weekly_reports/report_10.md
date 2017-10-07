## Changes as beta increases



![beta3](https://raw.githubusercontent.com/leahwu/Go_graphs/master/week_10/beta3.png)

![beta4](https://raw.githubusercontent.com/leahwu/Go_graphs/master/week_10/beta4.png)

![beta5](https://raw.githubusercontent.com/leahwu/Go_graphs/master/week_10/beta5.png)

![beta6](https://raw.githubusercontent.com/leahwu/Go_graphs/master/week_10/beta6.png)

![beta7](https://raw.githubusercontent.com/leahwu/Go_graphs/master/week_10/beta7.png)



### WIKI VOTE

Pearson's correlation: corr, p-value

(in-degree, out-degree)	(0.31763976337716515, 1.5853361463995747e-166)

(total-degree, in-degree)	(0.74782960155018874, 0.0)

(total-degree, out-degree)	(0.86704920856659373, 0.0)

(Page rank, in-degree)		(0.92304846171013577, 0.0)

(page rank, out-degree)	(0.25414821590213482, 2.7315071472270952e-105)

(page rank, total-degree)	(0.66294301163752367, 0.0)

(Page rank, betweeness centrality)		(0.52889191488043785, 0.0)

(betweeness centrality, in-degree)		(0.55171357611680383, 0.0)

(betweeness centrality, out-degree)		(0.57633476842922016, 0.0)

(betweeness centrality, total-degree)	(0.69341012182116557, 0.0)



![5](/Users/leah/summer_2017/Go_graphs/week_10/wiki_vote.png)

![wiki_vote_tail_dist](/Users/leah/summer_2017/Go_graphs/week_10/wiki_vote_tail_dist.png)





## Degree correlation

$$
\begin{align}
p_{w^-}(x)=PDF(W^-) &= \beta c^\beta x^{-\beta - 1}\\
\Rightarrow
E[(W^-)^s]&=\int_c ^\infty \beta c^\beta x^{-\beta - 1}x^sdx
\\ &=\frac{\beta c^s}{\beta -s}\\
E[(W^-)^{2s}]&=\frac{\beta c^{2s}}{\beta -2s}\\
E[(W^-)^2]&=\frac{\beta c^2}{\beta -2}\\
E[W^-]&=\frac{\beta c}{\beta -1}
\end{align}
$$

Since
$$
s=\frac{\beta}{\alpha}
$$
by setting
$$
\alpha, \beta > 2
$$
the denominator is not zero.
$$
\begin{align}
Var(D^+)=E[D^+]-(E[D^+])^2=E[W^+ +(W^+)^2] - (E[W^+])^2\\
E[W^+]=aE[(W^-)^s]\\
E[(W^+)^2]=a^2(d^2+(1-d)^2)E([W^-)^{2s}]+2a^2d(1-d)(E[(W^-)^s])^2
\end{align}
$$
Similarly,
$$
Var(D^-)=E[D^-]-(E[D^-])^2=E[W^- +(W^-)^2] - (E[W^-])^2
$$
Then we calculate the covariance of D+ and D-:
$$
\begin{align}
Cov(D^+,D^-)&=E[D^+D^-]-ED^+ED^-\\
E[D^+D^-]&=E_{\hat{W}^-}[E_{W^-}[E[D^+D^-]|W^-]|\hat{W}^-]\\
&=E_{\hat{W}^-}[E_{W^-}[W^+W^-|W^-]|\hat{W}^-]\\
&=E_{\hat{W}^-}[E_{W^-}[(ad(W^-)^s+a(1-d)(\hat{W}^-)^s)(W^-)^s|W^-]|\hat{W}^-]\\
&=adE(W^-)^{s+1}+a(1-d)E(\hat{W}^-)^sEW^-\\
\end{align}
$$


Finally,
$$
\rho =corr(D^+, D^-)=\frac{Cov(D^+, D^-)}{\sqrt{Var(D^+)Var(D^-)}}
$$


## Relationships between parameters

$$
s = \frac{\beta}{\alpha}\\
a\frac{\beta c^s}{\beta -s}=\frac{\beta c}{\beta -1}\\
\text{If } s = 1 \text{, then } a = 1\\
\text{Else, }a=(\frac{\beta - s}{a(\beta-1)})^{\frac{1}{s-1}}
$$

### Other graphs

![1](https://raw.githubusercontent.com/leahwu/Go_graphs/master/week_10/1.png)

![2](https://raw.githubusercontent.com/leahwu/Go_graphs/master/week_10/2.png)



