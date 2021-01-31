# dummy_data.py
# Loads dummy data from json files to populate the webpage while there is no backend established.

# Use os to navigate path and json to load json files
import os
import json


class DummyData:
    """Generate a set of dummy data to populate the site's database."""

    def __init__(self):
        """Load all dummy files on initialization."""

        self.special_components = self.load_data("special_components")
        self.regular_components = self.load_data("regular_components")

    @staticmethod
    def load_data(filename):
        """Load json files containing dummy data."""

        # Create a link to the `data` directory inside the `cim` directory
        data_path = os.path.join("cim", "data")

        # Load the json filename proviced
        with open(f"{data_path}/{filename}.json") as json_file:
            return json.load(json_file)