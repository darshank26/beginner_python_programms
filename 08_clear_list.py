input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  
my_list = [num for num in my_list]  

print(f'List {my_list}')

# 1. Method one using clear function

my_list.clear()


print(f'After clear method {my_list}')

# 2. Reinitilizing the list 


input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  
my_list = [num for num in my_list]  

print(f'List {my_list}')

my_list = []

print(f'After Re initializing method {my_list}')

# 3. using *= 0 method 


input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  
my_list = [num for num in my_list]  

print(f'List {my_list}')

my_list *= 0

print(f'Using *=0 method {my_list}')

# 4. using del method


input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  
my_list = [num for num in my_list]  

print(f'List {my_list}')

del my_list[:]

print(f'Using del method {my_list}')

# 5. using pop method

input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  
my_list = [num for num in my_list]  

print(f'List {my_list}')


while (len(my_list) != 0):
    my_list.pop()
    
print(f'Using pop method {my_list}')
