#Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
#Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
file_name = input('Название файла: ')
f = open(file_name,'w')
while True:
    s = input()
    if s == '': break


with open(file_name, 'r') as ans:
  result = sum(map(int, ans))
print(result)
out_f = open(file_name, 'w')
out_f.write(result)
out_f.close()
