import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Exercise 1
# Part a

from synoptic_exercise_optimization import lennard_jones

# Part b

starting = [3.2, 4.4, 6.0]
for x_0 in starting:
    result = minimize(lennard_jones, x0=x_0, args=(1e5, 40))

# Part c

    print(f"Starting point: {x_0}, Optimal distance (r): {result.x}, Iterations: {result.nit}")

# Exercise 2
# Part a

def dihedral_potential(theta, A1=55.229, A2=3.3472, A3=-58.576):
    """
    Compute the dihedral potential energy.

    Args:
        theta (float): The dihedral angle.
        A1 (float): The first Fourier coefficient.
        A2 (float): The second Fourier coefficient.
        A3 (float): The third Fourier coefficient.

    Returns:
        float: The dihedral potential energy.
    """
    return 0.5 * (A1 * (1 + np.cos(theta)) + A2 * (1 + np.cos(2 * theta)) + A3 * (1 + np.cos(3 * theta)))

if __name__ == "__main__":
    theta_dot = np.linspace(-1 * np.pi, np.pi, 500)
    potential_energy = dihedral_potential(theta_dot)
    plt.figure(1)
    plt.plot(theta_dot, potential_energy, label='Dihedral Potential')
    plt.xlabel('Dihedral Angle (theta)')
    plt.ylabel('Potential Energy')
    plt.title('Dihedral Potential Energy')
    plt.axhline(0, color='gray', linestyle='--', label='Zero Potential')
    plt.legend()
    plt.show()

# Part b

if __name__ == "__main__":
    starting_theta = [0, np.pi, 0.5 * np.pi, -1 * np.pi, -0.5 * np.pi]
    for theta_0 in starting_theta:
        result = minimize(dihedral_potential, x0=theta_0, args=(55.229, 3.3472, -58.576))
        print(f"Starting angle: {theta_0}, Optimal angle (theta): {result.x}, Iterations: {result.nit}")

# Part c

if __name__ == "__main__":
    start_angles = np.linspace(-1 * np.pi, np.pi, 20)
    start_positions = []
    final_positions = []
    for theta_0 in start_angles:
        result = minimize(dihedral_potential, x0=theta_0, args=(55.229, 3.3472, -58.576))
        start_positions.append(theta_0)
        final_positions.append(result.x)

# Part d

if __name__ == "__main__":
    plt.figure(2)
    plt.scatter(start_positions, final_positions, label='Optimization Results')
    plt.xlabel('Starting Angle (theta)')
    plt.ylabel('Final Angle (theta)')
    plt.title('Dihedral Angle Optimization')
    plt.legend()
    plt.grid(True, linestyle='--')
    plt.show()