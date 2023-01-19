from converter import converter
from path import csv_paths
from path import json_paths

# Instantiate and declare csv_to_json method
# convert_obj = json_converter.Converter(csv_paths.path_3, json_paths.json_path_3)
# print(convert_obj.csv_to_json())


# Function that converts all csv files to json files
def multiple_creation(csvf, jsonf):
    for i in range(1, 10):
        json_obj = converter.Converter(f'{csvf}{i}.csv', f'{jsonf}{i}.json')
        json_obj.csv_to_json()
    print('done')


csv_path = '../csv_data/pkmn_gen'
json_path = '../json_data/pkmn_gen_'
multiple_creation(csv_path, json_path)
