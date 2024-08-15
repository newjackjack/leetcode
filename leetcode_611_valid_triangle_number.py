class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # valid triangle: two edges is greater than the other edge
        # 1. Sort the nums array => O(n log n)
        nums.sort()
        
        # a variable to store count
        count = 0

        # loop through all the element in the nums aray
        for i in range(len(nums)):
            left = 0
            right = i - 1
            while left < right:
                if(nums[left] + nums[right] > nums[i]):
                    count += (right - left)
                    right -= 1
                else:
                    left += 1
        return count
