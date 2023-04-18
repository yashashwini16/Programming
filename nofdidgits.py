print("enter a digits:")
n=int(input())
count=0
while n>0:
    count=count+1
    n=n//10
print("the number of digits is",count)
