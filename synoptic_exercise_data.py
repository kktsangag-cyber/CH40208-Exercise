import numpy as np
import matplotlib.pyplot as plt

# Exercise 1
# Part a
path_SF6 = '/Users/jasontsang/VScode/NumPy and SciPy/.venv/CH40208 Exercise/SF6_data.csv'
pressure, molar_volume = np.loadtxt(path_SF6, delimiter=',', unpack=True)
plt.figure(1)
plt.plot(pressure, molar_volume, 'o-', label='Experimental Data')
# Part b
def ideal_gas_law(v, T=298, R=8.31446):
    p = (R * T) / v
    return p / 100
v = np.linspace(6.87e-1, 4.47, 100)
p_ideal = ideal_gas_law(v)
plt.plot(p_ideal, v, '--', label='Ideal Gas Law')
# Part c
def Van_der_Waals_equation(v, T=298, R=8.31446):
    v_m3 = v / 1000
    a = 7.857e-1      # Pa * m^6 / mol^2
    b = 8.79e-5     # m^3 / mol
    p = (R * T) / (v_m3 - b) - a / v_m3**2
    return p / 1e5
p_vdw = Van_der_Waals_equation(v)
plt.plot(p_vdw, v, ':', label='Van der Waals Equation')
plt.xlabel('Pressure / bar')
plt.ylabel('Molar Volume / L mol$^{-1}$')
plt.title('Molar Volume against Pressure')
plt.legend()
plt.show(block=False)

# Exercise 2
# Part a
plt.figure(2)
path_ion = '/Users/jasontsang/VScode/NumPy and SciPy/.venv/CH40208 Exercise/ion_mean_activity_data.txt'
ionic_strength, mean_activity = np.loadtxt(path_ion, unpack=True)
plt.plot(ionic_strength, mean_activity, 's-', label='Experimental Data')
# Part b
def Debye_Huckel(ionic_strength, A=1.179):
    sprt_I = np.sqrt(ionic_strength)
    ln_gamma = -2 * A * sprt_I
    return np.exp(ln_gamma)
plt.plot(ionic_strength, Debye_Huckel(ionic_strength), 'd--', label='Debye-Hückel')
# Part c
def Extended_Debye_Huckel(ionic_strength, A=1.179, B=18.3, a_0 = 0.071):
    sprt_I = np.sqrt(ionic_strength)
    ln_gamma = (-2 * A * sprt_I) / (1 + B * a_0 * sprt_I)
    return np.exp(ln_gamma)
plt.plot(ionic_strength, Extended_Debye_Huckel(ionic_strength), 'o:', label='Extended Debye-Hückel')
plt.xlabel('Ionic Strength / mol L$^{-1}$')
plt.ylabel('Mean Activity')
plt.legend()
plt.show()
