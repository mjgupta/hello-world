import os
import csv

# Get list of all CSV files in current folder
csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]

for csv_file in csv_files:

  # Open current CSV file
  with open(csv_file, 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    lines = list(csv_reader)
    
  # Remove last 2 lines
  lines = lines[:-2]  

  # Open CSV file in write mode    
  with open(csv_file, 'w', newline='') as write_obj:
    csv_writer = csv.writer(write_obj)
    
    # Write lines without last 2
    for line in lines:
      csv_writer.writerow(line)
