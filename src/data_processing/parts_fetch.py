import os
from pcpartpicker import API
import pandas as pd
import json
import config

# Instantiate API
api = API()
api.set_region(config.API_REGION)

# Ensure the 'data' folder exists
DATA_FOLDER = "data"
os.makedirs(DATA_FOLDER, exist_ok=True)

def fetch_and_update_data(class_name, csv_filename, unique_field):
    """General function to fetch data, compare with existing CSV, and add new data."""
    # Retrieve data from API
    data = api.retrieve(class_name)
    data_json = data.to_json()
    data_dict = json.loads(data_json)
    data_list = data_dict.get(class_name, [])
    
    # Convert to DataFrame
    df = pd.DataFrame(data_list)
    
    # Full path to the CSV file
    csv_filepath = os.path.join(DATA_FOLDER, csv_filename)
    
    # Load the existing data from the CSV (if it exists)
    try:
        existing_df = pd.read_csv(csv_filepath)
    except FileNotFoundError:
        existing_df = pd.DataFrame()  # If the file doesn't exist, create an empty DataFrame
    
    # Merge the new data with the existing data, keeping only the unique entries based on `unique_field`
    if not existing_df.empty:
        df = pd.concat([existing_df, df]).drop_duplicates(subset=[unique_field], keep='last')
    
    # Save the updated DataFrame back to CSV
    df.to_csv(csv_filepath, index=False)


def fetch_cpu_data():
    fetch_and_update_data("cpu", "cpu_data.csv", "model")

def fetch_cpucooler_data():
    fetch_and_update_data("cpu-cooler", "cpu_cooler_data.csv", "model")

def fetch_motherboard_data():
    fetch_and_update_data("motherboard", "motherboard_data.csv", "model")

def fetch_memory_data():
    fetch_and_update_data("memory", "memory_data.csv", "model")

def fetch_storage_drive_data():
    fetch_and_update_data("internal-hard-drive", "internal_hard_drive_data.csv", "model")

def fetch_gpu_data():
    fetch_and_update_data("video-card", "gpu_data.csv", "model")

def fetch_psu_data():
    fetch_and_update_data("power-supply", "psu_data.csv", "model")

def fetch_case_data():
    fetch_and_update_data("case", "case_data.csv", "model")

def fetch_fan_data():
    fetch_and_update_data("case-fan", "case_fan_data.csv", "model")

def fetch_fancontroller_data():
    fetch_and_update_data("fan-controller", "fan_controller_data.csv", "model")

def fetch_thermalpaste_data():
    fetch_and_update_data("thermal-paste", "thermal_paste_data.csv", "model")

def fetch_opticaldrive_data():
    fetch_and_update_data("optical-drive", "optical_drive_data.csv", "model")

def fetch_soundcard_data():
    fetch_and_update_data("sound-card", "sound_card_data.csv", "model")

def fetch_ethernetcard_data():
    fetch_and_update_data("wired-network-card", "ethernet_card_data.csv", "model")

def fetch_wirelesscard_data():
    fetch_and_update_data("wireless-network-card", "wireless_card_data.csv", "model")

def fetch_monitor_data():
    fetch_and_update_data("monitor", "monitor_data.csv", "model")

def fetch_externalhdd_data():
    fetch_and_update_data("external-hard-drive", "external_hard_drive_data.csv", "model")

def fetch_headphones_data():
    fetch_and_update_data("headphones", "headphones_data.csv", "model")

def fetch_keyboard_data():
    fetch_and_update_data("keyboard", "keyboard_data.csv", "model")

def fetch_mouse_data():
    fetch_and_update_data("mouse", "mouse_data.csv", "model")

def fetch_speakers_data():
    fetch_and_update_data("speakers", "speakers_data.csv", "model")

def fetch_ups_data():
    fetch_and_update_data("ups", "ups_data.csv", "model")
