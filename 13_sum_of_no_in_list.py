input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  
my_list = [int(num) for num in my_list]  

print(f'List {my_list}')

# 1. using iteration method 

new_add_list = []

for i in range(0,len(my_list)):
    sum = 0
    for j in str(my_list[i]):
        sum = sum + int(j)
    new_add_list.append(sum)

print(f'Addition of elements in list {new_add_list}')
    
