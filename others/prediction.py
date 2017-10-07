import numpy as np
import random
from numpy import genfromtxt
import matplotlib.pyplot as plt
from math import sqrt


def get_train_data(dataset):
    # column -- of the same features
    # row -- one sample of different features
    m, n = np.shape(dataset)
    train_data = np.ones((m, n - 1))
    train_data[:, 1:n - 2] = dataset[:, 1:n - 2]
    train_label = dataset[:, n - 1]
    return train_data, train_label


def get_test_data(dataset):
    m, n = np.shape(dataset)
    test_data = np.ones((m, n))
    test_data[:, 1:] = normalize(dataset[:, 1:])
    return test_data


def get_res_data(ref, m):
    res = np.ones((m, 2))
    res[:, 1] = ref[:]
    for i in range(0, m):
        res[i][0] = i
    return res


def normalize(x):
    m, n = np.shape(x)
    for i in range(0, n):
        tmp = np.ones((m))
        tmp[:] = x[:, i]
        # mean = np.mean(tmp)
        # dev = np.sqrt(np.var(tmp))
        mu = tmp.mean()
        std = tmp.std()
        flag = 0
        if std == 0:
            if -1 <= tmp[0] <= 1:
                continue
            flag = 1
        if flag == 1:
            x[:, i] = np.ones(m)
        else:
            x[:, i] = (x[:, i] - mu) / std
    return x


def gradient_descent(x, y, theta, alpha, m, numIterations):
    x_trans = x.transpose()
    size = len(y)
    cost = []
    for i in range(0, numIterations):
        hypothesis = np.dot(x, theta)
        loss = hypothesis - y
        gradient = np.dot(x_trans, loss) / size
        theta = theta - alpha * gradient
        cost.append((np.dot(loss, loss)) / 2 / size)
        l = len(cost)
        if l > 2:
            if abs(cost[l - 1] - cost[l - 2]) / cost[l - 2] < 1e-6:
                break

    return theta, cost


def predict(x, theta):
    m, n = np.shape(x)
    x_test = np.ones((m, n))
    x_test[:, :] = x
    reference = np.dot(x_test, theta)
    return reference


# dataSet = genfromtxt("test.csv", delimiter=',', skip_header=1)
# x = getTestData(dataSet)
# np.savetxt('getNormal.csv', x, fmt="%f", delimiter = ',')

dataset = genfromtxt("train.csv", delimiter=',', skip_header=1)
train_data, train_label = get_train_data(dataset)
m, n = np.shape(train_data)
theta = np.ones(n)
alpha = 0.06
numIterations = 5000
theta, cost = gradient_descent(train_data, train_label, theta, alpha, m, numIterations)

dataset = genfromtxt("test.csv", delimiter=',', skip_header=1)
x = get_test_data(dataset)
ref = predict(x, theta)
res = get_res_data(ref, m)
np.savetxt('res.csv', res, fmt="%i, %f", delimiter=',')