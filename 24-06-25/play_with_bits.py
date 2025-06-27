def cal(n):
    total_set = 0
    pow_2 = 2
    st = ""
    for i in range(32):
        whole_pair = (n+1)//pow_2
        # total_set += whole_pair*pow_2//2
        temp = (n+1)%pow_2
        if pow_2 == 2:
            st += "1" if whole_pair%2 else "0"
            pow_2 *= 2
            continue
        if temp <= pow_2//2:
            st+="0"
        else:
            st += "1" if temp%2 else "0"
        # total_set += max(0,temp-pow_2//2)
        pow_2 *= 2
    return st[::-1]
    # return int(st[::-1], 2)

print(cal(2),' ',cal(4))
