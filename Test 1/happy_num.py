def isHappy(self, n: int) -> bool:
    ctn = 0
    while ctn<10**4:
        temp = 0
        while n:
            digit = n%10
            temp += (digit**2)
            n = n//10
        n = temp
        if n==1:
            return True
        ctn+=1
    return False