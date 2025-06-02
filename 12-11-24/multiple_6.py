n = 1
num = 6
li = []
while n < 100:
    eq = pow(5,n)+pow(8,n+1)+pow(13,n+2)
    if eq % num == 0:
        li.append(n)
    n+=1
print(li)  
print(pow(11,3))