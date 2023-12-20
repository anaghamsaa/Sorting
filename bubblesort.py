#time complexity O(n^2)

print (" BubbleSort using python")

n=int(input("Enter limit:"))
arr = []
for i in range(n):
    arr.append(input("Enter element"))


for i in range(n-2):    
    for j in range(i,n-1):
        print(i,j)
        if(arr[j]>arr[j+1]):
            t=arr[j+1]
            arr[j+1]=arr[j]
            arr[j]=t
           
        
for k in range(n):
    print(arr[k])