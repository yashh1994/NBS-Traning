fun_calls = 0

def fun(arr, index1, index2, l, r, count):
    global fun_calls
    fun_calls += 1
    while index1 <= index2:
        if l < r:
            l += arr[index1]
            index1 += 1
            count += 1
        elif l > r:
            r += arr[index2]
            index2 -= 1
            count += 1
        else:
            if index1 == index2:
                return index1, True, count
            pivot, ans, count = fun(arr, index1 + 1, index2, l + arr[index1], r, count + 1)
            if ans:
                return pivot, True, count
            pivot, ans, count = fun(arr, index1, index2 - 1, l, r + arr[index2], count + 1)
            if ans:
                return pivot, True, count
            return -1, False, count

    return -1, False, count


arr = [1,2,3,3,2,1]
index1, index2 = 0, len(arr) - 1
l, r = 0, 0
count = 0

pivot, ans, count = fun(arr, index1, index2, l, r, count)
print(fun_calls)

# if ans:
#     print("Pivot index found at index:", pivot)
# else:
#     print("No pivot index found")
# print("Count is:", count)
