input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  
my_list = [int(num) for num in my_list]  

print(f'List {my_list}')

# 1. using iteration method 

mul = 1

for i in range(0,len(my_list)):
    mul = mul * my_list[i]

print(f'After multiplication {mul}')
    
