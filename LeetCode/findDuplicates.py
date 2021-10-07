class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        duplicates = []
        for index in range(n):
            if nums[abs(nums[index]) - 1 < 0:
                duplicates.append(abs(nums[index]))
            else:
                nums[abs(nums[index]) - 1] *= -1
        return duplicates
