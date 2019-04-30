import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm

A = np.array([[-3,3],[5,-5]])

t = np.arange(0, 10, 0.01)

B = np.zeros((len(t),2,2))

for i in range(0, len(t)):
    B[i] = expm(A*t[i])


plt.semilogx(t, B[:, 0, 0], label='-12')
plt.semilogx(t, B[:, 0, 1], label='12')
plt.semilogx(t, B[:, 1, 0], label='3')
plt.semilogx(t, B[:, 1, 1], label='-3')
plt.legend(loc='upper left')
plt.title('Exponential matrix 2,2')
plt.show()