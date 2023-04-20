def sumofN(n):
    sum=0
    while(n>0):
        sum=sum+n
        n=n-1
    return sum

n=16
print(sumofN(n))

#to print sum of first N natural numbers


#Write a program to find Sum of numbers in a given range
def sum(n1,n2):
    s=0
    for i in range(n1,n2+1):#range
        s=s+i
    print(s)

sum(2,6)