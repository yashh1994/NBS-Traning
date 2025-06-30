from collections import defaultdict

def solve(a):
    a.sort()
    mx = max(a)
    mp = {}
    for n in a:
        mp[n] = True
    for nm in a:
        if nm not in mp:
            temp = nm+nm
            while nm<mx:
                if temp in mp:
                    mp[temp] = False
            
# def gcd(a,b):
#     if not a%b:
#         return b
#     return gcd(b,a%b)
#                 ``


# print(gcd(6292, 9152))