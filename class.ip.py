'''
CLASS deep diving
(1) ENCAPSULATION
(2) INHERITENCE <
(3) POLIMORPHISM <
'''

print("======= INHERITANCE =======")
# Parent > child
# Parnt only provides public and protected properties to children


class Animal:
    description = "the class is parent for animals"

    def __init__(self, voice):
        self.status = "animal is alive"
        self.voice = voice

    def make_voice(self):
        print(f"the animal can make voice {self.voice}")


class Dog(Animal):  # child

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}--{self.sound}")

    def protect(self):
        print("Yes, I can protect you!")

    def make_voice(self):
        print(f"the {self.name} says {self.sound}")


class Cat(Animal):  # child

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}--{self.sound}")

    def play(self):
        print("Yes, I can play you!")


class Fish(Animal):  # child

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}--{self.sound}")

    def swim(self):
        print("Yes, I can swim!")


dog = Dog("Rex", "Wow", True)
cat = Cat("Tom", "Myew", True)
fish = Fish("Nemo", "ZZZ", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("------------")

dog.make_voice()
fish.make_voice()

print("-------------")
print(Animal.description)
print(Dog.description)

print(dog.voice, fish.voice)
print("status:", dog.status)
print("status:", cat.status)


print("======= Polimorphism =======")
dog.make_voice()
fish.make_voice()

print("------------")
# fish > Fish > Animal > object
a = isinstance(fish, Fish)
b = isinstance(fish, Animal)
c = isinstance(fish, object)
d = isinstance("MIT", object)
result = a and b and c and d
print(f"the result: {result}")


# Fish > Animal > object
data1 = issubclass(Fish, Animal)
data2 = issubclass(Animal, object)
print("data:", data1, data2)
