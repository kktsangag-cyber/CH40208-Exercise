import numpy as np

N = 500000 # Generate 500000 pairs of random numbers
M = 100
pi_estimates = []

import matplotlib.pyplot as plt

def plot_random_points(points):
    # Set up the plot with circle
    plt.axes()
    circle = plt.Circle((0,0), radius=1.0, fc='white', ec="green")
    plt.gca().add_patch(circle)
    plt.axis('scaled')
    plt.xlim(-1.0, 1.0)
    plt.ylim(-1.0, 1.0)
    plt.xlabel(r"$x$")
    plt.ylabel(r"$y$")

    # plot the points, using different colours depending on whether they
    # are inside or outside the circle
    points = np.random.uniform(low=-1, high=1, size=(N,2))
    dist_sq = points[:,0]**2 + points[:,1]**2
    inside = dist_sq < 1.0
    plt.scatter(points[inside, 0], points[inside, 1], color='red', s=0.1, alpha=0.3)
    plt.scatter(points[~inside, 0], points[~inside, 1], color='blue', s=0.1, alpha=0.3)

    plt.show()

def plot_times(times):
    for _ in range(times):
        points = np.random.uniform(low=-1, high=1, size=(N,2))
        plot_random_points(points)
        in_circle = np.sum(points[:,0]**2 + points[:,1]**2 < 1.0)
        pi_estimates.append(4 * in_circle / N)
    return pi_estimates

plot_times(M)
print(f"Mean estimated value of pi: {np.mean(pi_estimates)}")
print(f"Standard deviation of estimated values: {np.std(pi_estimates)}")
