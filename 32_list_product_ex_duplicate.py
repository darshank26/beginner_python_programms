input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  
my_list = [num for num in my_list]  

# 1. using sets 

new_list = list(set(my_list))

print(f'List {new_list}')

mul = 1 
for i in range(0,len(new_list)):
    mul = mul * int(new_list[i])

print(mul)

