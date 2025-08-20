brand = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {
        'France': 'blue',
        'Spain': 'red',
        'US': ['pink', 'green']
    }
}

brand['number_stores'] = 2

print(f"Zara's clients are {', '.join(brand['type_of_clothes'][:-1])} and {brand['type_of_clothes'][-1]}.")

brand['country_creation'] = 'Spain'

if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')

del brand['creation_date']

print(f"Last international competitor: {brand['international_competitors'][-1]}")

print(f"Major colors in US: {', '.join(brand['major_color']['US'])}")

print(f"Number of key-value pairs: {len(brand)}")

print(f"Dictionary keys: {', '.join(brand.keys())}")

more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000
}

brand.update(more_on_zara)

print(f"Number of stores: {brand['number_stores']}")
# number_stores updated from 7000 to 10000