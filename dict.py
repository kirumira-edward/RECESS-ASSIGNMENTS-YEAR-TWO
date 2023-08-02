     #returning a list of values in a dictionary
my_dict = {'key1': 4, 'key2': 5, 'key3': 6}
values_list = list(my_dict.values())
print(values_list)

       #checking if a key exists int he dictionary
my_dict = {'key1': 4, 'key2': 5, 'key3': 6}
if 'key2' in my_dict:
    print("The key 'key2' exists in the dictionary.")
else:
    print("The key 'key2' does not exist in the dictionary.")

       #changing and updating dictionary items
my_dict = {'key1': 4, 'key2': 5, 'key3': 6}
# Changing the value of an existing key
my_dict['key2'] = 50
print(my_dict)
# Adding a new key-value pair
my_dict['key4'] = 40
print(my_dict)
# Updating the dictionary with another dictionary
new_dict = {'key2': 34, 'key5': 99}
my_dict.update(new_dict)
print(my_dict)

           #adding and removing dictionary items
my_dict = {'key1': 4, 'key2': 5, 'key3': 6}
# Adding a new key-value pair
my_dict['key4'] = 40
print(my_dict)
# Removing a key-value pair using del
del my_dict['key2']
print(my_dict)
# Removing a key-value pair using pop()
removed_value = my_dict.pop('key3')
print(removed_value)
print(my_dict)


         # Looping through a dictionary
my_dict = {'key1': 4, 'key2': 5, 'key3': 6}
# Iterating over keys
for key in my_dict:
    print(key)
# Iterating over values
for value in my_dict.values():
    print(value)
# Iterating over key-value pairs
for key, value in my_dict.items():
    print(key, value)
# Nesting dictionaries
nested_dict = {
    'person1': {'name': 'raymond', 'age': 43},
    'person2': {'name': 'Janat', 'age': 30},
    'person3': {'name': 'Bobby', 'age': 32}
}
# Accessing nested dictionary values
print(nested_dict['person2']['name'])
print(nested_dict['person3']['age'])



