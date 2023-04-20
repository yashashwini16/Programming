def reverse(n):
    rev=0
    while(n>0):
        d=n%10
        rev=rev*10+d
        n=n//10
    return rev

n=1234
print(reverse(n))

#Write a program to reverse a given number