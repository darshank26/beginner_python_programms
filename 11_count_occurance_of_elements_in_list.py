input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  
my_list = [num for num in my_list]  

print(f'List {my_list}')

elements = input("Enter elements to find its occurrance: ")  

# 1. using iteration 

count= 0

for i in my_list:
    if(i == elements):
        count = count + 1 
        
        
print(f'{elements}, comes in list for {count} times')

# 2. using count method 

input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  
my_list = [num for num in my_list]  

print(f'List {my_list}')

elements = input("Enter elements to find its occurrance: ")  
x = my_list.count(elements)

print(f'{elements}, comes in list for {x} times')
