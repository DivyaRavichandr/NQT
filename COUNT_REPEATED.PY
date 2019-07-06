chars="abcdefghijklmnopqrstuvwxyz"
string=input(" ")
for char in chars:
  count=string.count(char)
if count>1:
  print(char,count)
else:
  print("DOES NOT EXIST")  
