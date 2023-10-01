import os
import pyshark
import csv

# Set the root folder path 
root_folder = 'path/to/pcap/files'

# Open CSV file for writing
csv_file = open('output.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)

# Loop through all files in the root folder and subfolders
for root, dirs, files in os.walk(root_folder):
    for file in files:
        if file.endswith('.pcap'):
            file_path = os.path.join(root, file)
            
            # Process the pcap file
            cap = pyshark.FileCapture(file_path)
            param1 = # get parameter 1
            param2 = # get parameter 2
            
            # Write row to CSV
            csv_writer.writerow([file_path, param1, param2])
            
csv_file.close()
