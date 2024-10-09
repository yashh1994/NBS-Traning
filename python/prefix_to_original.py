arr = [0, 1, 3, 6, 10, 15]



if __name__ == "__main__":
    cur = arr[0]
    for i in range(1,len(arr)):
        t = arr[i]-cur
        cur = arr[i]
        arr[i] = t
    print(arr)
