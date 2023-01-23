# Import local libraries and pandas
from url import urls
from path import csv_paths

import pandas as pd


# Getting specific html tags and identifiers
# Store in a list
html_data = urls.soup.find_all('table', class_='data-table')
pkmn_names = urls.soup.find_all('td', class_='cell-name')
pkmn_types = urls.soup.find_all('td', class_='cell-icon')
pkmn_stats = urls.soup.find_all('td', class_='cell-num')

# Store all data from the 'cell-num' class tags in a list
add_data = [data.text for data in pkmn_stats]
print(add_data)

# Store each column data in a list slice,
# and convert elements to int
pokedex_id_cols = map(int, add_data[::8])
base_total_cols = map(int, add_data[1::8])
hp_cols = map(int, add_data[2::8])
atk_cols = map(int, add_data[3::8])
def_cols = map(int, add_data[4::8])
spatk_cols = map(int, add_data[5::8])
spdef_cols = map(int, add_data[6::8])
speed = map(int, add_data[7::8])


# Create dictionary
pkmn_data: list[dict] = [{
                    'Pokedex Number': pkdx,
                    'Name': nm.text,
                    'Type': typ.text,
                    'Hp': hp,
                    'Attack': atk,
                    'Defense': de,
                    'Sp. Attack': spatk,
                    'Sp. Defense': spdef,
                    'Speed': spd,
                    'Base Total': bt
    } for pkdx, nm, typ, hp, atk, de, spatk, spdef, spd, bt
      in zip(pokedex_id_cols, pkmn_names, pkmn_types, hp_cols,
             atk_cols, def_cols, spatk_cols, spdef_cols,
             speed, base_total_cols)
]
# Visual
for i, ele in enumerate(pkmn_data, start=1):
    print(f'{i}: {ele}')

# Convert to csv
pkmn_df = pd.DataFrame(pkmn_data)
# Change csv path here
# pkmn_df.to_csv(csv_paths.path_9, index=False, header=True)
pkmn_gen9_stats = pd.read_csv(csv_paths.path_9, index_col=2)
pkmn_gen1_stats = pd.read_csv(csv_paths.path_1)
sort_by_speed = pkmn_gen9_stats.sort_values('Speed', ascending=False)

print(sort_by_speed.head(20))

