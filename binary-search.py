listy = [1,2,3,4,5,6,7,8]

def binary_search(my_list, item):
    low = 0
    high = len(my_list)-1

    while low <= high:  
        mid = (low + high)//2
        guess = my_list[mid] 

        print('low',low, 'high', high, 'mid', mid, 'guess',guess)
        if guess == item:
            return mid 
        if guess > item:
            high = mid -1
        else:
            low = mid +1
        
    
    return None
    

print(binary_search(listy, 7))