some_list = ['a', 'b', 'c', 'd', 'd', 'e', 'f', 'g']

duplicates = []
for value in some_list: #for every value in this list 
    if some_list.count(value) > 1: #if this value  appears more than once
        if value not in duplicates: #and if we've not already placed it in the duplicates list
            duplicates.append(value) #add this value to the duplicates list 

print(duplicates)