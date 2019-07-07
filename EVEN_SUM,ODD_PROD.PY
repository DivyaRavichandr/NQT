import numpy
N=int(input())
arr=[]
for i in range(N):
  x=int(input())
  arr.append(x)
print(arr) 
sum1=sum(arr)
product=numpy.prod(arr)
if (sum1%2==0):
  print(sum1)
else:
  print(product)
