def alpha(c):
    if(c>='a' and c<='z' ):
        print("it is alphabet")
    elif(c>='A' and c<='Z'):
        print("it is alphabet")
    else:
        print("it is not alphabet")

print("enter a character:")
c=input()
alpha(c)