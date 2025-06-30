def countGoodNumbers(self, n: int) -> int:
    def pow(a,n,mod):
        if n == 0:
            return 1
        elif n == 1:
            return a
        elif not n%2:
            temp = pow(a,n//2,mod)%mod
            return temp**2
        else:
            temp = pow(a,n//2,mod)%mod
            return a*(temp**2)
    MOD = 10**9 + 7
    odd_l = n//2
    even = (n+1)//2
    odd = pow(4,odd_l,MOD)
    even = pow(5,even,MOD)
    # print(pow(2,5,10))
    return (odd*even)%MOD