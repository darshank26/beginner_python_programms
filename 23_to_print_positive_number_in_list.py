input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  
my_list = [int(num) for num in my_list]  

print(f'List {my_list}')

# 1. using iteration 

pos_list = []

for i in range(0,len(my_list)):
    if ( my_list[i] > 0  ):
        pos_list.append(my_list[i])

print(f'Positive list:  {pos_list}')