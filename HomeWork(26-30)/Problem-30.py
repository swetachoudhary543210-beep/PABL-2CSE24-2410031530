def row_with_max_ones(arr):
    max_count = 0
    index = -1
    
    for i in range(len(arr)):
        count = sum(arr[i])
        if count > max_count:
            max_count = count
            index = i
    
    return index

arr = eval(input())
print(row_with_max_ones(arr))
