import json
import os

class Settings:
    def __init__(self, server_name, database, username, password, driver):
        self.server_name = server_name
        self.database = database
        self.username = username
        self.password = password
        self.driver = driver

def load_settings():
    # Check if the environment variable 'ENV' is set to 'test'
    settings_file = 'config.json'

    # Load the settings from the JSON file
    with open(settings_file, 'r') as f:
        settings_dict = json.load(f)

    # Create a Settings object with the loaded settings
    settings = Settings(
        settings_dict['server_name'],
        settings_dict['database'],
        settings_dict['username'],
        settings_dict['password'],
        settings_dict['driver']
    )

    return settings