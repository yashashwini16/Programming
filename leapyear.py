def leap_year(n):
    if(n%4==0 and n%100!=0 or n%400==0):
        print("it is leap year")
    else:
        print("it is not a leap year")

n=int(input())
leap_year(n)