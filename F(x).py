import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import genextreme as gev

# Read dataset from the text file
file_path = 'E:\DATA.txt'  # Replace with your file path
with open(file_path, 'r') as file:
    dataset = [float(line.strip()) for line in file.readlines()]

# Divide dataset into three sections
section_size = len(dataset) // 3  # Calculate size of each section
section1 = dataset[:section_size]  # First section
section2 = dataset[section_size:2 * section_size]  # Second section
section3 = dataset[2 * section_size:]  # Third section

top_values = []  # Initialize an empty list to store top values

# Loop to get top 3 values from each section and populate top_values list
for section in [section1, section2, section3]:
    top_values.extend(sorted(section)[-3:])  # Add top 3 values from each section to top_values

# Calculate the GEV parameters for the top values
shape_param, loc_param, scale_param = gev.fit(top_values)

# Generate values for CDF plot
x = np.sort(top_values)  # Sort the top values
cdf_values = gev.cdf(x, shape_param, loc_param, scale_param)  # Calculate CDF values using GEV parameters

# Plot CDF
plt.figure(figsize=(6, 4))  # Set figure size
plt.plot(cdf_values, x, marker='o', linestyle='-')  # Plot CDF values against x values
plt.xlabel('F(x)')  # Set x-axis label
plt.ylabel('X')  # Set y-axis label
plt.title('Cumulative Distribution Function (CDF) for Top 3 Values from Each Section')  # Set plot title
plt.grid(True)  # Show grid

# Save output to a file named output.txt
output_file = "output.txt"
with open(output_file, 'w') as file:
    file.write(f"Shape parameter: {shape_param}\n")
    file.write(f"Location parameter: {loc_param}\n")
    file.write(f"Scale parameter: {scale_param}\n")
    file.write("\nCDF values vs. X values:\n")
    file.write("CDF values, X values\n")
    for i in range(len(cdf_values)):
        file.write(f"{cdf_values[i]}, {x[i]}\n")

# Display the plot
plt.savefig('CDF_Plot.png')
plt.show()
print()