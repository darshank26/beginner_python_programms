# This programs will interchange first and last elements of list 

input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  
my_list = [int(num) for num in my_list]  

pos_1 = input("Enter position 1 : ")  

pos_2 = input("Enter position 2 : ")  

print(f'Before Swapping list {my_list}')

temp1 = my_list[int(pos_1)-1]

temp2 = my_list[int(pos_2)-1]

my_list[int(pos_1)-1] = temp2

my_list[int(pos_2)-1] = temp1


print(f'After Swapping list {my_list}')
