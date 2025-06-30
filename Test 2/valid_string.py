from collections import defaultdict
def isValid(s):
    if go(s):
        return "YES"
    return "NO"
    
def go(s):
    mp = defaultdict(int)
    for c in s:
        mp[c] += 1
    print("MP1: ",mp)
    mp2 = defaultdict(int)
    for k,v in mp.items():
        mp2[v]+=1

    print("MP2: ",mp2,' ')
    if len(mp2) > 2:
        return False
    if len(mp2) == 1:
        return True
    li = list(mp2.items())
    print("List: ",li)
    (k1,v1) = li[0]
    (k2,v2) = li[1]
    if v1 == 1:
        if k1-k2 == 1 or k1 == 1:
            return True
    elif v2 == 1:
        if k2-k1 == 1 or k2 == 1:
            return True
    return False  
