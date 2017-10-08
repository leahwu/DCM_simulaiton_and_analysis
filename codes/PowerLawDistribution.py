from math import exp

import numpy as np
import scipy.stats as st
from scipy.stats import poisson
from sympy import exp as sp_exp
from sympy import integrate
from sympy.abc import x


def generate_w(c, beta):
    # generate r.v. w ~ (x/c)^{-\beta} as tail distribution
    u = np.random.uniform(0, 1)
    w = c * (1 - u)**(-1.0/beta)
    return w



class PowerLaw:
    """
    a distribution class to specifically generate the bi-degree sequence 
    from double power law distribution with intrinsic dependence.
    
    If W+ and W- are dependent, we need beta > 2, beta > 2 * d, beta > d + 1 for finite variance, and beta > 1 for zero mean.
    Else, alpha, beta > 2 would satisfy
    """

    def __init__(self, a, alpha, beta, b, iden=False, dependency=True):
        # special case when alpha equals to beta, then a must be 1 and W+ equals to W-
        # b equals to c, could be assigned with any positive values, we default it as b = 2
        # dependency is True i.f.f W^+ = aW^d. Otherwise, W^+ and W^- are generated independently

        self.iden = iden
        self.dependency = dependency

        if dependency:
            self.d = beta/ alpha
            self.beta = beta
            self.alpha = alpha

            if self.alpha == self.beta:
                if b is None:
                    b = 10  # set default value to be 10
                else:
                    self.b = b
                self.a = 1
                self.c = b

            else:
                self.a = a
                self.b = (self.alpha / (self.alpha - 1) * (beta - 1) / beta * a ** (self.alpha / beta)) ** (beta / (self.alpha - beta))
                self.c = (self.b / self.a) ** (self.alpha / self.beta)


            print("The parameters are:")
            print("a = ", self.a)
            print("b = ", self.b)
            print("c = ", self.c)
            print("d = ", self.d)
            print("alpha = ", self.alpha)
            print("beta = ", self.beta)

            self.e_w_minus = self.c * beta/ (beta - 1)
            self.e_w_plus = a*beta*self.c**self.d / (beta - self.d)

            self.params = {'a': self.a, 'd': self.d, 'beta': self.beta, 'alpha': self.alpha,
                           'b': self.b, 'c': self.c}

        else:

            self.alpha = alpha
            self.beta = beta
            self.b = b
            self.c = b * alpha * (beta - 1) / ((alpha - 1) * beta)


            print("The parameters are:")
            print("b = ", self.b)
            print("c = ", self.c)
            print("alpha = ", self.alpha)
            print("beta = ", self.beta)

            self.e_w_minus = self.c * beta / (beta - 1)
            self.e_w_plus = b * alpha / (alpha - 1)

            self.params = {'alpha': self.alpha, 'beta': self.beta, 'b': self.b, 'c': self.c}

        print("Sequence degree mean is ", self.e_w_plus)


    def gene_iid_pairs_of_w(self, n):

        w_minus = np.zeros(n)
        w_plus = np.zeros(n)

        for i in range(0, n):
            w_minus[i] = generate_w(self.c, self.beta)
            if self.dependency:
                w_plus[i] = self.a * w_minus[i] ** self.d
            else:
                w_plus[i] = generate_w(self.b, self.alpha)

        return w_plus, w_minus

    def gene_one_pair(self):
        """
        method to generate one sample (d+, d-)
        :return: tuple with a pair of d+ and d- 
        """
        w_minus = generate_w(self.c, self.beta)
        if self.dependency:
            w_plus = self.a * w_minus ** self.d
        else:
            w_plus = generate_w(self.b, self.alpha)
        # derive the sample degree from W+ and W-
        if not self.iden:
            d_plus = int(poisson(mu=w_plus).rvs())
            d_minus = int(poisson(mu=w_minus).rvs())
        else:
            d_plus = int(poisson(mu=w_plus).rvs())
            d_minus = d_plus

        return d_plus, d_minus

    def rvs(self, n):
        """
        # method to generate n sample pairs from the distribution
        :param n: number of sample pairs
        :return: tuple of n sample sequence pairs 
        """
        d_out = np.zeros(n, dtype=np.int)
        d_in = np.zeros(n, dtype=np.int)
        for i in range(0, n):
            pair = self.gene_one_pair()
            d_in[i] = pair[0]
            d_out[i] = pair[1]

        # print("mean of in-degree sequence: ", np.mean(d_in))
        # print("mean of out-degree sequence: ", np.mean(d_out))

        return d_in, d_out



