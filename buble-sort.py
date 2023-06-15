arr = [64, 34, 25, 12, 22, 11, 90]
print(arr)

for j in range(len(arr)):
    for i in range(len(arr)-1-j):
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1], arr[i]
    print(j)

print(arr)
    

