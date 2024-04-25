input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  
my_list = [int(num) for num in my_list]  

print(f'List {my_list}')

# 1. using sort method 

my_list.sort()

print(f'Largest number {my_list[(len(my_list)-2)]}')


    


