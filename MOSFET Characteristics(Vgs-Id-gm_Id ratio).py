import numpy as np
import matplotlib.pyplot as plt

# Constants
mu_n = 0.01  # Electron mobility in m^2/Vs
C_ox = 5e-9  # Oxide capacitance per unit area in F/m^2
W = 2e-5  # Width of the MOSFET channel in meters
L = 0.15e-6  # Length of the MOSFET channel in meters
V_th = 1  # Threshold voltage in volts

# Generate a range of Vgs values
Vgs_values = np.linspace(0, 5, 100)

# Calculate Id and gm for each Vgs
Id_values = np.where(Vgs_values < V_th, 0, 0.5 * mu_n * C_ox * (W / L) * (Vgs_values - V_th)**2)
gm_values = mu_n * C_ox * (W / L) * (Vgs_values - V_th)

# Exclude points where Id is zero
non_zero_indices = np.nonzero(Id_values)
Vgs_non_zero = Vgs_values[non_zero_indices]
gm_id_ratio_non_zero = gm_values[non_zero_indices] / Id_values[non_zero_indices]

# Plotting
plt.figure(figsize=(12, 6))

# Plot Id vs. Vgs
plt.subplot(1, 2, 1)
plt.plot(Vgs_values, Id_values, label='$I_D$', color='blue', linewidth=2, linestyle='-', marker='o', markersize=5, markerfacecolor='red')
plt.title('MOSFET Characteristics: $I_D$ vs. $V_{gs}$')
plt.xlabel('$V_{gs}$ (V)')
plt.ylabel('$I_D$ (A)')
plt.grid(True)
plt.legend()

# Scatter plot of gm/Id vs. Vgs (excluding points where Id is zero)
plt.subplot(1, 2, 2)
plt.scatter(Vgs_non_zero, gm_id_ratio_non_zero, color='purple', label='$g_m/I_D$', s=30, linestyle='-', marker='o', facecolors='yellow')
plt.title('MOSFET Characteristics: $g_m/I_D$ vs. $V_{gs}$')
plt.xlabel('$V_{gs}$ (V)')
plt.ylabel('$g_m/I_D$ (S/A)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
