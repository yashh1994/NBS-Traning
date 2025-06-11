import math
import sys

def vedic(n):
    a = int(math.sqrt(n))  # nearest smaller perfect square root
    diff = n - (a * a)
    return a + (diff / (2.0 * a))  # Vedic approximation

def devi(actual, approx):
    return abs(actual - approx) / actual * 100

n = 100
i = 1
li = []
mp = {}
while i <= n:
    actual = math.sqrt(i)
    vedic_approx = vedic(i)
    d = devi(actual, vedic_approx)
    if d > 5:
        print("for ", i, "deviation is ",d)
        li.append((i,d))
        mp[i] = d
    i += 1
print("Size of li",sys.getsizeof(mp))
print("Size of mp",sys.getsizeof(li))





import math

def is_perfect_square(n):
    return int(math.sqrt(n))**2 == n

def print_square_diff_percentages(limit):
    last_perfect = 1  # Start with 1 as the first perfect square
    print(f"{'Range':<15} {'% Increase':<15}")
    print("-" * 30)

    for i in range(2, limit + 1):
        if is_perfect_square(i):
            percent = ((i - last_perfect) / last_perfect) * 100
            print(f"{last_perfect} to {i:<10} {percent:.2f}%")
            last_perfect = i

print_square_diff_percentages(100)


m = 2
n = 3

# m,n = int(input()),int(input())

li = [[0] * n for i in range(m)] 

ctn = 1
for i in range(m):
    for j in range(n):
        li[i][j] = ctn
        ctn += 1

print(li)
ctn = 1
for i in range(n):
    for j in range(m):
        li[j][i] = ctn
        ctn += 1


print(li)

