input_str_1 = input("Enter elements of the list 1 separated by space: ")  

my_list_1 = input_str_1.split()  

my_list_1 = [(num) for num in my_list_1]  

input_str_2 = input("Enter elements of the list 2 separated by space: ")  

my_list_2 = input_str_2.split()  

my_list_2 = [(num) for num in my_list_2]  

unique = []
for i in range(len(my_list_1)):
    for j in range(len(my_list_2)):
          unique.append((my_list_1[i],my_list_2[j]))
          
print(f'Unique combination {unique}')
