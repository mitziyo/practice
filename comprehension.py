'''
comprehension 
(1) What is comprehension & list comp
(2) set and ditionary comprehension
'''

print("======= What is comprehension & list comprehension =======")
# Comprehension acts like spread operators!
# comprehension js dagi spread kabidir


# comprehensions qoliplari
'''
    Comprehension general syntax:
a) *iterable
a) <expression> for item in iterable 
a) <expression> for item in iterable <condition>
'''

# list comp
numbers = [1, 2, 5, 8, 4, 20]
list_numbers = [*numbers]  # a version

print("list_numbers:", list_numbers)
print(numbers is list_numbers)
print(id(numbers), id(list_numbers))

print("--------------")

# tuplelardan iborat bolgan list
people = [("Robert", 20), ("Stive", 19), ("Joseph", 25)]
list_people = [person[0] for person in people]  # b version

print("list_people:", list_people)

print("--------------")

cars = [
    ("Ferrari", 78),
    ("Tayota", 87),
    ("Audi", 117),
    ("BMW", 109),
    ("Pogani", 33)
]

list_cars = [car[0] for car in cars if car[1] > 80]
print("list_cars:", list_cars)
