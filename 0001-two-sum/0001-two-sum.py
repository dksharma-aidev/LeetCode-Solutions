class Solution(object):
    def twoSum(self, nums, target):
        d = {}     #using dsa
        for i in range(len(nums)):
            answer = target - nums[i]
            if answer in d:
                return [d[answer], i]
            else:
                d[nums[i]] = i    
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        