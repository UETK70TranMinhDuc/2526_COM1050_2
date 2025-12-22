class Solution(object):
    def searchRange(self, nums, target):
        a=[-1,-1]
        b=[]
        if target not in nums:
            return a
        for i in range(len(nums)):
            if nums[i]==target:
                b.append(i)
        return [min(b),max(b)]
        