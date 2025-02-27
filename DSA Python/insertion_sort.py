arr = [34,66,24,55,34,56,3556,33,653,545,3]
n = len(arr)

for i in range(1, n):
    insert_index = i
    current_value = arr.pop(i)
    for j in range(i-1, -1, -1):
        if arr[j] > current_value:
            insert_index = j
    arr.insert(insert_index, current_value)  #this is slow becuz of shifting......

print("sorted array:", arr)




#improved
arr = [34,66,24,55,34,56,3556,33,653,545,3]
n = len(arr)

for i in range(1, n):
    insert_index = i
    current_value = arr[i]  #copies the element ie. less shifting
    for j in range(i-1, -1, -1):
        if arr[j] > current_value:
            arr[j+1] = arr[j]
            insert_index = j
        else:
            break

    arr[insert_index] = current_value

print(arr)