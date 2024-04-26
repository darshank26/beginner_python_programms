input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  
my_list = [num for num in my_list]  

print(f'List {my_list}')

input_str = input("Enter key of the list separated by space: ")  

key_list = input_str.split()  
key_list = [num for num in key_list]  

print(f'Key List {key_list}')

check_my_list = 0
check_key_list = 0

if len(my_list) % 2 == 0:
    check_my_list = 1
    print("test list is proper")
else:
    print("provide test list with even number")

if len(key_list) % 2 == 0:
    check_key_list = 1
    print("key list is proper")
else:
    print("provide key list with even number")

res = []

if check_my_list == 1 and check_key_list == 1:
    for i in range(0,len(my_list),2):
        res.append({key_list[0] : my_list[i], key_list[1] : my_list[i+1]})   
        
        
print(f'Final list : {res}')     








