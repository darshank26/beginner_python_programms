from itertools import permutations 


input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  

my_list = [int(num) for num in my_list]  

comb = permutations(my_list, len(my_list)) 

for i in comb:
    print(i)