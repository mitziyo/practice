'''
Tuple 
(1) What is tuple: tuple vs list
(2) Unpacing arguments
(3) zip
'''

print("======= What is tuple: tuple vs list =======")
# Java/PHP/NodeJs array => Python list

# literal
numbs = [3, 5, 1, 2]
# car_dict = {"brand": "Ferrari", "year": 1995}
# print(numbs)

# constructor
letters = list("Hello world!")
# person_dict = dict(name="Martin", age=35)
# print(letters)

fruits = ["apple", "lemon", "banana", "kiwi"]
print("before fruits", fruits)

fruits[2] = "melon"
print("after fruits", fruits)

# we cannot mutate tuple 
animals = ("dog", "cat", "fish", "lion")
tuple_obj = ("MIT", 100, True, None)

print(animals[0])
animals[0] = "bird"
print(animals)