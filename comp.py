import pandas as pd
import matplotlib.pyplot as plt
import sys

# Check if the correct number of command line arguments are provided
if len(sys.argv) != 2:
    print("Usage: python script.py <input_csv_file>")
    sys.exit(1)

# Get the input CSV file from the command line arguments
csv_file = sys.argv[1]

# Read the data from the CSV file into a Pandas DataFrame
df = pd.read_csv(csv_file)

# Create a Matplotlib figure and axis
fig, ax = plt.subplots()

# Define the groups of columns
groups = ['X', 'Y', 'Z']

# Define the colors for enabled and disabled
enabled_color = 'lightgreen'
disabled_color = 'lightcoral'

# Define the positions for the vertical dotted lines
line_positions = [1.5, 3.5]

# Initialize a list to store median values
median_values = []

# Loop through each group (X, Y, Z)
for group in groups:
    # Get the enabled and disabled columns for the current group
    enabled_col = f'{group} enabled'
    disabled_col = f'{group} disabled'

    # Plot the box and whisker plots for enabled and disabled columns
    ax.boxplot([df[enabled_col], df[disabled_col]], positions=[1, 2], widths=0.6,
               boxprops=dict(facecolor=enabled_color),
               medianprops=dict(color='black'))

    # Add a vertical dotted line to separate the groups
    if group != 'X':
        ax.axvline(line_positions.pop(0), linestyle='--', color='black')

    # Get median values for enabled and disabled and store them in the list
    median_enabled = df[enabled_col].median()
    median_disabled = df[disabled_col].median()
    median_values.extend([median_enabled, median_disabled])

# Set x-axis ticks and labels for X, Y, and Z
ax.set_xticks([1.5, 3.5, 5.5])
ax.set_xticklabels(['X', 'Y', 'Z'])

# Set the y-axis label
ax.set_ylabel('AppRx in Kbps')

# Annotate the median values on the plot
for i, median in enumerate(median_values):
    x = i + 1
    ax.text(x, median, str(median), ha='center')

# Show the plot
plt.show()
