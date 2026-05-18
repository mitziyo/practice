'''
Array and set
(1) Array 
(2) Set
(3) Specific operators with set
'''

print("======= Array =======")

from array import array

# sonlar ketma ketligi katta hajmga ega bolsa misol mingta: array ishlatiladi
numbers = array("i", [1, 4, 5, 7, 8, 41])
# arrayda faqat br hil turdagi typeda boladi # i , f

print("numbers(1):", numbers)

numbers.append(100)
numbers.insert(0, 14)
print("numbers(2)", numbers)

numbers.remove(5)
numbers.pop()
print("numbers(3)", numbers)

del numbers[0:2] 
print("numbers(4)", numbers)
