class Solution:
    def threeSum(self, nums):
        # 1. sort the nums list
        nums = sorted(nums)

        result = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                # To avoid duplicates
                continue
            # if nums[i] != nums[i - 1]
            # => find_two_sum from (i + 1) -> (len(nums) - 1 ) target is -current number
            self.find_two_sum(nums, i + 1, len(nums) - 1, -nums[i], result)

        return result
    
    def find_two_sum(self, nums, left, right, target, result):
        # create a variable for the pair that equals to target which is -nums[i]
        last_pair = None
        while left < right:
            # find if left + right equals to target
            if(nums[left] + nums[right] == target):
                # check if the left and right is duplicated
                if([nums[left], nums[right]] != last_pair):
                    # append -target, nums[left], and nums[right] to result
                    # target of find two sum is -nums so we have to convert the target to -target
                    result.append([-target, nums[left], nums[right]])
                # store the current nums[left], nums[right]
                last_pair = [nums[left], nums[right]]
                # move both pointer
                right -= 1
                left += 1
            elif(nums[left] + nums[right] > target):
                right -= 1
            else:
                left += 1
        return result