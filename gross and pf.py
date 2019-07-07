name=input(" ")
sal=float(input(" "))
HRA=float(input(" "))
DA=float(input(" "))
a=sal+DA
PF=a*0.12
GS=sal+HRA+DA-PF

print("Name :" , name)
print("BASIC : ", sal)
print("HRA : ",HRA)
print("DA : " ,DA)
print("PF : " ,PF)
print("GROSS SALARY :",GS)
