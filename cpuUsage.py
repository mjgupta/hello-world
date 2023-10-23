import matplotlib.pyplot as plt
import numpy as np

# Data
groups = ['Group 1', 'Group 2']
labels = ['Bar 1', 'Bar 2', 'Bar 3']
values = [[47.09, 44.13, 57.8], [22.04, 19.75, 21.38]]

# Set the bar colors
colors = ['lightblue', 'lightcoral', 'lightgreen']

# Number of bars
num_bars = len(labels)
bar_width = 0.35
index = np.arange(num_bars)

# Create the grouped bar plot
for i in range(len(groups)):
    plt.bar(index + i * bar_width, values[i], bar_width, label=groups[i], color=colors)

# Set the x-axis labels
plt.xlabel('Bars')
plt.xticks(index + bar_width, labels)

# Set the y-axis label
plt.ylabel('Values')

# Add a legend
plt.legend()

# Show the plot
plt.show()