def difference(bi_degree):
    """
    # a function that returns the difference between in-degree sequence and out-degree sequence
    :param bi_degree: the sample of bidegree sequence
    :return: the difference 
    """
    in_sum = sum(bi_degree[0])
    # print("in_sum", end=":")
    # print(in_sum)
    out_sum = sum(bi_degree[1])
    # print("out_sum", end=":")
    # print(out_sum)
    # denote delta_n as the difference
    delta_n = in_sum - out_sum
    return delta_n


# test for the convergence of bi_degree sequence
#N = range(1000,6000,1000)
#a = 2
#alpha = 3



def test():
    a = 1.2  # the lower bound for W+
    alpha = 3  # the power for W+
    beta = 3.5  # the power for W+

    d = beta / alpha

    n = 5000  # graph size

    pld = PowerLaw(a, alpha, beta)
    din, dout = pld.rvs(n)

    w_minus, w_plus = pld.gene_iid_pairs_of_w(n)
    print("mean of w_minus is ", np.mean(w_minus))
    print("mean of w_plus is ", np.mean(w_plus))

    print("mean of in-degree sequence is ", np.mean(din))
    print("mean of out-degree sequence is ", np.mean(dout))



def test_2(alpha, beta, b):
    n = 5000  # graph size
    # a does not matter
    pld = PowerLaw(1, alpha, beta, b, dependency=False)
    din, dout = pld.rvs(n)

    w_minus, w_plus = pld.gene_iid_pairs_of_w(n)
    print("mean of w_minus is ", np.mean(w_minus))
    print("mean of w_plus is ", np.mean(w_plus))

    print("mean of in-degree sequence is ", np.mean(din))
    print("mean of out-degree sequence is ", np.mean(dout))


def test_din(a, alpha, beta, b=None, dep=True, n=2000):
    """
    :param a: 
    :param alpha: 
    :param beta: 
    :param b: 
    :param dep: 
    :param n: size of sequence
    :return: P(din=0), P(dout=0), sample mean of e^[-w+], sample mean of e^[-W-]
    """

    pl = PowerLaw(a, alpha, beta, b, dependency=dep)
    w_minus, w_plus = pl.gene_iid_pairs_of_w(n)

    d_out = np.zeros(n, dtype=np.int)
    d_in = np.zeros(n, dtype=np.int)
    for i in range(0, n):
        d_in[i] = int(poisson(mu=w_plus[i]).rvs())
        d_out[i] = int(poisson(mu=w_minus[i]).rvs())

    p1 = 0
    p2 = 0
    for d in d_in:
        if d == 0:
            p1 += 1
    for d in d_out:
        if d == 0:
            p2 += 1
    p1 /= n
    p2 /= n

    e_w_plus = np.array([exp(-w) for w in w_plus])
    e_w_minus = np.array([exp(-w) for w in w_minus])

    return p1, p2, e_w_plus.mean(), e_w_minus.mean()



def integ(alpha, b):
    """
    :param alpha: 
    :param b: 
    :return: integral of -alpha * b * e^(-x) * x ^(-alpha-1), from b to infty
    That is the integral of e^-W+ from b to infty
    That is E[e^[-W+]]
    """
    result = integrate(sp_exp(-x) * x**(-alpha-1), (x, b, float("inf")))
    result *= -alpha * b **alpha
    return result

