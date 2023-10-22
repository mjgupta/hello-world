import pandas as pd
import matplotlib.pyplot as plt
import sys

csv_file = sys.argv[1]

df = pd.read_csv(csv_file)

fig, ax = plt.subplots()

ax.boxplot([df['X enabled']], positions=[1], widths=0.6,
           boxprops=dict(facecolor='lightgreen'))

ax.boxplot([df['X disabled']], positions=[2], widths=0.6,
           boxprops=dict(facecolor='lightcoral'))

ax.axvline(2.5, linestyle='--', color='black')

ax.boxplot([df['Y enabled']], positions=[3], widths=0.6,
           boxprops=dict(facecolor='lightgreen')) 

ax.boxplot([df['Y disabled']], positions=[4], widths=0.6,
           boxprops=dict(facecolor='lightcoral'))

ax.axvline(4.5, linestyle='--', color='black')

ax.boxplot([df['Z enabled']], positions=[5], widths=0.6,
           boxprops=dict(facecolor='lightgreen'))

ax.boxplot([df['Z disabled']], positions=[6], widths=0.6, 
           boxprops=dict(facecolor='lightcoral'))

ax.set_xticks([1.5, 3.5, 5.5])
ax.set_xticklabels(['X', 'Y', 'Z'])  

ax.set_ylabel('AppRx in Kbps')

for i, box in enumerate(ax.artists):
    x = i // 2 + 1
    y = box.get_ydata()[2]
    ax.text(x, y, str(y), ha='center')

plt.show()
