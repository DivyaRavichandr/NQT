string=input(" ")
N=int(input(" "))
count=0
for i in string:
  count=count+1
new=string[0:N]+string[count-N:count]
print(new)
