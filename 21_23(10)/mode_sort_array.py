ar = [1,1,1,2,2,2,2,3,4,5,5,5]

ar.sort()

count = 1
max_count = 0
li = []
current_val = ar[0]

for i in range(1, len(ar)):
    if ar[i] == ar[i-1]:
        count += 1
        
    if count > max_count:
        max_count = count
        li = [ar[i]]
    elif count == max_count:
        li.append(ar[i-1])
        
    if ar[i] != ar[i-1]:
        count = 1


# if count == max_count:
#     li.append(ar[-1])
# elif count > max_count:
#     max_count = count
#     li = [ar[-1]]

print(f"The max frequency is {max_count} and values are {li}")