#usinf for loop

prev2 = 0
prev1 = 1
print(prev2)
print(prev1)

for i in range(18):
    newfib = prev1 + prev2
    print(newfib)
    prev2 = prev1
    prev1 = newfib 


#using recursion

count = 2
print(0)
print(1)
def fibonacci(prev1, prev2):
    global count
    if count<=18:
        newfib = prev2 + prev1
        print(newfib)
        prev2 = prev1
        prev1 = newfib
        count += 1
        fibonacci(prev1, prev2)
    else:
        return

fibonacci(0, 1)

""" finding the nth fibbonacci no. ie. F(n) = F(n-1)+F(n-2)"""

def F(n):
    if n<=1:
        return n
    else:
        return F(n - 1) + F(n - 2)

print(F(19))     


