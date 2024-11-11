a = 1
b = 1
ans_a = -1
ans_b = -1
ans = 1000
while a<=1000 and b <= 1000:
    if ans > abs(pow(2, a)-pow(10,b))/pow(10,b)*100:
        ans = abs(pow(2, a)-pow(10,b))/pow(10,b)*100
        ans_a = a
        ans_b = b
    if pow(2,a) < pow(10,b):
        a += 1
    else:
        b += 1
print(f"The Closest Diff is {ans} and value of a is {ans_a} and b is {ans_b}")
print(f"a is {pow(2,ans_a)} b is {pow(10,ans_b)}")