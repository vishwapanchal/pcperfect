import src.data_processing.parts_fetch as pf

def update_all_components():
    """
    Calls all the data-fetching functions for each component type
    and ensures the database is updated only with new data.
    """
    print("Updating CPU data...")
    pf.fetch_cpu_data()

    print("Updating CPU Cooler data...")
    pf.fetch_cpucooler_data()

    print("Updating Motherboard data...")
    pf.fetch_motherboard_data()

    print("Updating Memory data...")
    pf.fetch_memory_data()

    print("Updating Storage Drive data...")
    pf.fetch_storage_drive_data()

    print("Updating GPU data...")
    pf.fetch_gpu_data()

    print("Updating PSU data...")
    pf.fetch_psu_data()

    print("Updating Case data...")
    pf.fetch_case_data()

    print("Updating Fan data...")
    pf.fetch_fan_data()

    print("Updating Fan Controller data...")
    pf.fetch_fancontroller_data()

    print("Updating Thermal Paste data...")
    pf.fetch_thermalpaste_data()

    print("Updating Optical Drive data...")
    pf.fetch_opticaldrive_data()

    print("Updating Sound Card data...")
    pf.fetch_soundcard_data()

    print("Updating Ethernet Card data...")
    pf.fetch_ethernetcard_data()

    print("Updating Wireless Card data...")
    pf.fetch_wirelesscard_data()

    print("Updating Monitor data...")
    pf.fetch_monitor_data()

    print("Updating External HDD data...")
    pf.fetch_externalhdd_data()

    print("Updating Headphones data...")
    pf.fetch_headphones_data()

    print("Updating Keyboard data...")
    pf.fetch_keyboard_data()

    print("Updating Mouse data...")
    pf.fetch_mouse_data()

    print("Updating Speakers data...")
    pf.fetch_speakers_data()

    print("Updating UPS data...")
    pf.fetch_ups_data()

    print("All components have been updated.")
