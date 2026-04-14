import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def plot_static_results(x, densities, norms, dt, V=None, title="TDSE Results"):
    fig, axes = plt.subplots(2, 1, figsize=(10, 8))

    axes[0].plot(x, densities[-1], label=r"$|\psi(x,t)|^2$")

    if V is not None and np.max(V) > 0:
        V_scaled = V / np.max(V) * np.max(densities[-1]) * 0.8
        axes[0].plot(x, V_scaled, "--", label="Scaled Potential")

    axes[0].set_title(f"{title} - Final Probability Density")
    axes[0].set_xlabel("x")
    axes[0].set_ylabel(r"$|\psi|^2$")
    axes[0].legend()
    axes[0].grid(True)

    time_array = np.arange(len(norms)) * dt
    axes[1].plot(time_array, norms)
    axes[1].set_title("Total Probability vs Time")
    axes[1].set_xlabel("Time")
    axes[1].set_ylabel("Total Probability")
    axes[1].grid(True)

    plt.tight_layout()
    plt.show()

def animate_results(x, densities, real_parts, imag_parts, dt, V=None, x_min=None, x_max=None, title="TDSE Animation"):
    fig, ax = plt.subplots(figsize=(10, 5))

    line_density, = ax.plot([], [], lw=2, label=r"$|\psi(x,t)|^2$")
    line_real, = ax.plot([], [], lw=1, alpha=0.7, label=r"Re($\psi$)")
    line_imag, = ax.plot([], [], lw=1, alpha=0.7, label=r"Im($\psi$)")

    if V is not None and np.max(V) > 0:
        V_scaled = V / np.max(V) * np.max(densities) * 0.8
        ax.plot(x, V_scaled, "--", label="Scaled Potential")

    if x_min is None:
        x_min = x[0]
    if x_max is None:
        x_max = x[-1]

    ax.set_xlim(x_min, x_max)
    ax.set_ylim(
        min(np.min(real_parts), np.min(imag_parts), 0) * 1.2,
        max(np.max(densities), np.max(real_parts), np.max(imag_parts)) * 1.2
    )
    ax.set_xlabel("x")
    ax.set_ylabel("Amplitude / Density")
    ax.set_title(title)
    ax.legend()
    ax.grid(True)

    time_text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    def init():
        line_density.set_data([], [])
        line_real.set_data([], [])
        line_imag.set_data([], [])
        time_text.set_text("")
        return line_density, line_real, line_imag, time_text

    def update(frame):
        line_density.set_data(x, densities[frame])
        line_real.set_data(x, real_parts[frame])
        line_imag.set_data(x, imag_parts[frame])
        time_text.set_text(f"t = {frame * dt:.2f}")
        return line_density, line_real, line_imag, time_text

    ani = FuncAnimation(
        fig,
        update,
        frames=range(0, len(densities), 3),
        init_func=init,
        blit=True,
        interval=30
    )

    plt.show()
    return ani