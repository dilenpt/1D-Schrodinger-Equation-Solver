import numpy as np

def gaussian_wave_packet(x, x0, sigma, k0):
    psi = np.exp(-((x - x0) ** 2) / (2 * sigma ** 2)) * np.exp(1j * k0 * x)
    return psi

def normalize(psi, dx):
    norm = np.sqrt(np.sum(np.abs(psi) ** 2) * dx)
    return psi / norm