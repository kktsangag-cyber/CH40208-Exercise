import numpy as np
import matplotlib.pyplot as plt
# Exercise 1
def p_e_s_diatomic(k, r, r_0):
    """Calculate the potential energy surface of a diatomic molecule using the harmonic potential.
    
    Args:
        k (float): Bond force constant.
        r (float): Current bond length.
        r_0 (float): Equilibrium bond length.

    Returns:
        float: Potential energy.
    """
    return 0.5 * k * (r - r_0)**2

# Exercise 2
if __name__ == "__main__":
    r = np.linspace(0.38, 1.1, 101)
    r_0 = 0.74  # Equilibrium bond length
    k = 36.0     # eV/angstrom^2

# Calculate potential energy surface
if __name__ == "__main__":
    potential_energy = p_e_s_diatomic(k, r, r_0)

# Plotting
if __name__ == "__main__":
    plt.plot(r, potential_energy)

# Exercise 3
if __name__ == "__main__":
    plt.xlabel('Bond Length (r)')
    plt.ylabel('Potential Energy')
    plt.title('Potential Energy Surface of a Diatomic Molecule')
    plt.scatter(r_0, p_e_s_diatomic(k, r_0, r_0), color='red', label='Equilibrium Bond Length')
    plt.axhline(0, color='gray', linestyle='--', label='Zero Potential Energy')
    plt.legend()
    plt.show()

    print(f'Index of min value: {np.argmin(potential_energy)}')
    loc = np.argmin(potential_energy)
    print(f'The value at index {loc} is {potential_energy[loc]}')

