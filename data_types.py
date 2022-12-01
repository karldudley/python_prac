# LIST - equivalent of an array in JS
# lists are mutable - they can be changed after creation (not everything is mutable in Python, unlike JS)
my_list = ['one', [2, 3.4], False]
print(my_list[1][1])

my_list[2] = True
print(my_list[2])

my_list.append(['hello', 'bonjour', 'Gutten Tag'])
print(my_list)

# Note this is not adding a list, but three ints
# use extend to add multiple items at once
my_list.extend([4, 5, 6])
print(my_list)

# DICTIONARY - equivalent of an object in JS
# dictionaries are mutable

# JavaScript
# let myObject = {
#     name: "Sarah",
#     age: 26
# }

# Python
my_dictionary = {
    "name": "Sarah",
    "age": 26
}
# 1st option to access a value in a dictionary
print(my_dictionary["age"])

# 2nd option to access a value in a dictionary
print(my_dictionary.get('name'))

# Add item to dictionary
my_dictionary['country'] = 'France'
print(my_dictionary)

# Update item of a dictionary
my_dictionary['age'] = 20
print(my_dictionary)

# TUPLE - like a list but it is immutable (use if the data shouldn't be changed after creation)
my_tuple = ('banana', 'kiwi', 'apple', 'orange')
print(type(my_tuple))

# similar to lists they can be accessed via index
print(my_tuple[1])

# These will not work
# my_tuple[1] = "watermelon"
# my_tuple.append(2)

# But you can overwrite the whole tuple
my_tuple = ('banana', 'watermelon', 'apple', 'orange')
print(my_tuple)

# SET - similar to an object but no key value pairs
# They are mutable but they are unchangeable
# you can remove and add but can not change individual items
# can only have unique items
# they are unordered and do not have an index
# they print in a different order each time I run it
my_set = {'banana', 'watermelon', 'apple', 'orange', 'banana'}
print(my_set)

my_set.add(3)
print(my_set)

my_set.update([3,4,5])
print(my_set)

# check for a value in a set
# sets are usually faster than lists
is_this_in_my_set = 'banana' not in my_set
print(is_this_in_my_set)
