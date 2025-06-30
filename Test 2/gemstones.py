def gemstones(arr):
    total = 0
    for i in range(26):
        ocu = 0
        for s in arr:
            if chr(i+ord('a')) in s:
                ocu += 1
        if ocu == len(arr):
            total+=1
    return total