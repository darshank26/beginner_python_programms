input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  
my_list = [num for num in my_list]  

# 1. using sets 

print(f'List {len(set(my_list))}')

# using iterations

input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  
my_list = [num for num in my_list]  

new_list = []
count = 0 
for item in my_list:
    if item not in new_list:
        count += 1
        new_list.append(item)
        
print(count)