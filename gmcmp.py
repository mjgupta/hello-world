import matplotlib.pyplot as plt
import numpy as np

# Sample data
fast_latency_enabled = 50 
fast_latency_disabled = 100
http_latency_enabled = 150  
http_latency_disabled = 200

fast_bw_enabled = 20
fast_bw_disabled = 10
http_bw_enabled = 30
http_bw_disabled = 15

# Create figure and axes
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

# Plot bar chart
x = np.arange(2)
ax1.bar(x - 0.2, [fast_latency_enabled, fast_latency_disabled], 0.4, 
       color=['lightgreen'], edgecolor=['darkgreen'], hatch='', label='Fast')
ax1.bar(x + 0.2, [http_latency_enabled, http_latency_disabled], 0.4,
       color=['lightcoral'], edgecolor=['maroon'], hatch='', label='HTTP')

# Add latency labels
ax1.text(x=x[0]-0.2, y=fast_latency_enabled+5, s='X') 
ax1.text(x=x[1]-0.2, y=fast_latency_disabled+5, s='X')
ax1.text(x=x[0]+0.2, y=http_latency_enabled+5, s='X')
ax1.text(x=x[1]+0.2, y=http_latency_disabled+5, s='X')

# Format primary y-axis 
ax1.set_ylabel('In game latency in ms')

# Plot scatter chart  
# Plot scatter values 
ax2.scatter(x - 0.2, [fast_bw_enabled, fast_bw_disabled], marker='x', c='yellow')
ax2.text(x[0]-0.2, fast_bw_enabled/1000, f"{fast_bw_enabled/1000:.2f}")
ax2.text(x[1]-0.2, fast_bw_disabled/1000, f"{fast_bw_disabled/1000:.2f}")

ax2.scatter(x + 0.2, [http_bw_enabled, http_bw_disabled], marker='x', c='orange') 
ax2.text(x[0]+0.2, http_bw_enabled/1000, f"{http_bw_enabled/1000:.2f}")
ax2.text(x[1]+0.2, http_bw_disabled/1000, f"{http_bw_disabled/1000:.2f}")

# Format secondary y-axis
ax2.set_ylabel('Background Rx Throughput in Mbps')

# Final touches
ax1.set_xticks(x)
ax1.set_xticklabels(['Fast', 'HTTP'])
ax1.set_title('COD')
ax1.legend()

plt.show()
