def CalculatePower(N,X):
  P=1
  for i in range(1, X+1):
    P=P*N
  return P
 
N,X=2,3
print(CalculatePower(N,X))
N,X=3,4
print(CalculatePower(N,X))


#another method
print(pow(9,2))