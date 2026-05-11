'''
OBJECTS
(1) What is object
(2) Iterable object & RANGE
(3) DICTIONARY
(4) Error handling system
'''


import array # package/module
import math # package
from math import ceil # bunda ceilni ozini qolga olamz

print("===== What is object =====")
# An object has state and method properties.
# Everything is object in Python!

print(type('Hello World'))
print(type(100))
print(type(True))          # bular classdan olingan instance
print(type(array))
print(type(math))

# Hamma objectlar maqsadli object hisoblanadi

# Paradigms > Functional Programming & OOP (object oriented programming)
# OOP 4 CONCEPTS > Abstraction | Encapsulation | Inheritance | Polimorphism

result1 = math.ceil(97.7) # CALL
print("result1:", result1)  

result2 = ceil(99.7)
print("result2:", result2)

