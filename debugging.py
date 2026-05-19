'''
Packages and debuggung
(1) Python Packages and Core packages
(2) Package manager & External Package
(3) Debugging
'''

from PIL import Image
import turtle
print("======= Python Packages and Core packages =======")
''' Python Packages/Modules: Core, File and External '''
#  Core Package > https://docs.python.org/3/library

# Core package
# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(1)
# t.circle(100)

# turtle.done()

my_file = open("material/message.txt", "r")
try:
    content = my_file.read()
    print("content:", content)
finally:
    my_file.close()

# with = contex manager
with open("material/message.txt", "r") as your_file:
    your_content = your_file.read()
    print("your_content:", your_content)
print("DONE")

print("======= Package manager & External Package =======")
# External packages https://pypi.org/
# Package manager pip/pipenv  bur orqali external packagelarni ornatish uchun ishlatiladi

with Image.open("material/nature.jpg") as img_obj:
    resized_img = img_obj.resize((200, 200))
    resized_img.show()
    resized_img.save("material/sample.png")


'''

import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Pizza with Turtle")

# Turtle setup
t = turtle.Turtle()
t.speed(1)

# Draw pizza base
t.penup()
t.goto(0, -150)
t.pendown()
t.color("orange")
t.begin_fill()
t.circle(150)
t.end_fill()

# Draw cheese layer
t.penup()
t.goto(0, -130)
t.pendown()
t.color("gold")
t.begin_fill()
t.circle(130)
t.end_fill()

# Pepperoni positions
pepperoni = [
    (-50, 50), (40, 60), (-70, -20),
    (60, -10), (0, 0), (-20, -70),
    (70, -70)
]

# Draw pepperoni
t.color("red")
for x, y in pepperoni:
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(20)
    t.end_fill()

# Slice lines
t.color("brown")
t.pensize(3)

for angle in [0, 60, 120]:
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.pendown()
    t.forward(150)

    t.penup()
    t.goto(0, 0)
    t.setheading(angle + 180)
    t.pendown()
    t.forward(150)

t.hideturtle()
turtle.done()
'''

print("======= Debugging =======")

#Define
def get_summary(*args):
    total_amount = 0
    for a in args:
        total_amount += a
    return total_amount # find the bug via debugging

test = 100
#Call
result = get_summary(1,2,3,4,5)
print("result:", result)