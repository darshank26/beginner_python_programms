input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  

my_list = [int(num) for num in my_list]  

count = 0 

final_list = []

print(my_list)

for i in range(0,len(my_list)-1):
    if(my_list[i] == my_list[i+1]):
        count += 1
        if(count>=3):
            final_list.append(my_list[i])

print(final_list)