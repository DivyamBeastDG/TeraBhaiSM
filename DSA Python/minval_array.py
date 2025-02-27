"""Variable 'minVal' = array[0]
For each element in the array
    If current element < minVal
        minVal = current element
        
algo:
1.Create a variable 'minVal' and set it equal to the first value of the array.
2.Go through every element in the array.
3.If the current element has a lower value than 'minVal', update 'minVal' to this value.
4.After looking at all the elements in the array, the 'minVal' variable now contains the lowest value.
"""


arr = [4,76,3,56,4,446,35,76,56,4,2,0,]
minVal = arr[0]

for i in arr:
    if i < minVal:
        minVal = i

print("lowest value:", minVal)