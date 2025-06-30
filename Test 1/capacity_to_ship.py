def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(limit):
            d = 1
            cur = 0
            for w in weights:
                if cur+w <= limit:
                    cur += w
                elif w > limit:
                    return False
                else:
                    cur = w
                    d += 1
            return d <= days




        l,r = 0,sum(weights)
        ans = 0
        while l<=r:
            mid = (l+r)//2
            if check(mid):
                ans = mid
                r = mid-1
                # print("Got at: ",mid,"got to left side")
            else:
                l = mid+1    
                # print("not at: ",mid,"got to right side")
        
        # print(check(13))
        return ans
        