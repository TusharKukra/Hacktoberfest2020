def bubblesort(arr,n):

    for i in range(n):

        for j in range(0,n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr


arr=[1,9,0,8,6]
print(bubblesort(arr,len(arr)))
