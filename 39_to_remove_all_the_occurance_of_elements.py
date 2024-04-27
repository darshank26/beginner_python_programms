input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  

my_list = [int(num) for num in my_list]  

k = int(input("Enter element to remove ")) 

final_list = []

for i in range(0,len(my_list)):
    if my_list[i] != k:
        final_list.append(my_list[i])

print(final_list)