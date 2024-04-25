start = int(input("Enter start number: "))

end  = int(input("Enter end number: "))

# 1. using iteration 

pos_list = []

for i in range(start,end+1):
    if i > 0:
        pos_list.append(i)
        
print(f'Positive list {pos_list}')