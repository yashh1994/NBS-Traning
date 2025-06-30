def movingTiles(l, s1, s2, queries):
    speed_diff = abs(s1-s2)
    ans = []
    for q in queries:
        mini_l = q**0.5
        rem_l = l-mini_l
        dis = (2**0.5)*rem_l
        ans.append((dis/speed_diff))
    return ans

