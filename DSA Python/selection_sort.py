arr = [34,66,24,55,34,56,3556,33,653,545,3]
n = len(arr)

for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i] #improved way cuz shifting takes a lot of time like in the manual way below
    #manual way    
    #min_val = arr.pop(min_index)
    #arr.insert(i, min_val)

print("Sortedd array:", arr)

'''Go through the array to find the lowest value.
Move the lowest value to the front of the unsorted part of the array.
Go through the array again as many times as there are values in the array.
An inner loop that goes through the array, finds the lowest value, and moves it to the front of the array. 
This loop must loop through one less value each time it runs.
For an array with n values, this outer loop must run n-1 times.
'''
