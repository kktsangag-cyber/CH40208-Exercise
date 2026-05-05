import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import Rydberg, h, c

# Exercise 1
def energy_level(n):
    energy = (-Rydberg * h * c)/ (n**2)
    return energy
for x in range(1, 6):
    print(f"Energy level for n={x}: {energy_level(x):.2e} J")

# Exercise 2
def wavelength(n_1, n_2):
    wavelength = (Rydberg * (1/(n_1**2) - 1/(n_2**2)))**-1
    wavelength_nm = wavelength * 1e9
    return wavelength_nm
lyman = []
balmer = []
paschen = []
for m in range(1, 4):
    for x in range(m + 1, m + 11):
        if m == 1:
            print(f"Lyman series wavelength from n={x} to n={m}: {wavelength(m, x):.2f} nm")
            lyman.append(wavelength(m, x))
        elif m == 2:
            print(f"Balmer series wavelength from n={x} to n={m}: {wavelength(m, x):.2f} nm")
            balmer.append(wavelength(m, x))
        elif m == 3:
            print(f"Paschen series wavelength from n={x} to n={m}: {wavelength(m, x):.2f} nm")
            paschen.append(wavelength(m, x))
plt.figure(figsize=(12, 4))
plt.vlines(lyman, ymin=0, ymax=1, colors='pink', label='Lyman Series')
plt.vlines(balmer, ymin=0, ymax=1, colors='blue', label='Balmer Series')
plt.vlines(paschen, ymin=0, ymax=1, colors='green', label='Paschen Series')
plt.xlabel('Wavelength (nm)')
plt.xlim(0, 2000)
plt.legend()
plt.gca().get_yaxis().set_visible(False)
plt.title('Emission Spectra of Hydrogen Atom')
plt.savefig('H_emission.pdf', bbox_inches='tight')