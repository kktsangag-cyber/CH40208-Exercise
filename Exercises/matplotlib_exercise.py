import matplotlib.pyplot as plt
import numpy as np

# Exercise 1
volume = np.array([0.0, 5.0, 10.0, 15.0, 20.0, 22.0, 24.0, 25.0, 26.0, 30.0])  # mL
pH = np.array([1.00, 1.2, 1.4, 1.7, 2.2, 3.0, 7.0, 11.0, 12.0, 12.5]) 
plt.figure(1, figsize=(7, 5))
plt.plot(volume, pH)
plt.xlabel('Volume of NaOH / mL')
plt.ylabel('pH')
plt.title('pH against Volume')
plt.show(block=False)

# Exercise 2
time = np.linspace(0, 30, 7) # min
absorbance_A = np.array([0.80, 0.68, 0.58, 0.49, 0.42, 0.36, 0.31])
absorbance_B = np.array([0.80, 0.60, 0.45, 0.34, 0.25, 0.19, 0.14])
plt.figure(2)
plt.plot(time, absorbance_A, label='Sample A')
plt.plot(time, absorbance_B, label='Sample B')
plt.xlabel('Time / min')
plt.ylabel('Absorbance')
plt.title('Absorbance vs Time')
plt.legend()
plt.show(block=False)

# Exercise 3
time = np.linspace(0, 60, 7)
conc_water = np.array([1.00, 0.61, 0.37, 0.22, 0.14, 0.08, 0.05])
conc_ethanol = np.array([1.00, 0.82, 0.67, 0.55, 0.45, 0.37, 0.30])
plt.figure(3)
plt.plot(time, conc_water, 'o-', label='Water')
plt.plot(time, conc_ethanol, 'o-', label='Ethanol')
plt.xlabel('Time / min')
plt.xlim(0, 60)
plt.ylabel('Concentration / M')
plt.yscale('log')
plt.title('Concentration vs Time')
plt.legend()
plt.show(block=False)

# Exercise 4
Concentration = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5]) #mM
Absorbance = np.array([0.00, 0.12, 0.24, 0.35, 0.48, 0.59])
Uncertainty = np.array([0.01, 0.02, 0.02, 0.03, 0.02, 0.03])
plt.figure(4)
plt.errorbar(Concentration, Absorbance, yerr=Uncertainty, fmt='o-', label='Calibration')
plt.axhline(y=0.36, linestyle='--', label='Unknown sample')
plt.xlabel('Concentration / mM')
plt.ylabel('Absorbance')
plt.legend()
plt.show()