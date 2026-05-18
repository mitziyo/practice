'''
Array and set
(1) Array 
(2) Set
(3) Specific operators with set
'''

from array import array
print("======= Array =======")


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

print("======= Set =======")
# set of unique collection without keepeing order!
# set orqali array qurilganda ichidagi takroriy raqamlarni  qabul qlmaydi
# {set} da index ketma ketlik degan tushuncha yoq

new_numbers = array("i", [1, 4, 5, 7, 4, 7, 3, 3, 3, 3, 5, 7, 8, 41])
numbs_set = set(new_numbers)

print(f"the numbs_set: {numbs_set} and type: {type(numbs_set)}")

numbs_set.add(200)
print("numbs_set(1):", numbs_set)

numbs_set.add(7)
print("numbs_set(2):", numbs_set)

print("======= Specific operators with set =======")

# | & - ^

a = {10, 20, 50}
b = {20, 40}

result1 = a | b  # union  bir xillarni olmasdan a va b toplamni olib beradi
print("result1", result1)

result2 = a & b  # intersection faqat ikkovida ham bor qiymatni olib beradi
print("result2", result2)

result3 = a - b  # difference a dan b dagi bor qiymatni ayrb tashlaydi
print("result3", result3)

result4 = a ^ b  # simmetric difference ikkovida ham qatnashmaganni obberadi
print("result4", result4)
