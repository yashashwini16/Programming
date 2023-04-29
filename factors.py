def factors_ofnum(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i)

n=120
factors_ofnum(n)