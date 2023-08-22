class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        multi = 1
        guaranteed_nums = [1] * len(nums)
        for i in range(len(nums)):
            guaranteed_nums[i] *= multi
            multi *= nums[i]
        
        multi = 1
        for i in range(len(nums)-1,-1,-1):
            guaranteed_nums[i] *= multi
            multi *= nums[i]
        return guaranteed_nums
