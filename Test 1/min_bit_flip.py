def minBitFlips(self, start: int, goal: int) -> int:
        xor = start ^ goal
        ans = 0
        for c in bin(xor)[2:]:
            if int(c):
                ans += 1
        return ans