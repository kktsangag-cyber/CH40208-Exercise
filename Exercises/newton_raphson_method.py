import numpy as np
import matplotlib.pyplot as plt

def newton_raphson_harmonic(k, r_0, x0):
    """
    Perform Newton-Raphson method to minimize a harmonic potential energy function.

    Args:
        k (float): Bond force constant.
        r_0 (float): Equilibrium bond length.
        x0 (float): The initial guess for the bond length.
        max_iter (int): The maximum number of iterations.

    Returns:
        float: The optimized bond length.
    """
    r_val = x0
    grad = k * (r_val - r_0)
    r_val = r_val - grad / k
    print(f"At iteration 1, position: {r_val} and gradient: {grad}")
    return r_val, grad

plt.figure(1)
r, grad = newton_raphson_harmonic(36.0, 0.74, 1.5)
plt.plot(r, grad, 'o-')
plt.xlabel("Bond Length")
plt.ylabel("Gradient")
plt.title("Newton-Raphson Optimization")
plt.show(block=False)

plt.figure(2)
plt.plot(1, r, 'o-')
plt.xlabel("Iteration")
plt.ylabel("Bond Length")
plt.title("Bond Length Convergence")
plt.show()

# It works perfectly for this simple harmonic potential
# because it is already a quadratic function.
# Therefore, the Newton-Raphson method converges in one step for any initial guess.
# For more complex functions, the method may require multiple iterations to converge,
# or fail to converge.
# Common practice: use gradient descent first
# and then switch to Newton-Raphson for more accurate results.