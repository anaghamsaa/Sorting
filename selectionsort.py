#time complexity O(n^2)

def for_min(arr,j,n):
    min_index=j    
    for k in range(j,n):     
        if ( arr[min_index] > arr[k]):
            min_index=k    
    return min_index

def  swap(arr,min_index,i):
    t=arr[min_index]
    arr[min_index]=arr[i]
    arr[i]=t
    #return arr


print (" SelectionSort using Python")
n=int(input("Enter limit:"))
arr = []
for i in range(n):
    arr.append(int(input("Enter element")))


for i in range(n):
    min_index=for_min(arr,i,n)
    swap(arr,min_index,i)

for k in range(n):
    print(arr[k])