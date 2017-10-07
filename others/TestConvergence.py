import math
a = 1.2
alpha = 3
beta = 3.5

d = (alpha + 0.0) / beta

if alpha == beta:
    a = 1
    b = 2
    c = 2
else:
    b = (alpha / (alpha - 1) * (beta - 1) / beta * a ** (alpha / beta)) ** (beta / (alpha - beta))
    c = (b / a) ** (alpha / beta)

e_ww = -a * beta * c**beta / (d - beta + 1) * c**(d - beta + 1)
e_w = b * alpha / (alpha - 1)
lambda_1 = e_ww / e_w

def comp_e(beta, c):
    return beta * c**beta * (1.0/(beta - 2) * c**(2 - beta) - 1.0/(beta - 1) * c**(1-beta))

e = comp_e(beta, c) * (comp_e(alpha, b))
lambda_2 = e / (e_w**2)

print(lambda_1)
print(lambda_2)
print(math.exp(- lambda_1 - lambda_2))