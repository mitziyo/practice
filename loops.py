'''
LOOP operators
(1) for
(1) break/else
(1) while
'''

print("======= for operator =======")
# Iterable objects > string dict tuple list range map filter

text = "MIT"
numbs = [10, 7, 3, 4]
car_obj = dict(brand="Ferrari", year="2025")
range_obj = range(5)

for letter in text:
    print(f"the letter: {letter}")

print("------------------")
for number in numbs:
    print(f"the number: {number}")

print("------------------")
for x in range_obj:
    print(f"the element: {x}")

print("------------------")
for key in car_obj:
    print(f"the key: {key} => value: {car_obj.get(key)}")

print("------------------")
for x in range(1, 20, 5):
    print(f"the x {x}")


print("======= break/else =======")
for x in range(1, 20, 5):
    print(f"the x: {x}")
    if x > 100:
        print("reached break")
        break
else:
    print("Excuted successfully")
