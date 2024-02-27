import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button
import numpy as np

# Declare animation as a global variable
animation = None

# Function to generate sinusoidal wave data
def generate_wave_data(frame, voltage_amplitude):
    frequency = 2  # Set the frequency of the sine wave
    voltage = voltage_amplitude * np.sin(2 * np.pi * frequency * frame)
    current = voltage / 1000  # Current (I) = Voltage (V) / Resistance (R)
    return voltage, current

# Function to update the plot data with a smaller, more sinusoidal sine wave
def update(frame, voltage_amplitude):
    # Generate new wave data
    voltage, current = generate_wave_data(frame, voltage_amplitude)

    # Update the data lists
    x_data.append(frame)
    y_voltage_data.append(voltage)
    y_current_data.append(current)

    # Limit the number of data points to keep the plot readable
    max_data_points = 50
    if len(x_data) > max_data_points:
        x_data.pop(0)
        y_voltage_data.pop(0)
        y_current_data.pop(0)

    # Clear the current plot and plot the updated data in separate subplots
    ax1.clear()
    ax1.plot(x_data, y_voltage_data, label='Voltage', color='blue', linewidth=2)
    ax1.set_title('Voltage Example', fontsize=14)
    ax1.set_xlabel('Time (s)', fontsize=12)
    ax1.set_ylabel('Voltage (V)', fontsize=12)
    ax1.legend()

    ax2.clear()
    ax2.plot(x_data, y_current_data, label='Current', linestyle='dashed', color='orange', linewidth=2)
    ax2.set_title('Current Example', fontsize=14)
    ax2.set_xlabel('Time (s)', fontsize=12)
    ax2.set_ylabel('Current (A)', fontsize=12)
    ax2.legend()

# Function to start the animation
def start_animation(event):
    global animation  # Declare animation as a global variable
    voltage_amplitude = voltage_slider.val
    if animation:
        animation.event_source.stop()  # Stop the previous animation
    animation = FuncAnimation(fig, update, frames=np.linspace(0, 2, 90), fargs=(voltage_amplitude,), interval=100, repeat=False)
    plt.show()  # Display the plot

# Create a figure and two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))

# Initialize x, voltage, and current values
x_data = []
y_voltage_data = []
y_current_data = []

# Set up sliders for interactive input
ax_slider = plt.axes([0.25, 0.02, 0.65, 0.03], facecolor='lightgoldenrodyellow')
voltage_slider = Slider(ax_slider, 'Voltage Amplitude', 1, 50, valinit=25)

# Set up the button to start the animation
ax_button = plt.axes([0.8, 0.1, 0.1, 0.05])
button = Button(ax_button, 'Start Animation')
button.on_clicked(start_animation)

# Set up the initial plot
update(0, voltage_slider.val)

# Customize plot layout
plt.tight_layout()

# Show the plot
plt.show()
