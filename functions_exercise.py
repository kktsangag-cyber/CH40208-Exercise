import math

# Exercise 1
def calculate_h_plus(concentration, Ka):
    r1 = (-Ka + math.sqrt(Ka**2 + 4*Ka*concentration)) / 2
    return r1

def calculate_pH(h_plus, activity_coefficient=1.0):
    h_plus_effective = h_plus * activity_coefficient
    return -math.log10(h_plus_effective)

def calculate_percent_dissociation(h_plus, concentration):
    return (h_plus / concentration) * 100

concentration = float(input("What is the concentration of the acid (in M)? "))
Ka = float(input("What is the acid dissociation constant (Ka)? "))
activity_coefficient = input("What is the activity coefficient? ")

if activity_coefficient == "":
    h_plus = calculate_h_plus(concentration, Ka)
    pH = calculate_pH(h_plus)
else:
    h_plus = calculate_h_plus(concentration, Ka)
    pH = calculate_pH(h_plus, float(activity_coefficient))

percent_dissociation = calculate_percent_dissociation(h_plus, concentration)

print(f"Hydrogen ion concentration: {h_plus:.2e} M")
print(f"pH: {pH:.2f}")
print(f"Percent dissociation: {percent_dissociation:.2f}%")

# Exercise 4
def calculate_einstein_heat_capacity(temperature):
    """
    Determine the kinetic energy of a particle.
    
    Args: 
        theta_E (float): Einstein temperature (K)
        temperature (float): Particle temperature (K)
        R (float): Ideal gas constant (J/(mol*K))

    Returns:
        (float): heat capacity J/(mol*K)
    """
    R = 8.314  # J/(mol*K)
    heat_capacity = 3 * R * (theta_E / temperature)**2 * math.exp(theta_E / temperature) / (math.exp(theta_E / temperature) - 1)**2
    return heat_capacity

theta_E = float(input("What is the Einstein temperature (in K)? "))
temperature = float(input("What is the temperature (in K)? "))
print(f"Einstein heat capacity: {calculate_einstein_heat_capacity(temperature):.2f} J/(mol*K)")