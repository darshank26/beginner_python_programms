input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  
my_list = [int(num) for num in my_list]  

print(f'List {my_list}')

# 1. using iteration 

pos_count = 0
neg_count = 0 

for i in range(0,len(my_list)):
    if (  my_list[i] > 0 ):
        pos_count += 1 
    else:
        neg_count += 1 


print(f'Positive count: {pos_count}, Negative count: {neg_count}')