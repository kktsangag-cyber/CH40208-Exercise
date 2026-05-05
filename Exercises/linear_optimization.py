import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 20)
y_true = 2 * x + 3
np.random.seed(42)
noise = np.random.normal(0, 1.5, size=20)
y_data = y_true + noise

# Exercise 1
def linear_model(x, m, c):
    """Calculate y values for a linear model y = mx + c.
    
    Args:
        x (float): Independent variable value(s).
        m (float): Slope parameter.
        c (float): Intercept parameter.
        
    Returns:
        float: Predicted y value(s).
    """
    y = m * x + c
    return y

# Exercise 2
def error_function(params, x_data, y_data):
    """Calculate sum-of-squares error for linear model.
    
    Args:
        params (list): List/array containing [slope, intercept].
        x_data (list): Observed x values.
        y_data (list): Observed y values.
        
    Returns:
        Chi-squared error value.
    """
    m, c = params
    y_model = linear_model(x_data, m, c)
    residuals = y_data - y_model
    return float(np.sum(residuals**2))

# Exercise 3
import scipy.optimize as opt
initial_guess = [1.0, 1.0]
result = opt.minimize(error_function, initial_guess, args=(x, y_data))
m_fit, c_fit = result.x
print(f"Best-fit parameters: m = {m_fit:.4f}, c = {c_fit:.4f}")
print(f"Chi-squared error: {result.fun:.4f}")
print(f"Number of iterations: {result.nit}")

# Exercise 4
plt.plot(x, y_true, color="gray", linestyle='--', label="True model")
plt.plot(x, linear_model(x, m_fit, c_fit), label="Fitted model")
plt.text(0.5, 20, f'Fitted: y = {m_fit:.3f}x + {c_fit:.3f}', fontsize=10)
plt.legend()
plt.show()

# Exercise 5
initial_guesses = [
    [1.0, 1.0],
    [0.0, 0.0],
    [5.0, 10.0],
    [-1.0, 8.0]
]
for i in initial_guesses:
    result = opt.minimize(error_function, i, args=(x, y_data))
    m_fit, c_fit = result.x
    print(f"Best-fit parameters: m = {m_fit:.4f}, c = {c_fit:.4f}")
    print(f"Chi-squared error: {result.fun:.4f}")
    print(f"Number of iterations: {result.nit}")