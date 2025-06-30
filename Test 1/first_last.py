def searchRange(self, nums: List[int], target: int) -> List[int]:
        st = -1
        l,r = 0,len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                st = mid
                r = mid-1
            elif nums[mid] > target:
                r = mid-1
            else:
                l = mid+1
        print("Starting is ",st)
        if st == -1:
            return [-1,-1]
        ed = -1
        l,r = 0,len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                ed = mid
                l = mid+1
            elif nums[mid] > target:
                r = mid-1
            else:
                l = mid+1
        return [st,ed]