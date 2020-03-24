import torch
import matplotlib.pyplot as plt
import numpy as np

x = torch.randn(64,1000)
y = torch.randn(64,1)

w1 = torch.randn(1000, 100, requires_grad=True)
w2 = torch.randn(100, 1, requires_grad=True)

lr = 1e-6

for it in range(1000):
    # forward
    h = x.mm(w1).clamp(min=0).mm(w2)

    # cost
    loss = torch.pow(h - y,2).sum()
    print(it, loss.item())

    # bp
    loss.backward()
    with torch.no_grad():
        w1 -= lr * w1.grad
        w2 -= lr * w2.grad
        w1.grad.zero_()
        w2.grad.zero_()

plt.figure()
plt.scatter(h.detach().numpy(),y.numpy())
# plt.plot(y,h)
plt.show()

