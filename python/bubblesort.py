arr = [34,66,24,55,34,56,3556,33,653,545,3]
n = len(arr)

for i in range(n - 1):
    swapped = False
    for j in range( n - i - 1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swapped = True
    if not swapped:
        break

print("sorted array:", arr)

'''
Go through the array, one value at a time.
For each value, compare the value with the next value.
If the value is higher than the next one, swap the values so that the highest value comes last.
Go through the array as many times as there are values in the array.

An inner loop that goes through the array and swaps values if the first value is higher than the next value.
This loop must loop through one less value each time it runs.
An outer loop that controls how many times the inner loop must run. 
For an array with n values, this outer loop must run n-1 times.
'''
