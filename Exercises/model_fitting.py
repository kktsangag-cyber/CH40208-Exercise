import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

# Exercise 1
# Part a
plt.figure(1)
path_data1 = '/Users/jasontsang/Documents/VS Code/NumPy and SciPy/CH40208 Exercise/Data/model_fitting_data1.txt'
temperature, equilibrium_constant = np.loadtxt(path_data1, unpack=True)

# Part b
inverse_temp = 1 / (temperature + 273)
ln_equilibrium_constant = np.log(equilibrium_constant)
plt.plot(inverse_temp, ln_equilibrium_constant, 'o', label='Data')

# Part c
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

def error_function_1_(params, x_data, y_data):
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

plt.plot(inverse_temp, linear_model(inverse_temp, 7400, -22.5), label='Test')

# Part d
initial_guess_1 = [7400, -22.5]
result = opt.minimize(error_function_1_, initial_guess_1, args=(inverse_temp, ln_equilibrium_constant))
m_fit, c_fit = result.x

# Part e
plt.plot(inverse_temp, linear_model(inverse_temp, m_fit, c_fit), "s--", label='Line of best fit')

# Part f
from scipy.stats import linregress
result = linregress(inverse_temp, ln_equilibrium_constant)
plt.plot(inverse_temp, linear_model(inverse_temp, result.slope, result.intercept), "d--", label='Line of best fit (linregress)')
plt.legend()
plt.show(block=False)

# Exercise 2
# Part a
path_data2 = '/Users/jasontsang/Documents/VS Code/NumPy and SciPy/CH40208 Exercise/Data/model_fitting_data2.txt'
time, concentration = np.loadtxt(path_data2, unpack=True)
plt.figure(2)
plt.plot(time, concentration, 'o', label='Data')

# Part b
def first_order(time, initial_concentration, rate_constant):
    """Calculate concentration of a first-order reaction over time.
    
    Args:
        time (array): Time values.
        initial_concentration (float): Initial concentration of the reactant.
        rate_constant (float): Rate constant for the reaction.
        
    Returns:
        array: Concentration values over time.
    """
    return initial_concentration * np.exp(-rate_constant * time)

# Part c
def error_function_2_(params, time_data, concentration_data):
    """Calculate sum-of-squares error for first-order model.
    
    Args:
        params (list): List/array containing [rate_constant, initial_concentration].
        time_data (list): Observed time values.
        concentration_data (list): Observed concentration values.
        
    Returns:
        Chi-squared error value.
    """
    rate_constant, initial_concentration = params
    y_model = first_order(time_data, initial_concentration, rate_constant)
    residuals = concentration_data - y_model
    return float(np.sum(residuals**2))

# Part d
initial_guess_2 = [0.1, 7]
result = opt.minimize(error_function_2_, initial_guess_2, args=(time, concentration))

# Part e
plt.plot(time, first_order(time, result.x[1], result.x[0]), "s--", label='Line of best fit')

# Part f
from scipy.optimize import curve_fit
popt, pcov = curve_fit(first_order, time, concentration)
plt.plot(time, first_order(time, *popt), "d--", label='Line of best fit (curve_fit)')

# Part g
ln_concentration = np.log(concentration)
optional = linregress(time, ln_concentration)
initial_guess_3 = [optional.slope, optional.intercept]
result_2 = opt.minimize(error_function_2_, initial_guess_3, args=(time, concentration))
plt.plot(time, first_order(time, result_2.x[1], result_2.x[0]), "--", label='Line of best fit (initial guess from linearization)')
plt.legend()
plt.show()