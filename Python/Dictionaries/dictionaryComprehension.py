import random

city_names = ['Paris', 'London', 'Rome', 'Berlin', 'Madrid']

# Dictionary comprenhension
# - Create a dictionary based on a list
city_temps = {city:random.randint(20,30) for city in city_names}
print(city_temps)

# - Create a dictionary based on a dictionary
conditional_cities = {city:value for (city, value) in city_temps.items() if value <= 25 and value >= 21}
print(conditional_cities)