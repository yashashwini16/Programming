n=int(input("enter a number:"))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum=sum+i
if(sum==n):
    print("it is a perfect number")
else:
    print("not a perfect number")

#Write a program to identify if the number is Perfect number or not