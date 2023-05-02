def lar_three(a,b,c):
    if a>b and a>c:
        print(a,"is greater")
    elif b>c and b>a:
        print(b,"is greater")
    else:
        print(c,"is greater")
    
a=int(input())
b=int(input())
c=int(input())
lar_three(a,b,c)