def test_din_coh(alpha, beta, E, d, n=2000):
    """
    :return: P(din=0), P(dout=0), sample mean of e^[-w+], sample mean of e^[-W-]
    """

    pl = coherent_power_Law(alpha, beta, E, d)
    w_minus, w_plus = pl.gene_iid_pairs_of_w(n)

    d_out = np.zeros(n, dtype=np.int)
    d_in = np.zeros(n, dtype=np.int)

    for i in range(0, n):
        d_in[i] = int(poisson(mu=w_plus[i]).rvs())
        d_out[i] = int(poisson(mu=w_minus[i]).rvs())

    p1 = 0
    p2 = 0
    for d in d_in:
        if d == 0:
            p1 += 1
    for d in d_out:
        if d == 0:
            p2 += 1
    p1 /= n
    p2 /= n

    e_w_plus = np.array([exp(-w) for w in w_plus])
    e_w_minus = np.array([exp(-w) for w in w_minus])

    return p1, p2, e_w_plus.mean(), e_w_minus.mean()


class coherent_power_Law(PowerLaw):

    def __init__(self, alpha, beta, E, d, iden=False):
        # special case when alpha equals to beta, then a must be 1 and W+ equals to W-
        # b equals to c, could be assigned with any positive values, we default it as b = 2
        # dependency is True i.f.f W^+ = aW^d. Otherwise, W^+ and W^- are generated independently

        self.alpha = alpha
        self.beta = beta
        self.iden = iden ## whether perfected correlated or not
        self.s = beta / alpha
        self.E = E   ## expected degree E
        self.d = d

        self.dependency = True ## keep the default variable

        self.c = E * (beta - 1) / beta
        self.b = E * (alpha- 1) / alpha
        self.a = self.c **((alpha - beta) / alpha) * (beta * (alpha - 1)) / (alpha * (beta - 1))

        self.params = {'alpha': self.alpha, 'beta': self.beta, 's': self.s, 'Expected degree': self.E, 'd': self.d,
                       'c': self.c, 'b': self.b, 'a': self.a}

        print("The parameters are:")
        print("b = ", self.b)
        print("c = ", self.c)
        print("d = ", self.d)
        print("alpha = ", self.alpha)
        print("beta = ", self.beta)
        print("s =", self.s)

        self.e_w_minus = self.c * beta / (beta - 1)
        # self.e_w_plus = self.b * alpha / (alpha - 1)

        print("Sequence degree mean is ", self.e_w_minus)

    def gene_one_pair(self):
        """
        method to generate one sample (d+, d-)
        :return: tuple with a pair of d+ and d-
        """

        # derive the sample degree from W+ and W-
        if self.iden:
            w_plus = generate_w(self.c, self.alpha)
            d_plus = int(poisson(mu=w_plus).rvs())
            d_minus = d_plus
        else:
            w_minus = generate_w(self.c, self.beta)

            w_minus_copy = generate_w(self.c, self.beta)  ## indep copy of W-

            w_plus = self.a * self.d * w_minus ** self.s + self.a * (1 - self.d) * w_minus_copy ** self.s

            d_plus = int(poisson(mu=w_plus).rvs())
            d_minus = int(poisson(mu=w_minus).rvs())

        return d_plus, d_minus


    def gene_iid_pairs_of_w(self, n):

        w_minus = np.zeros(n)
        w_plus = np.zeros(n)

        for i in range(0, n):
            w_minus[i] = generate_w(self.c, self.beta)

            w_minus_copy = generate_w(self.c, self.beta)

            w_plus[i] = self.a * self.d * w_minus[i] ** self.s + self.a * (1 - self.d) * w_minus_copy ** self.s


        return w_plus, w_minus


def get_sample_corr(alpha, beta, E, d, n):
    co = coherent_power_Law(alpha, beta, E, d)
    d_in, d_out = co.rvs(n)
    return d_in, d_out, st.pearsonr(d_in, d_out)[0]


def test_coherent_degree_corr(alpha, beta, E, d, n, m):
    # m : simulation times
    corrs = []
    d_ins = []
    d_outs = []
    for i in range(0, m):
        result = get_sample_corr(alpha, beta, E, d, n)
        d_ins.append(result[0])
        d_outs.append(result[1])
        corrs.append(result[2])

    corrs = np.array(corrs)

    return d_ins, d_outs, corrs

