import random
import numpy as np

def directed_gen(alpha, beta, fg, n):
    """
    a function that generates same-sum sample pair of bi-degree using the algorithm
    the function returns a tuple  (in-degree, out-degree)

    Input Parameters
    -----------------
    alpha: the power for W+ 
    beta: the power for W-
    fg: the distribution of bi-degree 
    n: simulation size
    """

    # derive kappa

    kappa = min(1 - 1/alpha, 1 - 1/beta, 1/2)
    delta_0 = 9.95 / 10 * kappa  # take a fixed delta0
    tol = n ** (1 - kappa + delta_0) # take the tolerance limit for delta_n

    # derive the sample bi-degree sequence
    bi_seq = fg.rvs(n)
    in_seq = bi_seq[0]  # the sample in-degree sequence, type: np.array
    out_seq = bi_seq[1]  # the sample out-degree sequence

    original_din = np.copy(in_seq)
    original_dout = np.copy(out_seq)

    # derive the Delta_n
    delta_n = n + 1

    i = 1
    # repeat sample generation until Delta_n is small enough to be "negligible"
    while abs(delta_n) > tol:
        print("Now executing the loops in ValidDegree")
        # repeat the sample working
        bi_seq = fg.rvs(n)
        in_seq = bi_seq[0]
        out_seq = bi_seq[1]

        original_din = np.copy(in_seq)
        original_dout = np.copy(out_seq)

        in_sum = sum(in_seq)
        out_sum = sum(out_seq)
        print("in_sum", end=":")
        print(in_sum)
        print("out_sum", end=":")
        print(out_sum)
        delta_n = in_sum - out_sum
        print(i)
        i += 1
        print(delta_n, tol)

    if abs(delta_n) > 0:
        # derive random sample node's index  delta_i
        delta_i = random.sample(range(0, n), int(abs(delta_n)))
        if delta_n > 0:  # in-degree sequence sum is larger , increase the random out-degree
            for i in delta_i:
                out_seq[i] += 1
               # print("add out degree sequence")
        else:  # out-degree is larger, increase the random in-degree
            for i in delta_i:
                in_seq[i] += 1
               # print("add in degree sequence")

        print("after, in_sum", end=":")
        print(sum(in_seq))
        print("after, out_sum", end=":")
        print(sum(out_seq))

    return in_seq, out_seq, original_din, original_dout
