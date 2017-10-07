### Case I

alpha = beta = 2.1, E=3, d=0,0.25,0.5,0.75,1.0

GiantComponent:  3720
GiantComponent:  3802
GiantComponent:  3928
GiantComponent:  3903
GiantComponent:  3883

sample corr:

0.0097,	0.2368,	0.3835,	0.627,	0.9806

computed degree corr(theoretical):

0.0,		0.2899,	0.6402,	0.8687,	0.9345

对应的图是1，2，3，4，5

以及corr1 （degree corr随d的变化）

观察： 基本上total degree的影响大于betweeness centrality（差不多这两个）， 大于out degree大于in degree 大于page rank

但是特例：d=0的时候outdegree 的影响小于in degree

当d增大的时候， 五条线越来越接近，意味着这五个指标相关性越来越强

### Case 2

alpha=2.1, beta=2.3, E=3, d=0,0.25,0.5,0.75,1.0

GiantComponent:  3869
GiantComponent:  3886
GiantComponent:  3928
GiantComponent:  3943
GiantComponent:  3953

sample corr:

0.0228,	0.1512,	0.5584,	0.6563,	0.7122

computed degree corr(theoretical):

0.0,		0.2326,	0.5286,	0.7181,	0.7717

对应的图是1，2，3，4，5

以及corr1 （degree corr随d的变化）

观察结果如上



## Check Powerlaw

一共有四幅图片明明开头是check powerlaw

check power law_1.png 是case1 alpha=beta d=0 我肉眼fit了一下 page rank 和in degree 的斜率在2.1左右，图中fit的直线的斜率就是2.1。

注：我记得老师说当alpha 不等于beta的时候， 还是当degree corr 不等于1的时候，pagerank的斜率应该要和powerlaw 的index差1？ 总而言之就验证in degree的斜率好了，不要提page rank了。



Check_powerlaw_2.png 是case1 alpha=beta d从0变到1 因为powerlaw index一样，所以预期plot的斜率重合，画图验证这一点了。

check_powerlaw_3.png 是case2 alpha！=beta 但是由于alpha=2。1， beta=2.3 十分接近，我去fit 了graph的in degree， fit的直线斜率是在2.1+， 我觉得是在误差允许范围内。我没有fit page rank。。 