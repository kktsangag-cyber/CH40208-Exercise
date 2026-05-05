import numpy as np
import matplotlib.pyplot as plt

# Part a

def lennard_jones(r, A=1e5, B=40):
    """
    Compute the Lennard-Jones potential energy.

    Args:
        r (float): The distance between the particles.
        A (float): The depth of the potential well.
        B (float): The distance at which the potential is zero.

    Returns:
        float: The Lennard-Jones potential energy.
    """
    potential_energy = A / r**12 - B / r**6
    return potential_energy

if __name__ == "__main__":
    r_dot = np.linspace(3.6, 8.0, 500)
    potential_energy = lennard_jones(r_dot)
    plt.figure(1)
    plt.plot(r_dot, potential_energy, label='Lennard-Jones Potential')
    plt.xlabel('Distance (r)')
    plt.ylabel('Potential Energy')
    plt.title('Lennard-Jones Potential Energy')
    plt.axhline(0, color='gray', linestyle='--', label='Zero Potential')
    plt.legend()
    plt.show(block=False)

# Part b

def lennard_jones_first_derivative(r, A=1e5, B=40):
    """
    Compute the first derivative of the Lennard-Jones potential energy.

    Args:
        r (float): The distance between the particles.
        A (float): The depth of the potential well.
        B (float): The distance at which the potential is zero.

    Returns:
        float: The first derivative of the Lennard-Jones potential energy.
    """
    return -12 * A / r**13 + 6 * B / r**7

def lennard_jones_gradient(r, ran, lr, t, A=1e5, B=40):
    """
    Compute the gradient of the Lennard-Jones potential energy.

    Args:
        r (float): The distance between the particles.
        ran (int): The number of iterations.
        lr (float): The learning rate.
        t (float): Tolerance.
        A (float): The depth of the potential well.
        B (float): The distance at which the potential is zero.

    Returns:
        float: The gradient of the Lennard-Jones potential energy.
    """
    r_hist = []
    grad_hist = []
    iteration = []
    for i in range(ran):
        grad = lennard_jones_first_derivative(r, A, B)
        if np.abs(grad).any() < t:
            break
        r = r - lr * grad
        r_hist.append(r)
        grad_hist.append(grad)
        iteration.append(i + 1)
    print(f"At final iteration {i + 1}, position: {r} and gradient: {grad}")
    return r, r_hist, grad_hist, iteration

if __name__ == "__main__":
    r_start_b_d = 5.0
    r_b, r_hist_gradient_b, grad_hist_gradient_b, iter_hist_gradient_b = lennard_jones_gradient(r_start_b_d, ran=50, lr=100, t=0.001)
    plt.figure(2)
    plt.plot(iter_hist_gradient_b, r_hist_gradient_b, 'o-', label='Lennard-Jones Gradient Descent')
    plt.xlabel('Iteration')
    plt.ylabel('Distance (r)')
    plt.title('Lennard-Jones Gradient Descent')
    plt.legend()
    plt.show(block=False)

# Part c

if __name__ == "__main__":
    r_start_c_e = [3.2, 4.4, 6.0]
    r_c1, r_hist_gradient_c1, grad_hist_gradient_c1, iter_hist_gradient_c1 = lennard_jones_gradient(r_start_c_e[0], ran=500, lr=10, t=0.0005)
    r_c2, r_hist_gradient_c2, grad_hist_gradient_c2, iter_hist_gradient_c2 = lennard_jones_gradient(r_start_c_e[1], ran=500, lr=10, t=0.0005)
    r_c3, r_hist_gradient_c3, grad_hist_gradient_c3, iter_hist_gradient_c3 = lennard_jones_gradient(r_start_c_e[2], ran=500, lr=10, t=0.0005)

    results = [
        ("3.2", grad_hist_gradient_c1, r_hist_gradient_c1),
        ("4.4", grad_hist_gradient_c2, r_hist_gradient_c2),
        ("6.0", grad_hist_gradient_c3, r_hist_gradient_c3)
    ]

    for label, g_hist, r_hist in results:
        converged = False
        for x in range(50):
            if np.abs(g_hist[x]) < 0.001:
                print(f"Convergence achieved at iteration {x + 1} for initial guess {label} with distance {r_hist[x]:.4f}")
                converged = True
                break

        if not converged:
            print(f"No convergence achieved at first {x + 1} iterations for initial guess {label}")

    plt.figure(3)
    plt.plot(iter_hist_gradient_c1, r_hist_gradient_c1, 'r-', label='Lennard-Jones Gradient Descent (initial guess = 3.2)')
    plt.plot(iter_hist_gradient_c2, r_hist_gradient_c2, 'g-', label='Lennard-Jones Gradient Descent (initial guess = 4.4)')
    plt.plot(iter_hist_gradient_c3, r_hist_gradient_c3, 'b-', label='Lennard-Jones Gradient Descent (initial guess = 6.0)')
    plt.xlabel('Iteration')
    plt.ylabel('Distance (r)')
    plt.title('Lennard-Jones Gradient Descent')
    plt.legend()
    plt.show(block=False)

