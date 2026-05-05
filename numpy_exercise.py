import numpy as np

# Exercise 1: Average Atomic Mass
Sn_atomic_mass = np.array((112, 114, 115, 116, 117, 118, 119, 120, 122, 144))
Sn_abundance = np.array((0.0097, 0.0066, 0.0034, 0.1454, 0.0768, 0.2422, 0.0859, 0.3258, 0.0463, 0.0579))
print(f"Average atomic mass of Sn: {np.average(Sn_atomic_mass, weights=Sn_abundance)}")

# Exercise 2: Molecular Distances of NH3

atom_N = ([0.0, 0.0, 0.0])       # Nitrogen at origin
atom_H1 = ([0.0, 0.94, 0.38])    # Hydrogen 1
atom_H2 = ([0.81, -0.47, 0.38])  # Hydrogen 2
atom_H3 = ([-0.81, -0.47, 0.38]) # Hydrogen 3
atoms_NH3 = np.array([atom_N, atom_H1, atom_H2, atom_H3])
name_NH3 = ["N", "H_1", "H_2", "H_3"]

for i in range(len(atoms_NH3)):
    for j in range(i+1, len(atoms_NH3)):
        atom_1 = atoms_NH3[i]
        atom_2 = atoms_NH3[j]
        distance = np.linalg.norm(atom_1 - atom_2)
        print(f"Distance between {name_NH3[i]} and {name_NH3[j]}: {distance:.2f} Å")

# Exercise 3: Analysis of Experimental Data
times = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])  # minutes
absorbance = np.array([1.85, 1.52, 1.31, 1.08, 0.89, 0.71, 0.58, 0.49, 0.38, 0.32, 0.28])
i = int(input("Enter the first time point (in every 2 minutes): "))
j = int(input("Enter the second time point (in every 2 minutes): "))

for k in range(len(times)):
    if times[k] == i:
        time_i = times[k]
        absorbance_i = absorbance[k]
    if times[k] == j:
        time_j = times[k]
        absorbance_j = absorbance[k]
print(f"Relative absorbance at time point {i} mins: {absorbance_i/absorbance[0]:.2f}")
print(f"Relative absorbance at time point {j} mins: {absorbance_j/absorbance[0]:.2f}")
print(f"Change in absorbance between {i} and {j} mins: {(absorbance_j) - (absorbance_i):.2f}")

absorbance_half = np.where(absorbance < absorbance[0]/2)[0]
absorbance_05 = np.where(absorbance < 0.5)[0]

if len(absorbance_half) > 0:
    print(f"Half value reached at: {times[absorbance_half[0]]} mins")

if len(absorbance_05) > 0:
    print(f"Below 0.5 reached at: {times[absorbance_05[0]]} mins")