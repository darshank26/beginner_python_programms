input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  
my_list = [int(num) for num in my_list]  

print(f'List {my_list}')

# 1. using iteration 

even_count = 0
odd_count = 0 

for i in range(0,len(my_list)):
    if ( ( my_list[i] % 2 ) == 0 ):
        even_count += 1 
    else:
        odd_count += 1 


print(f'Even count: {even_count}, Odd count: {odd_count}')