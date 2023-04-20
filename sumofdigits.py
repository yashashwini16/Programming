def sumofdigits(n):
    sum=0
    while(n!=0):
        sum=sum+(n%10)
        n=n//10
    return sum
n=123
print("sum is:" ,sumofdigits(n))

