import numpy as np
import matplotlib.pyplot as plt

# Constants
mu_n = 1000  # Electron mobility (cm^2/Vs)
C_ox = 1e-6  # Oxide capacitance per unit area (F/cm^2)
W = 10e-4    # Width of the transistor (cm)
L = 1e-4     # Length of the transistor (cm)
vth = 1      # Threshold voltage (V)
lambda_value = 0.1  # Channel length modulation parameter

# Function to calculate drain current
def id(vgs, vds):
    triode_region = vds < (vgs - vth)
    id_triode = mu_n * C_ox * W / L * ((vgs - vth) * vds - (vds ** 2) / 2) * triode_region
    id_saturation = mu_n * C_ox * W / L * ((vgs - vth) ** 2) / 2 * (~triode_region)
    return id_triode + id_saturation

# Function to find transition points
def transition_points(vgs_values, vds_values):
    transition_vds_values = []
    for vgs in vgs_values:
        for vds in vds_values:
            if vds >= vgs - vth:
                transition_vds_values.append(vds)
                break
    return transition_vds_values

# Vds range
vds_values = np.linspace(0, 10, 1000)

# Values of Vgs
vgs_values = np.linspace(1, 7, 7)

# Find transition points
transition_vds_values = transition_points(vgs_values, vds_values)

# Calculate drain current for each transition point
id_transition = [id(vgs, vds) for vgs, vds in zip(vgs_values, transition_vds_values)]

# Plot characteristics for each Vgs value
plt.figure(figsize=(10, 6))
for vgs in vgs_values:
    id_values = id(vgs, vds_values)
    plt.plot(vds_values, id_values, label=f'$V_{{gs}}$ = {vgs} V', linewidth=2)

# Plot the curve based on transition points
plt.plot(transition_vds_values, id_transition, color='red', linestyle='--', label='Triode to Saturation Curve')

# Plot settings
plt.xlabel('$V_{ds}$ (V)', fontsize=14)
plt.ylabel('$I_{ds}$ (A)', fontsize=14)
plt.title('MOSFET Output Characteristic', fontsize=16)
plt.grid(True)
plt.legend(fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.tight_layout()
plt.show()
