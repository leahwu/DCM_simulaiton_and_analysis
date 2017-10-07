Test: 
$$
P(D^+ = 0) = E[e^{-W^+}]\\
P(D^- = 0) = E[e^{-W^-}]
$$

$$
E[e^{-W^+}] = \int_b^\infty e^{-x}(-\alpha b^\alpha x^{\alpha -1})dx\\
E[e^{-W^-}] = \int_b^\infty e^{-x}(-\beta c^\beta x^{\beta -1})dx\\
$$

#### Case1: take a=d=1, alpha=beta=3, b=c=3.

Expected degree = 4.5

| n (size)              | 2,000  | 10,000 | 100,000 | 1,000,000 |
| --------------------- | ------ | ------ | ------- | --------- |
| P(D+=0)               | 0.025  | 0.0248 | 0.02284 | 0.02303   |
| Sample Mean: e^{-W^+} | 0.02   | 0.0229 | 0.02300 | 0.02299   |
| P(D-=0)               | 0.0232 | 0.0207 | 0.02286 | 0.02281   |
| Sample Mean: e^{-W^-} | 0.0232 | 0.0229 | 0.02300 | 0.02299   |

And we get integral of E[e-W+]:

-4*exp(-3) - 27*Ei(3*exp_polar(I*pi))/2 + 27*Ei(+inf*exp_polar(I*pi))/2

**Graph:  disconnected**

Number of strongly connected components: 99



#### Case2: take a=d=1, alpha=beta=3, b=c=10.

Expected degree = 15.0

| n (size)              | 2,000          | 10,000     | 100,000   |
| --------------------- | -------------- | ---------- | --------- |
| P(D+=0)               | 0.0005         | 0.0        | 1e-05     |
| Sample Mean: e^{-W^+} | 0.01427291e-05 | 1.0027e-05 | 9.907e-06 |
| P(D-=0)               | 0.0            | 0.0        | 0.0       |
| Sample Mean: e^{-W^-} | 1.01427291e-05 | 1.0027e-05 | 9.907e-06 |

And we get integral of E[e-W+]:

-46*exp(-10) - 500*Ei(10*exp_polar(I*pi)) + 500*Ei(+inf*exp_polar(I*pi))

**Graph:  Strongly connected**



#### Case3: take a=0.8, alpha=3, beta=4, d=1.333 b=1.22 c=1.37

Expected degree = 1.829

| n (size)              | 2,000  | 10,000 | 100,000  |
| --------------------- | ------ | ------ | -------- |
| P(D+=0)               | 0.164  | 0.1834 | 0.17916  |
| Sample Mean: e^{-W^+} | 0.180  | 0.179  | 0.179687 |
| P(D-=0)               | 0.2005 | 0.1901 | 0.19586  |
| Sample Mean: e^{-W^-} | 1.197  | 0.195  | 0.195655 |

**Graph: disconnected**

Number of strongly connected components: 900

#### Case4: take a=0.8, alpha=3, beta=6, d=1.333 b=1.22 c=1.37

Expected degree = 1.200

| n (size)              | 2,000  | 10,000 | 100,000 |
| --------------------- | ------ | ------ | ------- |
| P(D+=0)               | 0.2945 | 0.3025 | 0.296   |
| Sample Mean: e^{-W^+} | 0.306  | 0.3094 | 0.3104  |
| P(D-=0)               | 0.317  | 0.341  | 0.3475  |
| Sample Mean: e^{-W^-} | 0.329  | 0.3360 | 0.3373  |

**Graph: disconnected**

**Number of strongly connected components: 1671**

