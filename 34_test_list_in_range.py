input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  
my_list = [int(num) for num in my_list]  


new_list  = []

new_list = sorted(my_list)

print(new_list)

a,b = new_list[0], new_list[((len(my_list)-1))]+ 1
r = True

for i in my_list:
    if i < a or i >= b:
        r = False
        break
    
print(f'Contain call list in range {r}')