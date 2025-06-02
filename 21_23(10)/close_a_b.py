num1 = 17
num2 = 10

limit1 = 77
limit2 = 1000

a = 1
b = 1
ans_a = -1
ans_b = -1
ans = 1000
while a<=limit1 and b <= limit2:
    if ans > abs(pow(num1, a)-pow(num2,b))/pow(num2,b)*100:
        ans = abs(pow(num1, a)-pow(num2,b))/pow(num2,b)*100
        ans_a = a
        ans_b = b
    if pow(num1,a) < pow(num2,b):
        a += 1
    else:
        b += 1
        
print(f"For the Nums: {num1} With {ans_a}, {num2} With {ans_b}")
print(f"The Closest Diff is {ans}")
print(f"a is {pow(num1,ans_a)} b is {pow(num2,ans_b)}")