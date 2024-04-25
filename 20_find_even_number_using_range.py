start = int(input("Enter start number: "))

end  = int(input("Enter end number: "))

# 1. using iteration 

even_list = []

for i in range(start,end,2):
    even_list.append(i)

print(f'Even list {even_list}')