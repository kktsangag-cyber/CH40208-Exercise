import numpy as np

# Part 1

def calculate_energy(spins, J=0.012):
    """
    Calculate the energy of a 1D Ising model.

    Arg:
    spins: Array of spin values (+1 or -1)
    J: Coupling constant (default: 0.012 eV)
    """
    neighbor_spins = np.concatenate((spins[1:], spins[:1]))
    energy = -J * np.sum(neighbor_spins * spins) # np.roll(spins, -1) == spins[1:] + spins[:1]
    return energy

# Part 2

def Boltzmann_factor(energy_difference, temperature=1000):
    """
    Calculate the Boltzmann factor for a given energy difference and temperature.

    Args:
    energy_difference: The difference in energy (E_final - E_initial)
    temperature: The temperature (in Kelvin)

    Returns:
    The Boltzmann factor (exp(-ΔE / (kB * T)))
    """
    kB = 8.617333262145e-5  # Boltzmann constant in eV/K
    return np.exp(-energy_difference / (kB * temperature))

def metropolis_step(current_state, temperature=1000):
    """
    Perform a single Metropolis step.

    Args:
    current_state: The current state of the system (array of spins)
    temperature: The temperature (in Kelvin)

    Returns:
    The new state of the system after the Metropolis step
    """
    new_state = current_state.copy()
    random_flip = np.random.randint(len(current_state))
    new_state[random_flip] *= -1  # Flip the spin

    delta_E = calculate_energy(new_state) - calculate_energy(current_state)
    if delta_E < 0 or np.random.rand() <= Boltzmann_factor(delta_E, temperature):
        return new_state  # Accept the new state
    return current_state  # Reject the new state

# Part 3

def magnetization(spins):
    """
    Calculate the magnetization of a 1D Ising model.

    Args:
    spins: Array of spin values (+1 or -1)

    Returns:
    The magnetization (average spin)
    """
    return np.abs(np.mean(spins))

# Part 4

magnetization_hist = []

def multiple_metropolis_steps(initial_state, num_steps, temperature=1000):
    """
    Perform multiple Metropolis steps starting from an initial state.

    Args:
    initial_state: The initial state of the system (array of spins)
    num_steps: The number of Metropolis steps to perform
    temperature: The temperature (in Kelvin)

    Returns:
    The final state of the system after the specified number of steps
    """
    current_state = initial_state.copy()
    for _ in range(num_steps):
        current_state = metropolis_step(current_state, temperature)
        print(f"Current state: {current_state}, Energy: {calculate_energy(current_state)}, Magnetization: {magnetization(current_state)}")
        magnetization_hist.append(magnetization(current_state))
    return current_state, magnetization_hist

if __name__ == "__main__":
    random_initial_state = np.random.choice([-1, 1], size=4)
    final_state, magnetization_hist = multiple_metropolis_steps(random_initial_state, 1000)
    print(f"<M>: {np.mean(magnetization_hist):.2f}")

# Part 5

import matplotlib.pyplot as plt

magnetization_mean_hist = []

if __name__ == "__main__":
    temperature_range = np.linspace(1e-19, 2000, 100)
    for T in temperature_range:
        random_initial_state = np.random.choice([-1, 1], size=4)
        _, magnetization_hist = multiple_metropolis_steps(random_initial_state, 1000, temperature=T)
        magnetization_mean_hist.append(np.mean(magnetization_hist))

    plt.plot(temperature_range, magnetization_mean_hist)
    plt.xlabel("Temperature (K)")
    plt.ylabel("<M>")
    plt.title("Mean Magnetization vs Temperature")
    plt.show()

# Bonus

def statistical_mechanics(m_list, g_list, E_list, temperature=1000):
    """
    Calculate the partition function and free energy for a 1D Ising model.

    Args:
    m_list: Array of the mean magnetization of the system
    g_list: Array of the degeneracy of the system (number of microstates)
    E_list: Array of the energy of the system
    temperature: The temperature of the system (in Kelvin)

    Returns:
    Mean magnetization (M)
    """
    kB = 8.617333262145e-5  # Boltzmann constant in eV/K
    weight = g_list * np.exp(-E_list / (kB * temperature))
    partition_function = np.sum(weight)
    mean_magnetization = np.sum(np.abs(m_list) * weight) / partition_function
    return mean_magnetization

if __name__ == "__main__":
    J = 0.012
    m_list = np.array([0.0, 0.0, 0.5, 1.0])
    g_list = np.array([2, 4, 8, 2])
    E_list = np.array([4*J, 0, 0, -4*J])

    high_T_limit = np.sum(m_list * g_list) / 16 # As T approaches infinity, exp(-E/kT) approaches 1 for all states

    temperature_range = np.linspace(1e-19, 2000, 50)
    sim_results = []
    exact_results = []

    for T in temperature_range:
        magnetization_hist = []
        _, hist = multiple_metropolis_steps(np.random.choice([-1, 1], 4), 2000, temperature=T)
        sim_results.append(np.mean(hist))
        
        exact_results.append(statistical_mechanics(m_list, g_list, E_list, temperature=T))

    plt.figure(figsize=(10, 6))
    plt.scatter(temperature_range, sim_results, label='Metropolis Simulation', color='blue', alpha=0.6)
    plt.plot(temperature_range, exact_results, label='Exact Theory', color='red', linewidth=2)
    plt.axhline(high_T_limit, color='green', linestyle='--', label=f'High-T Limit ({high_T_limit})')

    plt.xlabel("Temperature (K)")
    plt.ylabel("<|M|>")
    plt.title("Ising Model (N=4): Simulation vs Theory")
    plt.legend()
    plt.grid(True)
    plt.savefig('ising_model_comparison.png', dpi=300)
    plt.show()