def leastcommon(x,y):
    if x>y:
        g=x
    else:
        g=y
    while(True):
        if(g%x==0 and g%y==0):
            lcm= g
            break
        g=g+1
    return lcm

x=54
y=24
print(leastcommon(x,y))
#Write a program to find LCM of two number