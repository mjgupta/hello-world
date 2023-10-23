import matplotlib.pyplot as plt
import numpy as np

# Data
values = [47.09, 44.13, 57.8, 22.04, 19.75, 21.38]

# Define colors for the bars
colors = ['blue', 'red', 'green', 'blue', 'red', 'green']

# Create an array of indices for the x-axis
x = np.arange(len(values))

# Create a figure and axis
fig, ax = plt.subplots()

# Create the bar chart with the specified colors
bars = ax.bar(x, values, color=colors, width=0.7)

# Add a gap between the 3rd and 4th bar
ax.bar(3, 0, color='white', width=0.7)
for bar, value in zip(bars, values):
    ax.annotate(f'{value:.2f}', (bar.get_x() + bar.get_width() / 2, bar.get_height()), ha='center', va='bottom')

legend_elements = [plt.Line2D([0], [0], marker='s', color='w', label='R', markerfacecolor='red', markersize=10),
                  plt.Line2D([0], [0], marker='s', color='w', label='G', markerfacecolor='green', markersize=10),
                  plt.Line2D([0], [0], marker='s', color='w', label='B', markerfacecolor='blue', markersize=10)]
legend_labels = ['R', 'G', 'B']

ax.legend(handles=legend_elements, labels=legend_labels, loc='upper right')


# Set labels and title
ax.set_xlabel('Size')
ax.set_ylabel('CPU')
ax.set_title('Bar Chart')
ax.set_xticks([1.5, 4.5])
ax.set_xticklabels(['Small', 'Big'])

# Show the plot
plt.show()
