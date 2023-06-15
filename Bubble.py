def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Ostatnie i elementów są już na swoim miejscu
        for j in range(0, n-i-1):
            # Porównujemy każde dwa kolejne elementy
            if arr[j] > arr[j+1] :
                # Zamieniamy miejscami, jeśli nie są w dobrej kolejności
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # print(arr[j], arr[j+1], arr[j+1],arr[j])

    return arr

# print(bubble_sort([4,8,2,3,9]))

