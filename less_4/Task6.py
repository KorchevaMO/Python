#Реализовать два небольших скрипта:
#а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
#б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
#Подсказка: использовать функцию count() и cycle() модуля itertools.
#1
from itertools import count

for a in count(0):
    if a > 20:
        break
    else:
        print(a)


#2

from itertools import cycle

polys = ['triangle', 'square', 'pentagon', 'rectangle']
iterator = cycle(polys)

print(next(iterator))  # triangle
print(next(iterator))  # square
print(next(iterator))  # pentagon
print(next(iterator))  # rectangle
print(next(iterator))  # triangle
print(next(iterator))  # square