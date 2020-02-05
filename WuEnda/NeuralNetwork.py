import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(64,1000)
y = np.random.randn(64,1)

w1 = np.random.randn(1000, 100)
w2 = np.random.randn(100, 1)

lr = 1e-6

for it in range(1000):
    # forward
    h = x.dot(w1)
    relu = np.maximum(h, 0)
    y_pre = relu.dot(w2)

    # cost
    loss = np.square(y_pre - y).sum()
    print(it, loss)

    # bp
    grad_y = 2.0 * (y_pre - y)
    grad_w2 = relu.T.dot(grad_y)
    grad_relu = grad_y.dot(w2.T)
    grad_h = grad_relu.copy()
    grad_h[h < 0] = 0
    grad_w1 = x.T.dot(grad_h)

    w1 -= lr * grad_w1
    w2 -= lr * grad_w2

plt.figure()
plt.scatter(y_pre,y)
# plt.plot(y,y_pre)
plt.show()

