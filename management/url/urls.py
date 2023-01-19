# Import BeautifulSoup and requests library
from bs4 import BeautifulSoup
import requests

# Initialize url and request

# Pokemondb.net
url_1 = 'https://pokemondb.net/pokedex/stats/gen1'
url_2 = 'https://pokemondb.net/pokedex/stats/gen2'
url_3 = 'https://pokemondb.net/pokedex/stats/gen3'
url_4 = 'https://pokemondb.net/pokedex/stats/gen4'
url_5 = 'https://pokemondb.net/pokedex/stats/gen5'
url_6 = 'https://pokemondb.net/pokedex/stats/gen6'
url_7 = 'https://pokemondb.net/pokedex/stats/gen7'
url_8 = 'https://pokemondb.net/pokedex/stats/gen8'
url_9 = 'https://pokemondb.net/pokedex/stats/gen9'

# Serebii.net
s_url_1 = 'https://www.serebii.net/pokemon/gen1pokemon.shtml'

# Change url here
page = requests.get(url_9)
serebii_page = requests.get(s_url_1)


# Load HTML page content
soup = BeautifulSoup(page.content, 'html.parser')
pkmn = BeautifulSoup(serebii_page.content, 'html.parser')

