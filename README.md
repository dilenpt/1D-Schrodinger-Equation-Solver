# 1D Time-Dependent Schrödinger Equation Solver

This project is a **1D time-dependent Schrödinger equation solver** written in Python. It simulates how a quantum wave packet evolves in time under different potentials, such as free space, a barrier, a step potential, or a harmonic potential.

It uses the **Crank–Nicolson method** for stable time evolution and visualizes the wavefunction with static plots and animation.

## Equation Solved

The solver evolves the wavefunction \(\psi(x,t)\) using the **time-dependent Schrödinger equation**:

\[
i\hbar \frac{\partial \psi(x,t)}{\partial t}
=
\left[
-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}
+
V(x)
\right]\psi(x,t)
\]

where:

- \(\psi(x,t)\) is the wavefunction
- \(\hbar\) is the reduced Planck constant
- \(m\) is the particle mass
- \(V(x)\) is the potential
- the bracketed operator is the **Hamiltonian**

## Features

- Simulates a **Gaussian wave packet**
- Supports multiple potentials:
  - free potential
  - barrier potential
  - step potential
  - harmonic potential
- Uses **Crank–Nicolson** time stepping
- Tracks:
  - probability density \(|\psi|^2\)
  - real part of \(\psi\)
  - imaginary part of \(\psi\)
  - total probability over time
- Produces:
  - static plots
  - animated wave evolution

## Project Structure

- `main.py`  
  Main entry point. Sets simulation parameters, chooses the scenario, runs the solver, and visualizes results.

- `solver.py`  
  Contains the `SchrodingerSolver1D` class. Builds the Hamiltonian and performs time stepping with Crank–Nicolson.

- `wavepacket.py`  
  Creates and normalizes the initial Gaussian wave packet.

- `potentials.py`  
  Defines the available potentials:
  - `free_potential`
  - `barrier_potential`
  - `step_potential`
  - `harmonic_potential`

- `visualize.py`  
  Creates static plots and animations for the simulation results.

## Requirements

Install the required Python packages:

```bash
pip install numpy scipy matplotlib
```

## How to Run

Run the main file:

```bash
python main.py
```

## Default Simulation Settings

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

These define:

- the physical constants
- the 1D spatial grid
- the time step and number of time steps
- the type of potential
- the initial wave packet position, width, and momentum

## Available Scenarios

In `main.py`, set:

```python
scenario = "free"
```

or

```python
scenario = "barrier"
```

or

```python
scenario = "step"
```

or

```python
scenario = "harmonic"
```

### Scenario Descriptions

- **free**  
  The wave packet moves in empty space and spreads out over time.

- **barrier**  
  The wave packet encounters a finite barrier and may reflect or tunnel through it.

- **step**  
  The wave packet encounters a sudden jump in potential.

- **harmonic**  
  The wave packet evolves inside a harmonic oscillator potential.

## Numerical Method

The Hamiltonian is discretized as:

\[
\hat H =
-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}
+
V(x)
\]

The second derivative is approximated with finite differences:

\[
\frac{\partial^2 \psi}{\partial x^2}
\approx
\frac{\psi_{j+1} - 2\psi_j + \psi_{j-1}}{dx^2}
\]

Time evolution uses the **Crank–Nicolson scheme**:

\[
\left(I + \frac{i\,dt}{2\hbar}H\right)\psi^{n+1}
=
\left(I - \frac{i\,dt}{2\hbar}H\right)\psi^n
\]

This method is stable and helps preserve total probability.

## Output

The solver returns:

- `psi_final`
- `densities`
- `real_parts`
- `imag_parts`
- `norms`

The visualization shows:

- final probability density
- total probability vs time
- animation of the wave evolution

For the barrier case, the code also reports:

- reflected probability
- barrier-region probability
- transmitted probability

## Example Concepts Demonstrated

This project can be used to study:

- wave packet propagation
- dispersion
- quantum reflection
- tunneling
- step-potential behavior
- harmonic oscillator motion
- probability conservation

## Customization Ideas

You can extend this project by adding:

- multiple barriers
- square wells
- absorbing boundaries
- time-dependent potentials
- saving animations to GIF or video
- comparisons between different initial conditions

## Notes

- The solver is **1D**, so motion only happens along the x-axis.
- The code currently uses a **time-independent potential** \(V(x)\), even though the wavefunction is evolved in time.
- The barrier shown in the plot is a **potential barrier**, not a solid classical wall.

## License

This project is for educational and research learning purposes.
