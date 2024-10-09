arr = [10,8,5,2,1]

cur = arr[-1]

for i in range(len(arr)-2,-1,-1):
    t = arr[i]-cur
    cur = arr[i]
    arr[i] = t
print(arr)