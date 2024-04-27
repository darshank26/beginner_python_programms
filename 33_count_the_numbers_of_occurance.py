input_str = input("Enter elements of the list separated by space: ")  

my_list = input_str.split()  
my_list = [int(num) for num in my_list]  

k = int(input("Enter the number of occurance of the elements ") )

res = []

for i in my_list:
    freq = my_list.count(i)
    if freq >= k and i not in res:
        res.append(i)

print(res)



