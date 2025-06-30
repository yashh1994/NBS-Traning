def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = set()
        for i in range(n-2):
            l,r = i+1,n-1
            if i>0 and nums[i] == nums[i-1]:
                continue
            while l<r:
                if nums[i]+nums[l]+nums[r] == 0:
                    ans.add((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
                elif nums[i]+nums[l]+nums[r] > 0:
                    r -= 1
                else:
                    l += 1
        return list(ans)