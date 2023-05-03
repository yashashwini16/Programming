def prime_num(n):
    if n>1:
        for i in range(2,int(n/2)+1):
            if n%i==0:
                print("it is not aprime number")
            break
        else:
           print("it is prime")
    else:
        print("it is not a prime")

n=int(input())
prime_num(n)