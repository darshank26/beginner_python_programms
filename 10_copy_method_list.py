import copy as cp 

input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  
my_list = [num for num in my_list]  

print(f'List {my_list}')

# 1. using assignment operator

new_list = my_list

print(f'Original List {my_list}')
print(f'After List {new_list}')

# 2. using copy method 

input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  
my_list = [num for num in my_list] 

print(f'List {my_list}')


new_list = cp.copy(my_list)

print(f'Original List {my_list}')
print(f'After List {new_list}')

