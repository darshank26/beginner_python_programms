from itertools import combinations_with_replacement 


input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  

my_list = [int(num) for num in my_list]  

comb = combinations_with_replacement(my_list, 2) 

for i in list(comb):
    print(i)    
