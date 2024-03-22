import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# file names

# 'efficiency_dome0_S08' 'efficiency_dome2_S08' 'efficiency_dome5_S08' 'efficiency_dome10_S08'

file_name = 'efficiency_dome2_S08'
col_names = ['Particle_Radius', 'Dome_Size', 'Efficiency', 'Efficiency_STDEV']
file = pd.read_csv(f'{file_name}.txt', sep='\t', header=None, names=col_names)


box_plot_data = []
for row in file.iterrows():
    data = np.random.normal(row[1]['Efficiency'], row[1]['Efficiency_STDEV'], size=100)
    data = data[data > 0]

    box_plot_data.append(data)


plt.boxplot(box_plot_data, showfliers=False)
plt.xlabel('Particle Radius (nm)')
plt.ylabel('Efficiency (%)')
plt.title(file_name)
x_label = list(file['Particle_Radius'])
x_ticks = list(range(1, len(x_label)+1))
plt.autoscale(enable=True, axis='y')

plt.xticks(ticks=x_ticks, labels=x_label)
plt.show()


