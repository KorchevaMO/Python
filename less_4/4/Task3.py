#Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
#Необходимо решить задание в одну строку.
#Подсказка: использовать функцию range() и генератор.
result = [random.randint(20, 240) for _ in range(10)]
tmp = [itm for itm in result if itm % 20 == 0 or itm % 21 == 0 ]
print(tmp)