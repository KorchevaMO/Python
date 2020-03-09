my_str = input('Введите список через , :')
my_list = list(my_str)
i = 0
for i in range(int(len(my_list)/2)):
  my_list[i], my_list[i+1] =  my_list[i+1], my_list[i]
   i += 2
print(my_list)

