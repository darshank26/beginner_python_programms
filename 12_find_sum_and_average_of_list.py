input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  
my_list = [int(num) for num in my_list]  

print(f'List {my_list}')

# 1. using sum() method

ans = sum(my_list)

avg = ans / len(my_list)


print(f'Sum of list {ans}')

print(f'Average of list {avg}')

# 2. using iteration 

input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  
my_list = [int(num) for num in my_list]  

print(f'List {my_list}')

ans = 0 
for i in range(0,len(my_list)):
    ans = ans + my_list[i]

print(f'Sum of list {ans}')

print(f'Average of list {ans/len(my_list)}')

