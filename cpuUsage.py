import matplotlib.pyplot as plt

bar_width = 0.3
indexes = [1, 2, 3]

values1 = [47.09, 44.13, 57.8]
values2 = [22.04, 19.75, 21.38]

plt.bar(indexes, values1, width=bar_width, color='lightblue', label='Group 1')
plt.bar([i + bar_width for i in indexes], values2, width=bar_width, color='lightcoral', label='Group 2')

plt.xlabel('Bars')
plt.ylabel('Values')
plt.title('Grouped Bar Plot')
plt.xticks([i + bar_width for i in indexes], ['Bar 1', 'Bar 2', 'Bar 3'])
plt.legend()

plt.show()
