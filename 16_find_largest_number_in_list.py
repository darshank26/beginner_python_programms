input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  
my_list = [int(num) for num in my_list]  

print(f'List {my_list}')

# 1. using sort method 

my_list.sort()

print(f'Largest number {my_list[(len(my_list)-1)]}')

# 2. using min method 

input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  
my_list = [int(num) for num in my_list]  

print(f'List {my_list}')

print(f'Largest number {max(my_list)}')

 # 3. using iteration 
 
 
input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  
my_list = [int(num) for num in my_list]  

print(f'List {my_list}')

min = my_list[0]

for i in range(0,len(my_list)):
    if  my_list[i] > min:
        min = my_list[i]
        
print(f'Largest number {min}')

    


