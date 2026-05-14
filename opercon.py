'''
OPERATOR va CONDITIONS
(1) Operators
(2) Conditions
(3) Logical Operators
'''


print("======= Operators =======")
# + - > >= < <= * /    // % += -= **

a = 19
b = 5

print("a > b", a > b)
print("a / b", a / b)
print("a * b", a * b)

print("-----------------")

result = a // b
left = a % b
print(f"the result: {result} and left: {left}")

print("-----------------")

# a = a + 100
a += 100
print("a:", a)

print("b**2", b**2)
print("b**3", b**3)

print("="*10)

c = dict(name="Martin", age=35)
d = dict(name="Martin", age=35)

print("c==d", c == d)  # only values not reference
print(id(c), id(d))
e = c

print("c is d", c is d)
print("c is e", c is e)

# valueni tekshrish uchun == / reference uchun esa is


print("======= Conditions =======")
# conditions Truthy and falsyni tekshradi har doim
x = 5

if x > 50:
    print("case A")
elif x > 10:
    print("case B")
else:
    print("case C")


print("======= Logical operators =======")

print("-----------------")
age = 18
# person = None

# if age > 16:
#     person = "adult"
# else:
#     person = "child"

# print("person:", person)

# Ternary operator
person = "adult" if age > 18 else "minor"
print("person:", person)

print("-----------------")

is_student = True
is_admin = False
is_guest = True
is_parent = True

if not is_student:
    print("Welcome here, do you want to be student")
elif is_admin:
    print("Please go to the office")
elif is_guest or is_parent:
    print("waiting room is over there")
else:
    print("Other case")