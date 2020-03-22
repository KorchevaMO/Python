#4. Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
#При этом английские числительные должны заменяться на русские.
#Новый блок строк должен записываться в новый текстовый файл.

with open('ftask4.txt', 'r+') as file:
    my_list = list()
    for line in file.readlines():
        my_list.extend(line.split(' '))
print(my_list)
rusmy_list = ["Один", "Два", "Три", "Четыре"]
j = 0
for i in range(0, len(my_list), 3):
    my_list[i] = rusmy_list[j]
    j += 1

print(my_list)
out_f = open('ftask4.txt', 'w')
out_f.writelines(my_list)
out_f.close()