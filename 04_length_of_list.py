# This programs will interchange first and last elements of list 

input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  
my_list = [st for st in my_list]  

print(f'So this {my_list} has {len(my_list) }')


