import matplotlib.pyplot as plt
import numpy as np

# Sample data
fast_latency_enabled = 150 
fast_latency_disabled = 200
http_latency_enabled = 100
http_latency_disabled = 250
fast_bandwidth_enabled = 20
fast_bandwidth_disabled = 15  
http_bandwidth_enabled = 30
http_bandwidth_disabled = 10

# Set up plot 
fig, ax1 = plt.subplots()
ax2 = ax1.twinx() 

# Latency bar plot
x = np.arange(2)
y1 = [fast_latency_enabled, fast_latency_disabled]
y2 = [http_latency_enabled, http_latency_disabled]
ax1.bar(x-0.2, y1, 0.4, color='lightgreen', edgecolor='darkgreen', label='Fast')
ax1.bar(x+0.2, y2, 0.4, color='lightcoral', edgecolor='maroon', label='Http')
ax1.set_xticks(x)
ax1.set_xticklabels(['Enabled','Disabled'])
ax1.set_ylabel('In game latency in ms')

for i, v in enumerate(y1):
    ax1.text(i-0.2, v+5, 'X', color='black', ha='center') 

for i, v in enumerate(y2):   
    ax1.text(i+0.2, v+5, 'X', color='black', ha='center')
    
# Bandwidth scatter plot  
ax2.scatter(x-0.2, [fast_bandwidth_enabled,fast_bandwidth_disabled], c='yellow', marker='x', label='Fast')
ax2.scatter(x+0.2, [http_bandwidth_enabled,http_bandwidth_disabled], c='orange', marker='x', label='Http') 
ax2.set_ylabel('Background Rx Throughput in Mbps')

# Final touches  
ax1.set_title('COD')
ax1.legend()
ax2.legend()
ax2.grid(None)
fig.tight_layout()  

plt.show()
