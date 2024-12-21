import pandas as pd
import os
from sklearn.preprocessing import MinMaxScaler
import json

# Define the path to the directory containing the CSV files
DATA_FOLDER = 'C:\\Users\\vishw\\Desktop\\PC_Perfect_Demo\\data'

def clean_data(file_path):
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)

        # Remove duplicates
        df.drop_duplicates(inplace=True)

        # Handle missing values
        df.fillna(method='ffill', inplace=True)  # Forward fill for simplicity

        # Convert dict and list columns to strings or extract specific values
        for column in df.columns:
            if df[column].apply(lambda x: isinstance(x, (dict, list))).any():
                df[column] = df[column].apply(lambda x: json.dumps(x) if isinstance(x, (dict, list)) else x)

        # Standardize price format
        if 'price' in df.columns:
            df['price'] = df['price'].apply(lambda x: float(x[1]) if isinstance(x, list) and len(x) > 1 else 0.0)

        # Convert data types
        for column in df.select_dtypes(include=['object']).columns:
            df[column] = df[column].astype('category')

        # Normalize numerical features
        scaler = MinMaxScaler()
        numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
        df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

        # Consistency checks and domain-specific cleaning
        if 'form_factor' in df.columns:
            df['form_factor'] = df['form_factor'].str.lower()

        # Convert all text to lowercase for consistency
        df = df.applymap(lambda s: s.lower() if type(s) == str else s)

        # Save the cleaned DataFrame back to CSV
        df.to_csv(file_path, index=False)
        print(f"Cleaned data for {file_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# Iterate over each component file and clean the data
component_files = [
    'case_data.csv', 'case_fan_data.csv', 'cpu_cooler_data.csv', 'cpu_data.csv',
    'ethernet_card_data.csv', 'external_hard_drive_data.csv', 'fan_controller_data.csv',
    'gpu_data.csv', 'headphones_data.csv', 'internal_hard_drive_data.csv',
    'keyboard_data.csv', 'memory_data.csv', 'monitor_data.csv', 'motherboard_data.csv',
    'mouse_data.csv', 'optical_drive_data.csv', 'psu_data.csv', 'sound_card_data.csv',
    'speakers_data.csv', 'thermal_paste_data.csv', 'ups_data.csv', 'wireless_card_data.csv'
]

for component_file in component_files:
    file_path = os.path.join(DATA_FOLDER, component_file)
    clean_data(file_path)
