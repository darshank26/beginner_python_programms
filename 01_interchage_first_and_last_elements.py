# This programs will interchange first and last elements of list 

input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  
my_list = [int(num) for num in my_list]  

print(f'Before Swapping list {my_list}')

temp = my_list[0]

new_list = my_list

new_list[0] = my_list[len(my_list) - 1]

new_list[len(my_list) - 1] = temp

print(f'After Swapping list {new_list}')
