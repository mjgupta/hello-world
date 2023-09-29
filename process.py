import os
import pandas as pd
import matplotlib.pyplot as plt

# Get list of all CSV files in folder 
csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]

for csv_file in csv_files:

  # Check if enable file
  if 'enable' in csv_file:
      
    # Split on '_enable_' to get base name
    name_parts = csv_file.split('_enable_')
    base_name = name_parts[0]
    
    # Construct disable filename
    disable_file = base_name + '_disable_' + name_parts[1] 

    if disable_file in csv_files:

      # Read enable CSV
      df1 = pd.read_csv(csv_file)
      
      # Read disable CSV
      df2 = pd.read_csv(disable_file)
      
      # Extract 'speedUid(K) R' columns
      data1_uid = df1['speedUid(K) R']
      data2_uid = df2['speedUid(K) R']
      
      # Extract 'speedTotal(K) R' columns
      data1_total = df1['speedTotal(K) R'] 
      data2_total = df2['speedTotal(K) R']
       
      # Plot 'speedUid(K) R'  
      plt.boxplot([data1_uid, data2_uid], positions=[1, 2], widths=0.6, patch_artist=True)
      plt.boxplot([data1_uid], positions=[1], widths=0.6, boxprops=dict(color='green'))
      plt.boxplot([data2_uid], positions=[2], widths=0.6, boxprops=dict(color='red'))  
      plt.xticks([1, 2], ['Enable', 'Disable'])
      plt.ylabel('AppRx in Kbps')
      plt.savefig(base_name + '_uid.png')
      plt.clf()
      
      # Plot 'speedTotal(K) R'
      plt.boxplot([data1_total, data2_total], positions=[1, 2], widths=0.6, patch_artist=True)
      plt.boxplot([data1_total], positions=[1], widths=0.6, boxprops=dict(color='green'))
      plt.boxplot([data2_total], positions=[2], widths=0.6, boxprops=dict(color='red'))
      plt.xticks([1, 2], ['Enable', 'Disable']) 
      plt.ylabel('AppRx in Kbps')
      plt.savefig(base_name + '_total.png')
      plt.clf()
