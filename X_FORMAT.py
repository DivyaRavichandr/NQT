def pattern(str1, len1): 
  if (len1%2!=0):
    print("INVALID")
  else:
    for i in range(0, len1):
      j = len1 -1 - i 
      for k in range(0, len1):
        if (k == i or k == j):
          print(str1[k],end=" ") 
        else: 
          print(end = " ") 
          
      print(" ")  
str1=input(" ")
len1=len(str1)
pattern(str1,len1)      
