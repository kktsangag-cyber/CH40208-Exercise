import numpy as np
import matplotlib.pyplot as plt

# Exercise 1a

def p_e_s_diatomic(k, r, r_0):
    """Calculate the potential energy surface of a diatomic molecule using the harmonic potential.

    Args:
        k (float): Bond force constant.
        r (float): Current bond length.
        r_0 (float): Equilibrium bond length.

    Returns:
        float: Potential energy.
    """
    return k * (r - r_0)**2

if __name__ == "__main__":
    r = np.linspace(0.38, 1.1, 501)
    r_0 = 0.74  # Equilibrium bond length
    k = 575     # N/m
    k_J_per_Angstrom_square = k * 1e-20
    # Calculate potential energy surface
    potential_energy_1 = p_e_s_diatomic(k_J_per_Angstrom_square, r, r_0)

    # Plotting
    plt.figure(1)
    plt.plot(r, potential_energy_1)
    plt.xlabel('Bond Length (r)')
    plt.ylabel('Potential Energy')
    plt.title('Potential Energy Surface of a Diatomic Molecule')
    plt.scatter(r_0, p_e_s_diatomic(k_J_per_Angstrom_square, r_0, r_0), color='red', label='Equilibrium Bond Length')
    plt.axhline(0, color='gray', linestyle='--', label='Zero Potential Energy')
    plt.legend()
    plt.show(block=False)

# Exercise 1b

def force_diatomic(k, r, r_0):
    """
    Calculate the force acting on the system using the harmonic potential.

    Args:
        k (float): Bond force constant.
        r (float): Current bond length.
        r_0 (float): Equilibrium bond length.

    Returns:
        float: Force acting on the bond.
    """
    force = -2 * k * (r - r_0)
    return force

if __name__ == "__main__":
    k_N_per_Angstrom = k * 1e-10
    force = force_diatomic(k_N_per_Angstrom, r, r_0)

    # Plotting the force
    plt.figure(2)
    plt.plot(r, force)
    plt.xlabel('Bond Length (r)')
    plt.ylabel('Force (N)')
    plt.title('Force Acting on the System')
    plt.axhline(0, color='gray', linestyle='--', label='Zero Force')
    plt.legend()
    plt.show(block=False)

# Exercise 2ab

def accelerate(force, mass):
    """Calculate the acceleration of the system.

    Args:
        velocity (float): Current velocity.
        force (float): Force acting on the system.
        mass (float): Mass of the system.

    Returns:
        float: Acceleration.
    """
    return (force / mass) * 1e10 # Convert from m/s^2 to Å/s^2

def euler_integration(position, velocity, acceleration, dt):
    """Perform a single step of Euler integration.

    Args:
        position (float): Current position.
        velocity (float): Current velocity.
        acceleration (float): Current acceleration.
        dt (float): Time step.

    Returns:
        tuple: Updated position and velocity.
    """
    new_velocity = float(velocity + acceleration * dt)
    new_position = float(position + velocity * dt + 0.5 * acceleration * dt**2)
    new_acceleration = float(accelerate(force_diatomic(k_N_per_Angstrom, new_position, r_0), mass))
    position_hist.append(new_position)
    velocity_hist.append(new_velocity)
    return new_position, new_velocity, new_acceleration

if __name__ == "__main__":
    position = 1.0
    velocity = 0.0
    acceleration = force_diatomic(k_N_per_Angstrom, position, r_0)
    mass = 0.5
    delta_t = 1e-5
    times = 500000

    position_hist = [position]
    velocity_hist = [velocity]

    for t in range(times):
        position, velocity, acceleration = euler_integration(position, velocity, acceleration, delta_t)

    time = np.linspace(0, times * delta_t, len(position_hist))
    plt.figure(3)
    plt.plot(time, position_hist, label='Position')
    plt.xlabel('Time (s)')
    plt.ylabel('Position (Å)')
    plt.title('Position vs Time')
    plt.legend()
    plt.show(block=False)

# Exercise 2c

if __name__ == "__main__":
    plt.figure(4)
    plt.hist(position_hist, bins=100, density=True)
    plt.xlabel('Position (Å)')
    plt.ylabel('Probability Density')
    plt.title('Position Distribution')
    plt.show(block=False)

# Exercise 2d

if __name__ == "__main__":
    plt.figure(5)
    potential_energy_2 = []
    kinetic_energy_2 = []
    total_energy_2 = []
    for i in range(len(position_hist)):
        potential_energy_2.append(p_e_s_diatomic(k_J_per_Angstrom_square, position_hist[i], r_0))
        kinetic_energy_2.append(0.5 * mass * (velocity_hist[i] * 1e-10)**2) # Convert from (Å/s)^2 to (m/s)^2
        total_energy_2.append(potential_energy_2[i] + kinetic_energy_2[i])
    plt.plot(time, potential_energy_2, label='Potential Energy')
    plt.plot(time, kinetic_energy_2, label='Kinetic Energy')
    plt.plot(time, total_energy_2, label='Total Energy')
    plt.xlabel('Time (s)')
    plt.ylabel('Energy (J)')
    plt.title('Energy vs Time')
    plt.legend()
    plt.savefig("Euler_Integration.png", dpi=300)
    plt.show(block=False)

# Exercise 3c

def verlet_integration(position, velocity, acceleration, dt):
    """Perform a single step of Verlet integration.

    Args:
        position (float): Current position.
        velocity (float): Current velocity.
        acceleration (float): Current acceleration.
        dt (float): Time step.

    Returns:
        tuple: Updated position and velocity.
    """
    new_position = position + velocity * dt + 0.5 * acceleration * dt**2
    new_acceleration = float(accelerate(force_diatomic(k_N_per_Angstrom, new_position, r_0), mass))
    new_velocity = velocity + 0.5 * (acceleration + new_acceleration) * dt
    return new_position, new_velocity, new_acceleration 

if __name__ == "__main__":
    pos = 1.0
    vel = 0.0
    acc = force_diatomic(k_N_per_Angstrom, pos, r_0) / mass
    plt.figure(6)
    potential_energy_3 = [p_e_s_diatomic(k_J_per_Angstrom_square, pos, r_0)]
    kinetic_energy_3 = [0.5 * mass * (vel * 1e-10)**2] # Convert from (Å/s)^2 to (m/s)^2
    total_energy_3 = [p_e_s_diatomic(k_J_per_Angstrom_square, pos, r_0) + 0.5 * mass * (vel * 1e-10)**2]
    for t in range(times):
        pos, vel, acc = verlet_integration(pos, vel, acc, delta_t)
        potential_energy_3.append(p_e_s_diatomic(k_J_per_Angstrom_square, pos, r_0))
        kinetic_energy_3.append(0.5 * mass * (vel * 1e-10)**2) # Convert from (Å/s)^2 to (m/s)^2
        total_energy_3.append(potential_energy_3[-1] + kinetic_energy_3[-1])
    plt.plot(time, potential_energy_3, label='Potential Energy')
    plt.plot(time, kinetic_energy_3, label='Kinetic Energy')
    plt.plot(time, total_energy_3, label='Total Energy')
    plt.xlabel('Time (s)')
    plt.ylabel('Energy (J)')
    plt.title('Energy vs Time')
    plt.legend()
    plt.savefig("Verlet_Integration.png", dpi=300)
    plt.show()