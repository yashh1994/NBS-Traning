n = 15
total_set = 0
pow_2 = 2
for i in range(32):
    whole_pair = (n+1)//pow_2
    total_set += whole_pair*pow_2//2
    temp = whole_pair%pow_2
    total_set += max(0,temp-pow_2//2)
    pow_2 *= 2
print(total_set)
