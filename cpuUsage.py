import matplotlib.pyplot as plt

bar_width = 0.3

small_cores = [47.09, 44.13, 57.8] 
big_cores = [22.04, 19.75, 21.38]

fig, ax = plt.subplots()

ax.bar(x=np.arange(len(small_cores)), height=small_cores, width=bar_width, color='lightblue', label='RCNB Off')
ax.bar(x=np.arange(len(big_cores)) + bar_width, height=big_cores, width=bar_width, color='lightcoral', label='Retransmission algorithm with prioritization')
ax.bar(x=np.arange(len(big_cores)) + 2*bar_width, height=big_cores, width=bar_width, color='lightgreen', label='Only context aware prioritizaton')

ax.set_xticks(np.arange(len(big_cores)) + bar_width)
ax.set_xticklabels(['Small Cores', 'Big Cores'])

ax.set_ylabel('CPU Core usage in %')
ax.legend()

fig.tight_layout()
plt.show()
