N=int(input(" "))
list1=[]
for i in range(N):
  x=int(input(" "))
  list1.append(x)
print(list1)
maxpos=list1.index(max(list1))
print(maxpos)
