import numpy as np

from wavepacket import gaussian_wave_packet, normalize
from potentials import free_potential, barrier_potential, step_potential, harmonic_potential
from solver import SchrodingerSolver1D
from visualize import plot_static_results, animate_results


hbar = 1.0
m = 1.0

x_min, x_max = -200.0, 200.0
Nx = 1200
x = np.linspace(x_min, x_max, Nx)
dx = x[1] - x[0]

dt = 0.05
Nt = 2400

scenario = "barrier"   # choose: free, barrier, step, harmonic

# Wave packet parameters
x0 = -100.0
sigma = 10.0
k0 = 2.0


psi0 = gaussian_wave_packet(x, x0, sigma, k0)
psi0 = normalize(psi0, dx)


if scenario == "free":
    V = free_potential(x)
elif scenario == "barrier":
    barrier_left = 20.0
    barrier_right = 40.0
    V0 = 2.0
    V = barrier_potential(x, left=barrier_left, right=barrier_right, height=V0)
elif scenario == "step":
    V = step_potential(x, step_location=20.0, height=2.0)
elif scenario == "harmonic":
    V = harmonic_potential(x, m=m, omega=0.05)
else:
    raise ValueError("Unknown scenario")


solver = SchrodingerSolver1D(x=x, dt=dt, hbar=hbar, m=m, V=V)
results = solver.run(psi0, Nt)

psi_final = results["psi_final"]
densities = results["densities"]
real_parts = results["real_parts"]
imag_parts = results["imag_parts"]
norms = results["norms"]

print(f"Initial total probability: {norms[0]:.6f}")
print(f"Final total probability:   {norms[-1]:.6f}")

# Barrier analysis
if scenario == "barrier":
    reflected = np.sum(densities[-1][x < barrier_left]) * dx
    transmitted = np.sum(densities[-1][x > barrier_right]) * dx
    middle = np.sum(densities[-1][(x >= barrier_left) & (x <= barrier_right)]) * dx

    print(f"Reflected probability:   {reflected:.6f}")
    print(f"Barrier-region prob.:    {middle:.6f}")
    print(f"Transmitted probability: {transmitted:.6f}")
    print(f"Total check:             {reflected + middle + transmitted:.6f}")


plot_static_results(x, densities, norms, dt, V=V, title=f"Scenario: {scenario}")

ani = animate_results(
    x,
    densities,
    real_parts,
    imag_parts,
    dt,
    V=V,
    x_min=x_min,
    x_max=x_max,
    title=f"Time-Dependent Schrödinger Equation: {scenario}"
)

