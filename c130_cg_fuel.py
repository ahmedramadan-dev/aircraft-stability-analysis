import numpy as np
import matplotlib.pyplot as plt

# 1) Compute CG During Fuel Burn
mass_structure = 8000
mass_payload = 2000
fuel = np.linspace(3000, 0, 50)

position_structure = 0.30
position_payload = 0.35
position_fuel = 0.20

cg = []
for mass_fuel in fuel:
    total_mass = mass_structure + mass_payload + mass_fuel
    xcg = (
        mass_structure * position_structure +
        mass_payload * position_payload +
        mass_fuel * position_fuel
    ) / total_mass
    cg.append(xcg)

# 2) Update Stability
Cm0 = 0.05
Cma = -0.8
Cm = []
for xcg in cg:
    cm_value = Cm0 + Cma * (xcg - 0.25)
    Cm.append(cm_value)

# 3) Detect Stability Limit
for i in range(len(Cm)):
    if Cm[i] == 0:
        print("Neutral Stability at CG =", cg[i])
    elif Cm[i] < 0:
        print("Stable at CG =", cg[i])
    else:
        print("Unstable at CG =", cg[i])

# 4) Determine CG Range
nose_limit = min(cg)
tail_limit = max(cg)
print("CG Limit = [", nose_limit, "to", tail_limit, "]")

# 5) Elevator Trim Compensation
Cmde = -1.1
delta_e = []
for i in range(len(cg)):
    de = -(Cm0 + Cma * (cg[i] - 0.25)) / Cmde
    delta_e.append(de)

# 6) Visualization
plt.figure(figsize=(12, 4))

# Graph 1: CG Position
plt.subplot(1, 3, 1)
plt.plot(fuel, cg)
plt.xlabel("Fuel Mass")
plt.ylabel("CG Position")
plt.title("CG Position")
plt.grid(True)

# Graph 2: Stability Coefficient (Cm)
plt.subplot(1, 3, 2)
plt.plot(fuel, Cm)
plt.xlabel("Fuel Mass")
plt.ylabel("Cm")
plt.title("Cm vs Fuel")
plt.grid(True)

# Graph 3: Elevator Deflection
plt.subplot(1, 3, 3)
plt.plot(fuel, delta_e)
plt.xlabel("Fuel Mass")
plt.ylabel("Elevator Deflection")
plt.title("Elevator Trim")
plt.grid(True)

plt.tight_layout()
plt.show()