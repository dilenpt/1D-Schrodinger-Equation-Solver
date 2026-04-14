import numpy as np
from scipy.sparse import diags, identity
from scipy.sparse.linalg import splu

class SchrodingerSolver1D:
    def __init__(self, x, dt, hbar=1.0, m=1.0, V=None):
        self.x = x
        self.dt = dt
        self.hbar = hbar
        self.m = m
        self.Nx = len(x)
        self.dx = x[1] - x[0]

        if V is None:
            V = np.zeros_like(x)
        self.V = V

        self.H = self._build_hamiltonian()
        self.A, self.B = self._build_crank_nicolson_matrices()
        self.solver = splu(self.A)

    def _build_hamiltonian(self):
        main_diag = -2.0 * np.ones(self.Nx)
        off_diag = 1.0 * np.ones(self.Nx - 1)

        laplacian = diags(
            [off_diag, main_diag, off_diag],
            [-1, 0, 1],
            format="csc"
        ) / (self.dx ** 2)

        H = -(self.hbar ** 2 / (2.0 * self.m)) * laplacian + diags(self.V, 0, format="csc")
        return H

    def _build_crank_nicolson_matrices(self):
        I = identity(self.Nx, format="csc")
        A = (I + 1j * self.dt / (2.0 * self.hbar) * self.H).tocsc()
        B = (I - 1j * self.dt / (2.0 * self.hbar) * self.H).tocsc()
        return A, B

    def step(self, psi):
        rhs = self.B @ psi
        psi_next = self.solver.solve(rhs)
        return psi_next

    def run(self, psi0, Nt):
        psi = psi0.copy()

        densities = []
        real_parts = []
        imag_parts = []
        norms = []

        for _ in range(Nt):
            psi = self.step(psi)

            density = np.abs(psi) ** 2
            densities.append(density.copy())
            real_parts.append(np.real(psi).copy())
            imag_parts.append(np.imag(psi).copy())

            prob = np.sum(density) * self.dx
            norms.append(prob)

        return {
            "psi_final": psi,
            "densities": np.array(densities),
            "real_parts": np.array(real_parts),
            "imag_parts": np.array(imag_parts),
            "norms": np.array(norms),
        }