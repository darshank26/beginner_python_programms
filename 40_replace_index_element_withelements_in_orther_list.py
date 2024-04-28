import numpy as np

input_str = input("Enter elements of the list 1 separated by space: ")  

my_list = input_str.split()  

my_list = [(num) for num in my_list]  

print(f'List 1 {my_list}')

input_str_2 = input("Enter elements of the list 2 separated by space: ")  

other_list = input_str_2.split()  

other_list = [int(num) for num in other_list]  

print(f'List 2 {other_list}')

res = np.take(my_list,other_list)

print(res)