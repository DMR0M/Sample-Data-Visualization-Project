import json
import os
from random import choice


class Jsonification:
    def __init__(self, path: str, data: list[dict]):
        self.path = path
        self.data_collections = data

    def jsonify(self) -> None:
        # Convert to json string or json format
        with open(self.path, 'w') as json_f:
            json_string = json.dumps(self.data_collections, indent=2)
            # Create json file
            json_f.write(json_string)

    @staticmethod
    def insert_entry(file_path: str, data_entry: dict) -> None:
        # Insert to json file path
        with open(file_path, 'r') as json_f:
            json_str = json.load(json_f)
            # Append entry to loaded json
            json_str.append(data_entry)

        # Convert to json string
        json_stringify = json.dumps(json_str, indent=2)

        # Open json file and write json string with the appended entry
        with open(file_path, 'w') as json_f:
            json_f.write(json_stringify)

    @staticmethod
    def delete_json(path) -> None:
        os.remove(path)


def main():
    f_path = '../csv_data/sample.json'
    # Sample Data Collection
    sample_data = [{
        'Name': 'Rommel',
        'Age': 23,
        'Job': 'Data Engineer'
    }, {
        'Name': 'Lance',
        'Age': 23,
        'Job': 'Front-End Developer'
    }, {
        'Name': 'Kevin',
        'Age': 23,
        'Job': 'Full-Stack Developer'
    }, {
        'Name': 'Cyrelle',
        'Age': 23,
        'Job': 'CyberSecurity Engineer'
    }, {
        'Name': 'Marck',
        'Age': 25,
        'Job': 'Tech Support'
    }, {
        'Name': 'Mari',
        'Age': 22,
        'Job': 'Front-End Web Developer'
    },
    ]
    insert_data = {
        'Name': 'RR',
        'Age': 25,
        'Job': 'Machine Learning Engineer'
    }
    random_data = choice(sample_data)
    j = Jsonification(f_path, sample_data)
    j.jsonify()
    j.insert_entry(f_path, insert_data)


if __name__ == '__main__':
    main()
