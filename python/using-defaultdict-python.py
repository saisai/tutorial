"""
Dictionaries are a convenient way to store data for later retrieval by name (key). Keys must be unique, immutable objects, and are typically strings. The values in a dictionary can be anything. For many applications the values are simple types such as integers and strings.

It gets more interesting when the values in a dictionary are collections (lists, dicts, etc.) In this case, the value (an empty list or dict) must be initialized the first time a given key is used. While this is relatively easy to do manually, the defaultdict type automates and simplifies these kinds of operations.

A defaultdict works exactly like a normal dict, but it is initialized with a function (“default factory”) that takes no arguments and provides the default value for a nonexistent key.

A defaultdict will never raise a KeyError. Any key that does not exist gets the value returned by the default factory.

"""
from collections import defaultdict

ice_cream = defaultdict(lambda: 'vanilla')

print(ice_cream)

ice_cream = defaultdict(lambda: 'vanilla')
ice_cream['Sarah'] = 'Chunky Monkey'
ice_cream['Abdul'] = 'Butter Pecan'

print(ice_cream['Sarah'])
print(ice_cream['Joe'])

"""
Be sure to pass the function object to defaultdict(). Do not call the function, i.e. defaultdict(func), not defaultdict(func()).

In the following example, a defaultdict is used for counting. The default factory is int, which in turn has a default value of zero. (Note: “lambda: 0″ would also work in this situation). For each food in the list, the value is incremented by one where the key is the food. We do not need to make sure the food is already a key – it will use the default value of zero.
"""

food_list = 'spam spam spam spam spam spam eggs spam'.split()
print(food_list)
food_count = defaultdict(int) # default value of int is 0
for food in food_list:
    food_count[food] += 1 # increment element's value by 1

print(food_count)


print('\n\n')

"""
In the next example, we start with a list of states and cities. We want to build a dictionary where the keys are the state abbreviations and the values are lists of all cities for that state. To build this dictionary of lists, we use a defaultdict with a default factory of list. A new list is created for each new key.

In conclusion, whenever you need a dictionary, and each element’s value should start with a default value, use a defaultdict.
"""

city_list = [('TX','Austin'), ('TX','Houston'), ('NY','Albany'), ('NY', 'Syracuse'), ('NY', 'Buffalo'), ('NY', 'Rochester'), ('TX', 'Dallas'), ('CA','Sacramento'), ('CA', 'Palo Alto'), ('GA', 'Atlanta')]

cities_by_state = defaultdict(list)
for state, city in city_list:
    cities_by_state[state].append(city)

for state, cities in cities_by_state.items():
    print(state, ', '.join(cities))

# https://www.accelebrate.com/blog/using-defaultdict-python
