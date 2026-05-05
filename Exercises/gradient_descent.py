import numpy as np
import matplotlib.pyplot as plt

# Exercise 1

def gradient_descent_harmonic(k, r_0, x0, lr, max_iter=50):
    """
    Perform gradient descent to minimize a harmonic potential energy function.

    Args:
        k (float): Bond force constant.
        r_0 (float): Equilibrium bond length.
        x0 (float): The initial guess for the bond length.
        lr (float): The learning rate.
        max_iter (int): The maximum number of iterations.

    Returns:
        float: The optimized bond length.
    """
    r_val = x0
    r_history = []
    grad_history = []
    iteration = []
    for i in range(max_iter):
        grad = k * (r_val - r_0)
        if np.abs(grad).any() < 0.001:
            break
        r_val = r_val - lr * np.sign(grad)
        r_history.append(r_val)
        grad_history.append(grad)
        iteration.append(i + 1)
        print(f"At iteration {i + 1}, position: {r_val} and gradient: {grad}")
    return r_val, r_history, grad_history, iteration

plt.figure(1)
r, r_hist, grad_hist, iter_hist = gradient_descent_harmonic(36.0, 0.74, 1.0, 0.01)
plt.plot(r_hist, grad_hist)
plt.xlabel("Bond Length")
plt.ylabel("Gradient")
plt.title("Gradient Descent Optimization")
plt.show(block=False)

plt.figure(2)
plt.plot(iter_hist, r_hist)
plt.xlabel("Iteration")
plt.ylabel("Bond Length")
plt.title("Bond Length Convergence")
plt.show(block=False)

plt.figure(3)
r, r_hist, grad_hist, iter_hist = gradient_descent_harmonic(36.0, 0.74, 1.0, 0.05)
plt.plot(r_hist, grad_hist)
plt.xlabel("Bond Length")
plt.ylabel("Gradient")
plt.title("Gradient Descent Optimization")
plt.show(block=False)


plt.figure(4)
plt.plot(iter_hist, r_hist)
plt.xlabel("Iteration")
plt.ylabel("Bond Length")
plt.title("Bond Length Convergence")
plt.show(block=False)

# Exercise 2

def step_size_gradient_descent_harmonic(k, r_0, x0, lr, max_iter=50):
    """
    Perform gradient descent to minimize a harmonic potential energy function.

    Args:
        k (float): Bond force constant.
        r_0 (float): Equilibrium bond length.
        x0 (float): The initial guess for the bond length.
        lr (float): The learning rate.
        max_iter (int): The maximum number of iterations.

    Returns:
        float: The optimized bond length.
    """
    r_val = x0
    r_history = []
    grad_history = []
    iteration = []
    for i in range(max_iter):
        grad = k * (r_val - r_0)
        if np.abs(grad).any() < 0.001:
            break
        r_val = r_val - lr * grad
        r_history.append(r_val)
        grad_history.append(grad)
        iteration.append(i + 1)
        print(f"At iteration {i + 1}, position: {r_val} and gradient: {grad}")
    return r_val, r_history, grad_history, iteration

plt.figure(5)
r, r_hist, grad_hist, iter_hist = step_size_gradient_descent_harmonic(36.0, 0.74, 1.0, 0.01)
plt.plot(r_hist, grad_hist)
plt.xlabel("Bond Length")
plt.ylabel("Gradient")
plt.title("Gradient Descent Optimization")
plt.show(block=False)

plt.figure(6)
plt.plot(iter_hist, r_hist)
plt.xlabel("Iteration")
plt.ylabel("Bond Length")
plt.title("Bond Length Convergence")
plt.show(block=False)

plt.figure(7)
r, r_hist, grad_hist, iter_hist = step_size_gradient_descent_harmonic(36.0, 0.74, 1.0, 0.001)
plt.plot(r_hist, grad_hist)
plt.xlabel("Bond Length")
plt.ylabel("Gradient")
plt.title("Gradient Descent Optimization")
plt.show(block=False)


plt.figure(8)
plt.plot(iter_hist, r_hist)
plt.xlabel("Iteration")
plt.ylabel("Bond Length")
plt.title("Bond Length Convergence")
plt.show(block=False)

plt.figure(9)
r, r_hist, grad_hist, iter_hist = step_size_gradient_descent_harmonic(36.0, 0.74, 1.0, 0.1)
plt.plot(r_hist, grad_hist)
plt.xlabel("Bond Length")
plt.ylabel("Gradient")
plt.title("Gradient Descent Optimization")
plt.show(block=False)


plt.figure(10)
plt.plot(iter_hist, r_hist)
plt.xlabel("Iteration")
plt.ylabel("Bond Length")
plt.title("Bond Length Convergence")
plt.show()