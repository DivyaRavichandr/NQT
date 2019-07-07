string=input(" ")
result = []
for i in string:
    if i not in result:
        result.append(i)
result = ''.join(result)
print(result)
