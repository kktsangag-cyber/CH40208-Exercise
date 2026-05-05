import numpy as np
import matplotlib.pyplot as plt

# Exercise 1
plt.figure(1)
x = np.linspace(0, 10, 20)
y_true = 2 * x + 3
np.random.seed(42)
noise = np.random.normal(0, 1.5, size=20)
y_data = y_true + noise
plt.plot(x, y_true, 'o-', label="True")
plt.plot(x, y_data, 'o--', label="Data")
plt.legend()
plt.show(block=False)

# Exercise 2
plt.figure(2)
y_model = 2.0 * x + 3.0
residuals = y_data - y_model
for i in range(len(x)):
    plt.plot([x[i], x[i]], [y_data[i], y_model[i]], 'r-', alpha=0.5)
plt.plot(x, y_data, 'o--', label="Data")
plt.legend()
plt.show(block=False)

# Exercise 3
chi_squared = np.sum(residuals**2)
parameters_to_test = [
    (2.0, 3.0),   # True parameters
    (1.5, 3.0),   # Wrong slope
    (2.0, 4.0),   # Wrong intercept  
    (2.5, 2.0),   # Both wrong
    (1.0, 5.0),   # Both very wrong
]
chi_squared = []
for i in range(len(parameters_to_test)):
    slope, intercept = parameters_to_test[i]
    y_model = slope * x + intercept
    residuals = y_data - y_model
    chi_squared.append(float(np.sum(residuals**2)))
    print(f"Parameters: slope={slope}, intercept={intercept}, Chi-squared={chi_squared[-1]:.2f}")

# Exercise 4
X_matrix = np.vstack([x, np.ones_like(x)]) 
plt.figure(3)
plt.plot(x, y_data, 'o', label="Data")
plt.plot(x, np.array(parameters_to_test[0]) @ X_matrix, 's-', label=f"m=2.0, c=3.0, chi-squared={chi_squared[0]:.2f}")
plt.plot(x, np.array(parameters_to_test[1]) @ X_matrix, 'd--', label=f"m=1.5, c=3.0, chi-squared={chi_squared[1]:.2f}")
plt.plot(x, np.array(parameters_to_test[4]) @ X_matrix, 'x--', label=f"m=1.0, c=5.0, chi-squared={chi_squared[4]:.2f}")
plt.legend()
plt.show()
