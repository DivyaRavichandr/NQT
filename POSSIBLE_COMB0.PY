def arrs(arr, n, sum): 
      
    count = 0  
    for i in range(0, n): 
        for j in range(i + 1, n): 
            if arr[i] + arr[j] == sum: 
                count += 1
      
    return count 
  
# Driver function  
size=int(input("enter array size: "))
arr=[]
for i in range(0,size):
  x=int(input(" "))
  arr.append(x)
n=len(arr)
sum1=int(input(" enter sum value: "))
print(arrs(arr,n,sum1))  
