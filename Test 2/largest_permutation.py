def largestPermutation(k, arr):
    sort = sorted(arr,reverse=True)
    print("Sorted: ",sort)
    mp = {}
    for i in range(len(arr)):
        mp[arr[i]] = i
    print(mp)
    for i in range(len(arr)):
        if arr[i] != sort[i] and k:
            arr_i = mp[arr[i]]
            sor_i = mp[sort[i]]
            old = arr[i]
            arr[i],arr[mp[sort[i]]] = arr[mp[sort[i]]], arr[i]
            mp[arr[i]] = arr_i
            mp[old] = sor_i
            k -= 1
        if not k:
            break
    return arr