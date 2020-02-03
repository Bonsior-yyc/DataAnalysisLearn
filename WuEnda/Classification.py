import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(1, 10, 100)
y = np.linspace(1, 10, 100)
x_in, y_in, z_in, x_i, y_i = [], [], [], [], []
for p in x:
    for q in y:
        if (p + q) % 0.3 != 0:
            x_in.append(p)
            y_in.append(q)
            if 2 * p + 3 * q >= 25 + np.random.randint(-5, 5, size=1):
                z_in.append(1)
            else:
                z_in.append(0)
for p in x:
    for q in y:
        x_i.append(p)
        y_i.append(q)
size = len(z_in)
inp = [np.ones(len(z_in)), x_in, y_in]
ip = np.array(inp)
print(ip)
th = np.array([0, 0, 0])
z = np.array(z_in)
print(size)
col = np.where(z_in, "red", "blue")
print(col)
print("pre_ok")
plt.figure(1)
plt.scatter(x_in, y_in, color=col)


class HypothesisClassification(object):

    def __init__(self, dimension, m, lr):
        self.theta = np.array([0, 0, 0])
        self.m = m
        self.lr = lr
        self.dimension = dimension

    def calculate(self, i):
        trans = np.dot(self.theta, i)
        for i in range(len(trans)):
            t = 1 / (1 + pow(math.e, (-1 * trans[i])))
            trans[i] = t
        return trans

    def iteration(self, i, j):
        while round(np.sum(self.calculate(i) - j), 5) != 0:
            temp = []
            for h in range(self.dimension):
                temp.append(self.theta[h] - self.lr * (1 / self.m) * np.sum((self.calculate(i) - j) * i[h]))
            self.theta = np.array(temp)
            plt.figure(2)
            plt.cla()
            plt.scatter(x_in, y_in, color=col)
            plt.scatter(i[1], i[2], color=np.where(self.calculate(i) > 0.5, "green", "yellow"))
            plt.pause(0.1)
            self.debug(i, j)

    def debug(self, i, j):
        print(self.calculate(i))
        print(self.theta)


hypo1 = HypothesisClassification(3, len(z_in), 0.15)
hypo1.iteration(inp, z_in)
