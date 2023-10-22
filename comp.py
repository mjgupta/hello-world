import pandas as pd
import matplotlib.pyplot as plt
import sys

csv_file = sys.argv[1] 

df = pd.read_csv(csv_file)

fig, ax = plt.subplots()

ax.boxplot([df['X enabled'], df['X disabled']], positions=[1,2], widths=0.6,
           boxprops=dict(facecolor='lightgreen'),
           medianprops=dict(color='black')) 

ax.axvline(2.5, linestyle='--', color='black')

ax.boxplot([df['Y enabled'], df['Y disabled']], positions=[3,4], widths=0.6,
           boxprops=dict(facecolor='lightgreen'),
           medianprops=dict(color='black'))

ax.axvline(4.5, linestyle='--', color='black')

ax.boxplot([df['Z enabled'], df['Z disabled']], positions=[5,6], widths=0.6,
           boxprops=dict(facecolor='lightgreen'),
           medianprops=dict(color='black'))

ax.set_xticks([1.5, 3.5, 5.5])
ax.set_xticklabels(['X', 'Y', 'Z'])

ax.set_ylabel('AppRx in Kbps')

for i, box in enumerate(ax.artists):
    x = i + 1
    y = box.get_ydata()[2] 
    ax.text(x, y, str(y), ha='center') 

plt.show()
