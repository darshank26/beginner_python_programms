input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  
my_list = [int(num) for num in my_list]  

print(f'List {my_list}')

repeated_list = []

for i in range(0,len(my_list)):
    k = i + 1 
    for j in range(k,len(my_list)):
        if(my_list[i] == my_list[j]) and my_list[i] not in repeated_list :
            repeated_list.append(my_list[i])
        
print(repeated_list)

