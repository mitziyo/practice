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
# animals[0] = "bird"
# print(animals)


# try avoid this
people = "Andrew", "John"
animals = "dog",

print("======= Unpacing arguments =======")
groups = ["MIT", "FLEXY", "DEVEX", "MG"]
(x, y, *z) = groups
print(f"the x: {x}, and y: {y} ")
print("z:", z)

# *args > tuple


def calculate(*args):
    print("*args", args)
    total = 1
    for x in args:
        total *= x
    print(f"the total value: {total}")
    return total


# CALL
calculate(1, 7, 2, 3)
print("--------")
calculate(0, 2, 300)
print("--------")
calculate(5, 7)


print("-------------")
# **kwargs > dictionary


def introduce(**kwargs):
    print(f"the type(**kwargs) value: {type(kwargs)}")
    print(f"Hi, I am {kwargs["name"]} and I am {kwargs["age"]} years old!")


# CALL
introduce(name="Justin", age=28)
introduce(name="Shawn", age=30, single=True)
print("--------------------------------------- ")


def greeting(*args, **kwargs):
    print("*args >", args)
    print("**kwargs >", kwargs)


# CALL
greeting("hi", True, 10, name="John", age=22)
