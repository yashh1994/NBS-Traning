def main():
    ar = [1,2,3,4,5]
    i = 0
    while i < len(ar)-1:
        if ar[i] != ar[i+1]:
            flag = ar[i] < ar[i+1]
            break
        i += 1
    while i < len(ar)-1:
        if ar[i] != ar[i+1] and flag != (ar[i] < ar[i+1]):
            print("not")
            return
        i += 1
    print("OK")
main()