# Part d

def lennard_jones_second_derivative(r, A, B):
    """
    Compute the second derivative of the Lennard-Jones potential energy.

    Args:
        r (float): The distance between the particles.
        A (float): The depth of the potential well.
        B (float): The distance at which the potential is zero.

    Returns:
        float: The second derivative of the Lennard-Jones potential energy.
    """
    return 156 * A / r**14 - 42 * B / r**8

def lennard_jones_newton_raphson(r, A=1e5, B=40):
    """
    Compute the root of the Lennard-Jones potential energy using the Newton-Raphson method.

    Args:
        r (float): The initial guess for the distance between the particles.
        A (float): The depth of the potential well.
        B (float): The distance at which the potential is zero.

    Returns:
        float: The root of the Lennard-Jones potential energy.
    """
    r_hist = []
    grad_hist = []
    iteration = []
    for i in range(50):
        f = lennard_jones_first_derivative(r, A, B)
        f_prime = lennard_jones_second_derivative(r, A, B)
        if np.abs(f).any() < 0.001:
            break
        r = r - f / f_prime
        r_hist.append(r)
        grad_hist.append(f)
        iteration.append(i + 1)
    print(f"At final iteration {i + 1}, position: {r} and gradient: {f}")
    return r, r_hist, grad_hist, iteration

if __name__ == "__main__":
    r_d, r_hist_gradient_d, grad_hist_gradient_d, iter_hist_gradient_d = lennard_jones_newton_raphson(r_start_b_d, A=1e5, B=40)
    plt.figure(4)
    plt.plot(iter_hist_gradient_d, r_hist_gradient_d, 'o-', label='Lennard-Jones Newton-Raphson')
    plt.plot(iter_hist_gradient_b, r_hist_gradient_b, 'x-', label='Lennard-Jones Gradient Descent')
    plt.xlabel('Iteration')
    plt.ylabel('Distance (r)')
    plt.title('Lennard-Jones Optimization')
    plt.legend()
    plt.show(block=False)

# Part e

if __name__ == "__main__":
    plt.figure(5)
    r_e1, r_hist_gradient_e1, grad_hist_gradient_e1, iter_hist_gradient_e1 = lennard_jones_newton_raphson(r_start_c_e[0])
    r_e2, r_hist_gradient_e2, grad_hist_gradient_e2, iter_hist_gradient_e2 = lennard_jones_newton_raphson(r_start_c_e[1])
    r_e3, r_hist_gradient_e3, grad_hist_gradient_e3, iter_hist_gradient_e3 = lennard_jones_newton_raphson(r_start_c_e[2])
    plt.plot(iter_hist_gradient_e1, r_hist_gradient_e1, 'r', label='Lennard-Jones Newton-Raphson (initial guess = 3.2)')
    plt.plot(iter_hist_gradient_e2, r_hist_gradient_e2, 'g', label='Lennard-Jones Newton-Raphson (initial guess = 4.4)')
    plt.plot(iter_hist_gradient_e3, r_hist_gradient_e3, 'b', label='Lennard-Jones Newton-Raphson (initial guess = 6.0)')
    plt.xlabel('Iteration')
    plt.ylabel('Distance (r)')
    plt.title('Lennard-Jones Newton-Raphson')
    plt.legend()
    plt.show()