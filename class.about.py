'''
CLASS
(1) What is class
(2) Ordinary vs static properties
(3) Special methods
'''

print("===== What is class =====")
# class - blueprint for object creation!
# structures > state constructor method


class Person():
    # state
    message = "class state property"

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def introduce(self):
        print(f"{self.name} says: How do you do!")

    def say_age(self):
        print(f"{self.name} says I am {self.age}")

    # class decoretorlar bn static method yasaymz
    @classmethod
    def explain(cls):
        print("static method property excuted!")


person1 = Person("Khan", 25)
person2 = Person("Martin", 35)
person3 = Person("John", 22)

# ordinary state property
print("person1.name:", person1.name)

# orfinary method
person1.introduce()
person2.say_age()


print("===== Ordinary and static properties =====")
# static state
new_message = Person.message
print("new_message:", new_message)
# static method
Person.explain()
