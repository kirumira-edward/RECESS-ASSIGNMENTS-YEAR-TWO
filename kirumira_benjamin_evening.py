#names of people
names = ["Rashford", "Bob", "Owen", "David", "Evans"]
print(names[1])  

#changing index of the first person
names[0] = "Alex"
print(names)  

#adding a sixth person
names.append("Frank")
print(names) 

#adding bathel as the 3rd item
names.insert(2, "Bathel")
print(names)  

#remove the 4th item
del names[3]
print(names)  

#negative index to print the last item
print(names[-1])  

#new list with indexes to print the 3rd ,4th and 5th
new_list = ["John", "Kate", "Liam", "Mia", "Oliver", "Sophia", "William"]
print(new_list[2:5]) 

#list of countries and making a copy of it
countries = ["USA", "Canada", "France", "Germany", "Japan"]
countries_copy = countries.copy()
print(countries_copy) 

# a loop throught the countries
for country in countries:
    print(country)

#animal names and sorting them in both descending and ascending order
animals = ["lion", "elephant", "tiger", "giraffe", "zebra"]
#ascednding order
animals.sort()  
print(animals)
# descending order
animals.sort(reverse=True)  
print(animals)  

# onlyoutput animals with aletter a
animals_with_a = [animal for animal in animals if 'a' in animal]
print(animals_with_a)  # Output: ["zebra", "giraffe"]

#joining first and second names
first_names = ["Kirumira"]
second_names = ["benjamin"]
full_names = first_names + second_names
print(full_names) 


#tuple  for my favorite phone brand
x = ("samsung", "iphone", "tecno", "redmi")
favorite_brand = x[1]
print(favorite_brand)  

#negative indexing the second item in the list
second_last_item = x[-2]
print(second_last_item)  

#updating iphone to itel


#addinh huawei to my tuple
x = x + ("Huawei",)
print(x)  # Output: ("samsung", "itel", "tecno", "redmi", "Huawei")

#looping through the tuple
for item in x:
    print(item)

#removing the first item from my tuple
x = x[1:]
print(x) 

#tuple of cities
uganda_cities = tuple(["Kampala", "Entebbe", "Jinja", "Mbarara"])
print(uganda_cities)

#unpacking the tuple
brand1, brand2, brand3, brand4 = x
print(brand1, brand2, brand3, brand4)

#printing cities
print(uganda_cities[1:4]) 

#tuple containing my names
first_names = ("Kirumnira")
second_names = ("Benjamin")
full_names = first_names + second_names
print(full_names)

#tuple of colors being multiplied by 3
colors = ("red", "green", "blue")
multiplied_colors = colors * 3
print(multiplied_colors)

#number of times 8 is appearing
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_8 = thistuple.count(8)
print(count_8)  # Output: 2

#1. Use the set() constructor to create a set of 3 of your favorite beverages.
beverages = set(["coffee", "tea", "juice"])

#2. Use the correct method to add 2 more items to the beverages set.
beverages.update(["water", "soda"])

#3. Given the set below;
#mySet = {“oven”, “kettle”, “microwave”, “refrigerator”}
#check if microwave is present in the set.
mySet = {"oven", "kettle", "microwave", "refrigerator"}

if "microwave" in mySet:
    print("Microwave is present in the set.")
else:
    print("Microwave is not present in the set.")

#4. Write a python program to remove “kettle” from the set above.
mySet.remove("kettle")

#5. Write a python program to loop through the set above.
for item in mySet:
    print(item)
#6
mySet = {1, 2, 3, 4}  # Set of 4 items
myList = [5, 6]  # List of 2 items

# Adding elements from the list to the set
mySet.update(myList)

print(mySet)

#7containing ages  and first names
ages = {25, 30, 35}
names = {"John", "Alice", "Bob"}

joined_set = ages.union(names)
print(joined_set)
{35, 'John', 25, 30, 'Bob', 'Alice'}

#STRINGS
integer_var = 10
string_var = " years old"

concatenated_string = str(integer_var) + string_var
print(concatenated_string)
 
#2outputting string without spaces at the beginning
txt = " Hello, Uganda! "

trimmed_txt = txt.strip()
print(trimmed_txt)

#3convert txt to uppercase
txt = "Hello, Uganda!"

uppercase_txt = txt.upper()
print(uppercase_txt)

#4 replacing u with v
txt = "Hello, Uganda!"

replaced_txt = txt.replace('U', 'V')
print(replaced_txt)

#5returning a range of characters
y = "I am proudly Ugandan"

range_of_characters = y[1:4]
print(range_of_characters)

#6correcting an error
x = 'All "Data Scientists" are cool!'
# or
x = "All \"Data Scientists\" are cool!"
print(x)

#Dictionaries
#1printing shoe size
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

print(Shoes["size"])

#2changing nick to adidas
Shoes["brand"] = "Adidas"

print(Shoes)

#3add snaekrs to the dictionary
Shoes["type"] = "sneakers"

print(Shoes)

#4returning a list of all keys
keys_list = list(Shoes.keys())

print(keys_list)

#5returning a list of all values
values_list = list(Shoes.values())

print(values_list)

#6checking shoe size
if "size" in Shoes:
    print("The key 'size' exists in the dictionary.")
else:
    print("The key 'size' does not exist in the dictionary.")

#7looping through a dictionary
for key, value in Shoes.items():
    print(key, ":", value)

#8 removing color from dictionary
del Shoes["color"]

print(Shoes)

#9emptying the dictionary
Shoes.clear()

print(Shoes)

#10
original_dict = {
    "key1": "gold",
    "key2": "copper",
    "key3": "dogs"
}

# Making a copy of the original dictionary
copied_dict = original_dict.copy()

print(copied_dict)

#11showing nested dictionaries
nested_dict = {
    "outer_key1": {
        "inner_key1": "value1",
        "inner_key2": "value2"
    },
    "outer_key2": {
        "inner_key3": "value3",
        "inner_key4": "value4"
    }
}

# Accessing values in the nested dictionary
print(nested_dict["outer_key1"]["inner_key1"])
print(nested_dict["outer_key2"]["inner_key4"])
