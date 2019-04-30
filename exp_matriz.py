import numpy as np
import matplotlib.pyplot as plt

A = np.array([[-3,3],[5,-5]])

t = np.arange(0, 10, 0.01)

B = np.zeros((len(t),2,2))

for i in range(0, len(t)):
    B[i] = np.exp(A*t[i])


plt.loglog(t, B[:, 0, 0], label='-12')
plt.loglog(t, B[:, 0, 1], label='12')
plt.loglog(t, B[:, 1, 0], label='3')
plt.loglog(t, B[:, 1, 1], label='-3')
plt.legend(loc='upper left')
plt.title('Exponential matrix 2,2')
plt.show()