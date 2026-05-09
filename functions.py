'''
FUNCTIONS
(1) DEFINE vs CALL
(2) Parametr va Argument
(3) Keyword & default arguments
(4) Scope
'''

print("===== DEFINE vs CALL ======")
# build un function > print() type()
# Function - reusable block of code!
# Instead of block {} in JAVA, Python uses indentation!

# Define - build - parametr
# def greet(a):
#     print(f"How do you do, {a}")


# # CALL - execute
# greet('Martin')


def greet(a):
    print(f"How do you do, {a}")


# CALL - execute - argument
result3 = greet('Martin')
print("result3: ", result3)


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"


result4 = greeting("Justin")
print("result4", result4)

print("===== Keyword & default arguments ======")

# Define


def give_greet(name, age=22):
    print("give_greet is exexuted")
    return f"Hi {name}, you are {age} years old!"


# Call
result5 = give_greet(name="Justin", age=28)
print("result5: ", result5)

result6 = give_greet("John")
print("result6: ", result6)
