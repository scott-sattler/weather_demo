import requests


# get data
    # how do we get data?  # noqa
    # we use this thing  # noqa
    # https://api.weather.gov/gridpoints/{office}/{grid X},{grid Y}/forecast  # noqa

# transform data
    # what type of data is it?  # noqa
        # JSON file - is a collection of dictionaries and lists  # noqa
        # specifically, a nested collection of lists/dicts  # noqa


# display data
    # figure out how to display the data we want  # noqa


my_data = \
    {'person':
        [
            {'name': 'john'},
            {'age': 22}
        ]
}

# outer_most = my_data
# print(type(outer_most))
# one_level_lower = my_data['person']
# print(type(one_level_lower))
# two_levels_lower = my_data['person'][1]
# print(type(two_levels_lower))
# print(my_data['person'][1]['age'])







# # get data
# # https://api.weather.gov/gridpoints/{office}/{grid X},{grid Y}/forecast  # noqa
# # remember, we're using this as a URL
#
# office = "EWX"
# gridX = 156
# gridY = 96
# URL = f"https://api.weather.gov/gridpoints/{office}/{gridX},{gridY}/forecast"
# # print(URL)
# data = requests.get(URL)
# # print(data)
#
# # don't forget to use packages! here, requests
#
# # transform data
# decoded_data = data.json()
#
# # display data









# get data (using requests package)
office = "EWX"
gridX = 156
gridY = 96
URL = f"https://api.weather.gov/gridpoints/{office}/{gridX},{gridY}/forecast"
data = requests.get(URL)

# transform data
decoded_data = data.json()
data_for_each_day = decoded_data['properties']['periods']
print(data_for_each_day[0])

# display data
for each_day in data_for_each_day:
    print(each_day['name'], each_day['temperature'])
