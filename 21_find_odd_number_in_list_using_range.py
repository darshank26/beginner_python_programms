start = int(input("Enter start number: "))

end  = int(input("Enter end number: "))

# 1. using iteration 

odd_list = []

for i in range(start,end+1):
    if (i % 2 != 0):
        odd_list.append(i)
        
print(f'Odd list {odd_list}')