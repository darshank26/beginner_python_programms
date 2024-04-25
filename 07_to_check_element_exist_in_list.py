input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  
my_list = [num for num in my_list]  

element = input("Enter elements to check check in above list : ")  

print(f'List you entered {my_list},')

if element in my_list:
    print(f'Elements {element} exists in list')
else:
    print(f'Elements {element} does not in list')


