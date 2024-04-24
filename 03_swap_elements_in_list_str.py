# This programs will interchange first and last elements of list 

def reverse_str(x):
  return x[::-1]


input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  
my_list = [st for st in my_list]  

print(f'Before Swapping  {my_list}')

new_list = []

for i in range(0, len(my_list)):  
    new_list.append(reverse_str(my_list[i]))
    
print(f'After Swapping  {new_list}')
