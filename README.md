# 1D Time-Dependent Schrödinger Equation Solver

A Python-based simulator for the **1D time-dependent Schrödinger equation**, designed to model how a quantum wave packet evolves over time in different potentials.

This project uses the **Crank–Nicolson method** for numerically stable time evolution and includes both static plots and animations to visualize the wavefunction.

---

## Overview

This solver models a **Gaussian wave packet** moving through one-dimensional space under several possible potentials, including:

- free space
- a finite barrier
- a step potential
- a harmonic oscillator potential

It is useful for exploring key quantum mechanics ideas such as:

- wave packet propagation
- dispersion
- reflection
- tunneling
- probability conservation

---

## Equation Solved

The simulation evolves the wavefunction $\psi(x,t)$ using the **time-dependent Schrödinger equation**:

$$
i\hbar \frac{\partial \psi(x,t)}{\partial t}=\left[-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}+V(x)\right]\psi(x,t)
$$

where:

- $\psi(x,t)$ is the wavefunction
- $\hbar$ is the reduced Planck constant
- $m$ is the particle mass
- $V(x)$ is the potential energy function
- the operator in brackets is the **Hamiltonian**

---

## Features

- Simulates a **Gaussian wave packet**
- Supports multiple potential types
- Uses the **Crank–Nicolson** scheme for time stepping
- Tracks:
  - probability density $|\psi|^2$
  - real part of $\psi$
  - imaginary part of $\psi$
  - total probability over time
- Generates:
  - static plots
  - animated wavefunction evolution

---

## Project Structure

### `main.py`
Main entry point for the simulation. Defines parameters, selects the scenario, runs the solver, and calls the visualization tools.

### `solver.py`
Contains the `SchrodingerSolver1D` class. Builds the Hamiltonian and performs time evolution using the Crank–Nicolson method.

### `wavepacket.py`
Creates and normalizes the initial Gaussian wave packet.

### `potentials.py`
Defines the available potential functions:

- `free_potential`
- `barrier_potential`
- `step_potential`
- `harmonic_potential`

### `visualize.py`
Handles plotting and animation of the simulation results.

---

## Requirements

Install the required packages with:

```bash
pip install numpy scipy matplotlib
```

---

## How to Run

Run the simulation with:

```bash
python main.py
```

---

## Default Parameters

The default settings in `main.py` are:

```python
hbar = 1.0
m = 1.0

x_min, x_max = -200.0, 200.0
Nx = 1200

dt = 0.05
Nt = 1200

scenario = "barrier"
x0 = -100.0
sigma = 10.0
k0 = 2.0
```

These values define:

- the physical constants
- the 1D spatial domain
- the number of grid points
- the time step and number of time steps
- the potential scenario
- the initial wave packet position, width, and momentum

---

## Available Scenarios

Choose a scenario in `main.py` by setting:

```python
scenario = "free"
```

Other available options are:

```python
scenario = "barrier"
scenario = "step"
scenario = "harmonic"
```

### Scenario Meanings

- **free**  
  The wave packet travels in empty space and spreads out over time.

- **barrier**  
  The wave packet encounters a finite potential barrier and may partially reflect or tunnel through it.

- **step**  
  The wave packet encounters a sudden change in potential energy.

- **harmonic**  
  The wave packet evolves in a harmonic oscillator potential.

---

## Numerical Method

The Hamiltonian is discretized as:

$$
\hat{H}=-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}+V(x)
$$


The second derivative is approximated using finite differences:

$$
\frac{\partial^2 \psi}{\partial x^2}
\approx
\frac{\psi_{j+1} - 2\psi_j + \psi_{j-1}}{dx^2}
$$

Time evolution is performed using the **Crank–Nicolson scheme**:

$$
\left(I + \frac{i\,dt}{2\hbar}H\right)\psi^{n+1}=\left(I - \frac{i\,dt}{2\hbar}H\right)\psi^n
$$

This method is widely used because it is numerically stable and helps preserve total probability.

---

## Output

The solver returns:

- `psi_final`
- `densities`
- `real_parts`
- `imag_parts`
- `norms`

The visualizations include:

- final probability density
- total probability versus time
- animation of the wave packet evolution

For the barrier case, the simulation can also report:

- reflected probability
- probability inside the barrier region
- transmitted probability

---

## Physics Concepts Demonstrated

This project helps illustrate:

- quantum wave propagation
- wave packet spreading
- reflection from a barrier
- quantum tunneling
- step-potential behavior
- harmonic oscillator motion
- conservation of probability

---

## Possible Extensions

Some ideas for expanding the project:

- multiple barriers
- square well potentials
- absorbing boundary conditions
- time-dependent potentials
- GIF or video export
- comparisons between different wave packet parameters

---

## Notes

- This solver is **one-dimensional**, so motion only occurs along the x-axis.
- The current implementation uses a **time-independent potential** $V(x)$, even though the wavefunction itself evolves in time.
- The plotted barrier represents a **potential energy barrier**, not a solid classical wall.

---

## Educational Purpose

This project is intended for learning and exploration in:

- quantum mechanics
- numerical methods
- computational physics

---

## License

This project is provided for educational and research-learning purposes.
