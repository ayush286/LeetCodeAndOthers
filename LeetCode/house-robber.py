class Solution(object):
    # O(n) Time | O(1) Space where n is length of nums
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        chosen = None
        notChosen = None
        for loot in nums:
            if chosen is None:
                chosen = loot
                notChosen = 0
                continue
            newChosen = notChosen + loot
            newNotChosen = max(chosen, notChosen)
            chosen = newChosen
            notChosen = newNotChosen
        return max(chosen, notChosen)
        
