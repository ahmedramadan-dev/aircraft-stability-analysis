import numpy as np
import matplotlib.pyplot as plt

# Constants
CM_0 = 0.02
CM_ALPHA_REF = -0.05
CM_DE = -0.80
CL_ALPHA = 4.50
REF_CG = 0.30

# Variables to test
ELEVATOR_ANGLES = [0, 5, -5]
CG_LOCATIONS = [0.20, 0.30, 0.40, 0.50]

# Angle of attack range
alpha_deg = np.linspace(-10, 10, 100)
alpha_rad = np.deg2rad(alpha_deg)

# Plotting functions
def plot_trim_point(alpha_deg, Cm):
    idx = np.argmin(np.abs(Cm))
    plt.scatter(alpha_deg[idx], 0)

def format_graph(title):
    plt.axhline(0, color='black', linewidth=0.8)
    plt.xlabel("Alpha")
    plt.ylabel("Cm")
    plt.title(title)
    plt.legend()
    plt.grid()

# ── Graph 1: Elevator ──────────────────────────────────────────────────────────
plt.figure()

for de in ELEVATOR_ANGLES:
    de_rad = np.deg2rad(de)
    Cm = CM_0 + CM_ALPHA_REF * alpha_rad + CM_DE * de_rad
    plt.plot(alpha_deg, Cm, label=f"de={de}")
    
    plot_trim_point(alpha_deg, Cm)

format_graph("Cm vs Alpha (Elevator)")

# ── Graph 2: CG Sweep ──────────────────────────────────────────────────────────
plt.figure()

for cg in CG_LOCATIONS:
    Cm_alpha = CM_ALPHA_REF - CL_ALPHA * (cg - REF_CG)
    Cm = CM_0 + Cm_alpha * alpha_rad
    plt.plot(alpha_deg, Cm, label=f"CG={cg:.2f}")
    
    plot_trim_point(alpha_deg, Cm)

format_graph("Cm vs Alpha (CG)")

plt.show()