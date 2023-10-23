import matplotlib.pyplot as plt
import numpy as np

# Data
values = [47.09, 44.13, 57.8, 22.04, 19.75, 21.38]
labels = ['Bar 1', 'Bar 2', 'Bar 3']
group_labels = ['Group 1', 'Group 2']
bar_width = 0.35  # Width of each bar

# Create an array of indices for the x-axis
x = np.arange(len(labels))

# Split the values into two groups, each containing three bars
group1_values = values[:3]
group2_values = values[3:]

# Create subplots
fig, ax = plt.subplots()

# Plot the bars for each group
bar1 = ax.bar(x - bar_width/2, group1_values, bar_width, label=group_labels[0])
bar2 = ax.bar(x + bar_width/2, group2_values, bar_width, label=group_labels[1])

# Set labels and title
ax.set_xlabel('Bars')
ax.set_ylabel('Values')
ax.set_title('Grouped Bar Chart')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

# Show the plot
plt.show()
