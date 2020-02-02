import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# hypothesis y = a + bx + cz + ...
x = np.linspace(-2, 2, 100)
y = np.linspace(0, 4, 100)
X, Y = np.meshgrid(x, y)
put = []
x_in, y_in, z_in = [],[],[]
Z = X * 2 + Y * 3 + 5
for p in x:
    for q in y:
        x_in.append(p)
        y_in.append(q)
        z_in.append(p * 2 + q * 3 + 5)

fig = plt.figure(1)
ax = Axes3D(fig)
# ax.scatter(X, Y, Z)
inp = [np.ones(len(z_in)),  x_in, y_in]
ip = np.array(inp)
print(ip)
th = np.array([0, 0, 0])
z = np.array(z_in)


class HypothesisTwo(object):
    def __init__(self, dimension, m, lr):
        self.theta = np.array([0, 0, 0])
        self.m = m
        self.lr = lr
        self.dimension = dimension

    def calculate(self, i):
        return np.dot(self.theta, i)

    def iteration(self, i, j):
        while round(np.sum(self.calculate(i) - j), 5) != 0:
            temp = []
            for h in range(self.dimension):
                temp.append(self.theta[h] - self.lr * (1 / self.m) * np.sum((self.calculate(i) - j) * i[h]))
            self.theta = np.array(temp)
            ax.cla()
            ax.scatter(X, Y, Z,color="blue")
            ax.plot_surface(X, Y, self.theta[0]+self.theta[1]*X + self.theta[2]*Y,color="red")
            ax.text(0,0,-1,self.__str__(),fontdict={'size': 10, 'color': 'red'})
            plt.pause(0.1)
            # plt.cla()
            # plt.scatter(i, j)
            # plt.plot(i, hypo.a + hypo.b * i, 'r-', lw=5)
            # plt.text(0.5, 0, "y = %.2f  +  %.2f x" % (self.a, self.b), fontdict={'size': 20, 'color': 'red'})
            #

    def __str__(self):
        out = ""
        for l in range(self.dimension):
            if l == 0:
                out = out + "z = %.2f " % self.theta[l]
            else:
                out = out + "+ %.2f*x%d " % (self.theta[l], l)
        return out


hypo = HypothesisTwo(3, len(z_in), 0.1)

hypo.iteration(ip, z)
print(hypo)

# plt.show()
