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
        
        # Get a sample of the data (e.g., 5 rows)
        sample_df = df.sample(n=5)
        
        # Print the sample
        print(f"Sample from {file}:")
        print(sample_df)
        print("\n" + "-"*50 + "\n")
