class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        hash_table = Counter(nums)
        for val, quantity in hash_table.items():
            if quantity > len(nums)/3:
                result.append(val)
        return result
