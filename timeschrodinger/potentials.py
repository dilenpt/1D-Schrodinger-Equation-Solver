import numpy as np

def free_potential(x):
    return np.zeros_like(x)

def barrier_potential(x, left=20.0, right=40.0, height=2.0):
    V = np.zeros_like(x)
    V[(x >= left) & (x <= right)] = height
    return V

def step_potential(x, step_location=0.0, height=2.0):
    V = np.zeros_like(x)
    V[x >= step_location] = height
    return V

def harmonic_potential(x, m=1.0, omega=0.05):
    return 0.5 * m * omega**2 * x**2