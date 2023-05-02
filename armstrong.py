def arm(n):
    b=len(str(n))
    s=n
    sum=0
    while n!=0:
        r=n%10
        sum=sum+(r**b)
        n=n//10
    if s==sum:
        print("it is armstrong number",sum)
    else:
        print("it is not armstrong number")

n=int(input())
arm(n)