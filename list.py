'''
List 
(1) Working with lists
(2) List methods
(3) Lambada function
(4) enumarate, map and filter
'''

print("======= Working with lists =======")
# literal
person = {"name": "Justin", "age": 25}  # dictionary
people = ("Andrew", "John", "Michael")  # tuple
groups = ["MIT", "FLEXY", "DEVEX", "MG"]  # list
for team in groups:
    print(f"the team: {team}")

# constructor
result = list("Hello world")
print(f"the letter {result} and size: {len(result)}")

print("---------------")
fruits = ["apple", "orange", "lemon", "kiwi"]
a = fruits[0]
b = fruits[0:2]   # [0,1)
c = fruits[::3]  # : brinchi qiymat degani 3 3 qadam sakra degani
d = fruits[::-1]  # teskari holatda chiqarbberadi

print("a:", a)
print("b:", b)
print("c:", c)


print("======= List methods =======")
# methods > append() insert() pop() remove() clear() sort() index()

letters = ["a", "d", "b"]

letters.append("c")  # listni oxridan element qoshadi
print(f"the append result: {letters}")

letters.insert(0, "z")
print(f"the insert result: {letters}")

size = len(letters) - 1
result1 = letters.pop(size)  # oxrida ayridi
print(f"the pop result1: {result1} and letters: {letters}")

result2 = letters.pop(0)  # oldidan qirqib beradi
print(f"the pop result2: {result2} and the letters: {letters}")

print("-----------------")
animals = ["dog", "cat", "capybara", "fish", "lion"]
print("animals:", animals)

animals.remove("lion")  # remove qb beradi
print("animals remove:", animals)

del animals[2:4]
print("animals delete:", animals)

exist = animals.index("cat")  # borligini tekshradi
print("cat exist", exist)

animals.clear()
print("animal clear:", animals)

if "cat" in animals:
    print("index of cat: ", animals.index("cat"))
else:
    print("cat does not exist")

print("-----------")
numbers = [2, 20, 12, 8, 57]
numbers.sort()
print("numbers:", numbers)
numbers.sort(reverse=True)
print("sort reverse:", numbers)


# immutable sorted function
numbs = [2, 20, 12, 100]
new_numbs = sorted(numbs)
print(f"the sorted numbs: {numbs} and new_numbs: {new_numbs}")


print("======= Lambada function ======")
# Lambda is small anonymous function
def calculate(x, y): return x*y


resultt = calculate(3, 5)
print("result:", resultt)

peoplee = [
    ("Robert", 20),
    ("Steve", 19),
    ("Joseph", 25),
    ("Michael", 30)
]
peoplee.sort()
print("peoplee", peoplee)

# sorted by age via lambda
peoplee.sort(key=lambda personn: personn[1])
print("people2", peoplee)

print("======= enumerate, map and filter =======")

# enumerate for index and .values
animals = ["dog", "cat", "fish"]  # list
for element in enumerate(animals):
    print("element:", element)

print("-------")
for (index, value) in enumerate(animals):
    print(f"the index: {index} and value {value}")


# similar in dictionary
car_obj = dict(brand="Ferrari", year=2025)  # dict \
resul = car_obj.items()  # key va valueni brga tuple qb beradi
for (key, value) in resul:
    print(f"the key {key} and value {value}")


print("---------")
# map
cars = [
    ("Ferrari", 78),
    ("Tayota", 87),
    ("Audi", 117),
    ("BMW", 109),
    ("Pogani", 33)
]

new_cars = []
for car in cars:
    new_cars.append(car[0])
print("new_car:", new_cars)

resultt1 = map(lambda car: car[0], cars)
print(f"the result: {resultt1} and type: {type(resultt1)}")

new_cars = list(resultt1)
print("new_cars(2)", new_cars)

print("-----------")
# filter
result_filter = filter(lambda car: car[1] > 80, cars)
print(f"the result_filter: {result_filter} and type: {type(result_filter)}")
print(list(result_filter))
