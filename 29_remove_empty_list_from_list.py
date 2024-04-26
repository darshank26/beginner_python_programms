my_list = [1,2,3,[],1,4,5,[],[],123, [1,23], []]

while [] in my_list:
    my_list.remove([])
        
print(my_list)