import numpy as np
import matplotlib.pyplot as plt

# Exercise 1
inverse_temp = np.array([0.0025, 0.0027, 0.0029, 0.0031, 0.0033])  # K^-1
ln_k = np.array([-8.5, -7.8, -7.2, -6.7, -6.2])
plt.figure(1)
plt.plot(inverse_temp, ln_k, 'o-')
plt.xlabel(r'$T^{-1}$ / K$^{-1}$')
plt.ylabel(r'ln $k$')
plt.title('Arrhenius Plot')
plt.show()