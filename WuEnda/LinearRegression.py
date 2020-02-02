import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 100)
y = x * 2 + 0.2
# hypothesis y = a + bx
t1 = t2 = 0


class Hypothesis(object):
    def __init__(self, a, b, m, lr):
        self.a = a
        self.b = b
        self.m = m
        self.lr = lr

    def calculate(self, i):
        return self.a + self.b * i

    def iteration(self, i, j):
        while round(sum(self.calculate(i) - j), 8) != 0:
            temp = sum(self.calculate(i) - j)
            temp2 = sum((self.calculate(i) - j) * i)
            self.a = self.a - self.lr * (1 / self.m) * temp
            self.b = self.b - self.lr * (1 / self.m) * temp2
            plt.cla()
            plt.scatter(i, j)
            plt.plot(i, hypo.a + hypo.b * i, 'r-', lw=5)
            plt.text(0.5, 0, "y = %.2f  +  %.2f x" % (self.a, self.b), fontdict={'size': 20, 'color': 'red'})
            plt.pause(0.1)

    def __str__(self):
        return "y = %.2f  +  %.2f x" % (self.a, self.b)


hypo = Hypothesis(t1, t2, 100, 0.2)
hypo.iteration(x, y)
print(hypo)

plt.show()