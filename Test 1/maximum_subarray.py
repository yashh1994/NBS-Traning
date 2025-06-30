def maxSubArray(self, nums: List[int]) -> int:
        cur_sm = -10000
        mx_sm = -10000
        for n in nums:
            mx_sm = max(mx_sm,cur_sm)
            cur_sm = max(cur_sm+n,n)
        mx_sm = max(cur_sm,mx_sm)
        return mx_sm