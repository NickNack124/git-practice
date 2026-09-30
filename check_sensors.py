"""
week40_Task2: checking overdue sensors

Created on Wed Sep 30 06:25:18 2026

£author: Nikolai Enger Hoff
"""

import json
from pathlib import Path

import pandas as pd

# Importing data from yml file
with open("config.yml") as file:
    config = file.readlines()
    max_days_since = config[0].split(": ")[1].strip()
    output_file = config[1].split(": ")[1].strip('"')

# Importing- and merging data from csv and excel files
calibrations_df = pd.read_csv("calibrations.csv")
sensors_df = pd.read_excel("sensors.xlsx")  # (I had to add openpyxl to the venv)
sensor_data = pd.merge(sensors_df, calibrations_df, on="sensor_id")

# Filtering- and reformating the dataframe so it can be used in json.dump
overdue_sensors = sensor_data[sensor_data["days_since_calibration"] > int(max_days_since)]
overdue_sensors = overdue_sensors.to_dict(orient='records')

# Make a Json file and write down the data
with open(Path(__file__).parent / output_file, 'w') as file:
    json.dump(overdue_sensors, file, indent=2)
