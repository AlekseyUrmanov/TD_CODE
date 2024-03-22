import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import Tkinter as tk



# Create sample data

plt.rcParams['toolbar'] = 'NONE'

x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot
plt.plot(x, y)

# Remove x-axis ticks and labels
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)

# Remove y-axis ticks and labels
plt.tick_params(axis='y', which='both', left=False, right=False, labelleft=False)

# Disable Matplotlib toolbar

# Show the plot
plt.show()
