start = int(input("Enter start number: "))

end  = int(input("Enter end number: "))

# 1. using iteration 

neg_list = []

for i in range(start,end+1):
    if i < 0:
        neg_list.append(i)
        
print(f'Negative list {neg_list}')