def findPeakElement(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        n = len(nums)
        if len(nums) == 1:
            return 0
        while l<=r:
            mid = (l+r)//2
            if mid+1 == n:
                return r
            if nums[mid] < nums[mid+1]:
                l = mid+1
            else:
                r = mid-1
        return l