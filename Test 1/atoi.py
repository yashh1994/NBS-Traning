def myAtoi(self, s: str) -> int:
        MAX = 2**31 - 1
        MIN = -2**31
        n = len(s)
        i = 0
        if not s:
            return 0
        while i < n and s[i] == ' ':
            i += 1
        if i == n:
            return 0
        sig="+"
        st = i
        if s[i] in ['+','-']:
            sig = s[i]
            st = i+1
        val = 0
        for i in range(st,n):
            if not s[i].isdigit():
                break
            nm = int(s[i])
            val *= 10
            val += nm
        return max(-val,MIN) if sig == '-' else min(val,MAX) 
            
        