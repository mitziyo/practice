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
