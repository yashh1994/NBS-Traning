def countPrimes(self, n: int) -> int:
        mp = {}
        for i in range(2,n):
            if i not in mp:
                mp[i] = True
                temp = i*i
                while temp<=n:
                    mp[temp] = False
                    temp += i
                    # print("Temp: ",temp)
        ans = 0
        for k,v in mp.items():
            if v:
                ans += 1
        # print(mp)
        return ans