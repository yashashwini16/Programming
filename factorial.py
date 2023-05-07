def factorial(n):
    """This is a recursive function
    to find the factorial of an integer"""

    if n == 1 or n==0:
        return 1
    else:
        # recursive call to the function
        return (n * factorial(n-1))
num=3  
result=factorial(num)
print(result)
#to find factorial of a number