# Import local libraries and pandas
from url import urls
from path import csv_paths
import pandas as pd

data = urls.pkmn.find_all('td', class_='fooinfo')
links = urls.pkmn.find_all('a')

x = []

for l in links:
    x.append(l.get('href'))
print(x)

# pre = '/pokemon/type/'
# types = [f'{pre}grass', f'{pre}fire', f'{pre}water', f'{pre}electric', f'{pre}flying',
#          f'{pre}dragon', f'{pre}dark', f'{pre}rock', f'{pre}steel', f'{pre}ground',
#          f'{pre}psychic', f'{pre}ghost', f'{pre}fairy', f'{pre}fighting', f'{pre}poison',
#          f'{pre}ice', f'{pre}bug', f'{pre}normal']


org_data = [i.text.strip() for i in data]
# for ele in org_data:
#     print(ele)


