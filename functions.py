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
