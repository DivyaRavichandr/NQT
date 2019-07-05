a = input()
b = input()
c = input()
d = input()
e = input()
m1=int(a)
m2=int(b)
m3=int(c)
m4=int(d)
m5=int(e)
sum=m1+m2+m3+m4+m5
percentage=(sum/500)*100
print(percentage)
if(percentage>=90):
  print("A")
elif(percentage>=80):
  print("B")
elif(percentage>=70):
  print("C")
elif(percentage>=60):
  print("D")    
else:
  print("F")   
