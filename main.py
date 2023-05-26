import requests

office = "EWX"
gridX = 156
gridY = 96
url = f"https://api.weather.gov/gridpoints/{office}/{gridX},{gridY}/forecast"\

print(url)

data = requests.get(url)  # get our data using requests
decoded_data = data.json()  # decode our data with the .json() method
# we can now access this JSON file, bound to decoded_data, w/ indexing

# print(decoded_data)

# JSON files are a collection of dictionaries, and lists

# print(type(decoded_data['properties']['periods']))

import datetime as dt
print("Our weekly forecast is:")
for each in decoded_data['properties']['periods']:
    if each['name'] in 'Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split(' '):
        print(f"{each['name']}, we have a temp of {each['temperature']} degrees Fahrenheit.")
    if each['name'] == 'Today' or each['name'] == 'Tonight':
        print(f"Monday, we have a temp of {each['temperature']} degrees Fahrenheit.")



# print()
# print(str(decoded_data))


# print(type(decoded_data['properties']))
