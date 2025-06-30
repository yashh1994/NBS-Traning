# def biggerIsGreater(w): 
#     new_s = []
#     for c in w:
#         new_s.append(c)
#     if len(w) == 1:
#         return "no answer"
#     i = len(w)-2
#     n = len(w)
#     while i>=0 and w[i]>w[i+1]:
#         i -= 1
#     print("i: ",i)
#     if i == -1:
#         return "no answer"
#     j = n-1
#     while w[j]<w[i] and j>i:
#         print("comparing: ",w[i],' ',w[j])
#         j -= 1
#     print("j: ",j)
#     if j!=i:
#         new_s[i],new_s[j] = new_s[j],new_s[i]
#         print("Befor: ",new_s)
#         new_s  = new_s[:i+1]+new_s[i+1:][::-1]
#     else:
#         print("wtf: ",w)
#         return ""
#     ans = "".join(new_s)
#     return ans if w != ans else "no answer"

# print(biggerIsGreater("rtglgzzqxnuflitnlyit"))
 
#!/bin/python3

import math
import os
import random
import re
import sys

def biggerIsGreater(w): 
    new_s = []
    for c in w:
        new_s.append(c)
    if len(w) == 1:
        return "no answer"
    i = len(w)-2
    n = len(w)
    while i>=0 and w[i]>=w[i+1]:
        i -= 1
    # print("i: ",i)
    if i == -1:
        return "no answer"
    j = n-1
    while w[j]<=w[i] and j>i:
        # print("comparing: ",w[i],' ',w[j])
        j -= 1
    # print("j: ",j)
    if j!=i:
        new_s[i],new_s[j] = new_s[j],new_s[i]
        # print("Befor: ",new_s)
        new_s  = new_s[:i+1]+new_s[i+1:][::-1]
    else:
        # print("wtf: ",w)
        return "no answer"
    ans = "".join(new_s)
    return ans if w != ans else "no answer"
    
if __name__ == "__main__":
    # m = int(input().strip())
    # for _ in range(m):
    #     s = input().strip()
    #     res = biggerIsGreater(s)
    #     print(res)
    print(biggerIsGreater("zalqxykemvzzgaka"))