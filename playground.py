import os
import pandas as pd

# Define the path to the directory containing the CSV files
data_folder = 'C:\\Users\\vishw\\Desktop\\PC_Perfect_Demo\\data'

# List all files in the directory
files = os.listdir(data_folder)

# Iterate over each file in the directory
for file in files:
    # Check if the file is a CSV
    if file.endswith('.csv'):
        # Full path to the CSV file
        csv_filepath = os.path.join(data_folder, file)
        
        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_filepath)
        
        # Get the total number of rows
        total_rows = len(df)
        
        # Print the total number of rows for each CSV file
        print(f"Total number of rows in {file}: {total_rows}")
