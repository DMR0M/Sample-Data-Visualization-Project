import csv
import json
import pandas as pd


class Converter:
    """Class that converts csv to json and json to csv"""
    def __init__(self, file_1, file_2):
        self.csv_file = file_1
        self.json_file = file_2

    def csv_to_json(self) -> None:
        try:
            json_data: list[dict] = []
            # Read the csv file
            with open(self.csv_file, 'r', encoding='UTF-8') as csv_f:
                csv_reader = csv.DictReader(csv_f)
                for row in csv_reader:
                    json_data.append(row)

            # Convert json_data variable to json string and write to file
            with open(self.json_file, 'w', encoding='UTF-8') as json_f:
                json_string = json.dumps(json_data, indent=2)
                json_f.write(json_string)
            print('done converting csv to json')

        except FileNotFoundError:
            print('file not found')

    def json_to_csv(self) -> None:
        with open(self.json_file, 'r', encoding='UTF-8') as json_f:
            json_string = json.load(json_f)

        pkmn_df = pd.DataFrame(json_string)
        pkmn_df.to_csv(self.csv_file, index=False, header=True)
        print('done converting json to csv')


def main():
    # Initialize paths
    json_name = 'pkmn_gen_1.json'
    csv_file_path = '../../dummy/pkmn_gen2.csv'
    json_file_path = '../../json_data/pkmn_gen_2.json'

    # Instantiate and call method
    x = Converter(csv_file_path, json_file_path)
    # x.json_to_csv()
    # x.csv_to_json()
    help(Converter)


if __name__ == '__main__':
    main()
