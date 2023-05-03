def palin(n):
    s=n
    r=0
    while(n>0):
        d=n%10
        r=r*10+d
        n=n//10
    if r==s:
        print("it is palindrome")
    else:
        print("it is not palindrome")

n=int(input())
palin(n)
#program to find palindrome