def powerSum(X, N):

    def go(sm,st):
        print("Comming for: ",sm,' ',st)
        nonlocal ans 
        if sm == 0:
           ans += 1 
           return
        for i in range(st+1,len(arr)):
            if arr[i]<=sm:
                print("Got: ",arr[i])
                go(sm-arr[i],i)
            else:
                break

    limit = int(X**(1/N))+1
    ans = 0
    arr = []
    for i in range(1,limit):
        arr.append(i**N)
    print(arr)
    go(sm=X,st=-1)
    return ans




print(powerSum(100,3))