class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r=0,len(nums)-1
        nums.sort()
        while l<r:
            if -nums[l]==nums[r]:
                return nums[r]
            elif -nums[l]>nums[r]:
                l+=1
            else:
                r-=1
        return -1
