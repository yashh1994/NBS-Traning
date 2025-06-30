def quickSort(arr):
    pivot = arr[0]
    l,e,r = [],[],[]
    for a in arr:
        if a<pivot:
            l.append(a)
        elif a>pivot:
            r.append(a)
        else:
            e.append(a)
    return l+e+r