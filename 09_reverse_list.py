input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  
my_list = [num for num in my_list]  

print(f'List {my_list}')

# 1. using reverse method 

my_list.reverse()
print(f'Reverse list {my_list}')

# 2. using slicing 

input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  
my_list = [num for num in my_list]  

print(f'List {my_list}')

def reverse_list(temp_list):
    new_list = my_list[::-1]
    return new_list

print(f'List after reverse {reverse_list(my_list)}')



