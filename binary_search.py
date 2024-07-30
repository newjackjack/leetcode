from typing import (List)
"""
Given a sorted array (ascending order) and a target number, find the first index of this number in 
O(logn) time complexity.
If the target number does not exist in the array, return -1.

ex1 = [1,4,4,5,7,7,8,9,9,10]
target = 1

walk-thru:
start = 0, end = len(nums) - 1, mid = (start + end)//2
Iteration 1:
start = 0, end = 9, mid = 4
[1,4,4,5,7,7,8,9,9,10]
 ^       ^          ^
 s      mid         e
 
nums[mid] is not less than target:
    end = mid

[1,4,4,5,7,7,8,9,9,10]
 ^       ^
 s       e
 
Iteration 2:
start = 0, end = 4, mid = 2
[1,4,4,5,7,7,8,9,9,10]
 ^   ^   ^
 s  mid  e
nums[mid] is not less than target
    end = mid

Iteration 3:

start = 0, end = 2, mid = 1
[1,4,4,5,7,7,8,9,9,10]
 ^ ^ ^
 s m e
 
 nums[mid] is not less than target
    end = mid

Iteration 4:

start = 0, end = 1, mid = 0
[1,4,4,5,7,7,8,9,9,10]
 ^ ^ 
 mse
nums[mid] is equal to target
    end = mid

"""


def binary_search_find_first(nums: List[int], target: int) -> int:
    # check if input list is valid
    if not nums:
        return -1

    start = 0
    end = len(nums) - 1

    while (start + 1 < end):
        mid = (start + end) // 2
        # if mid is less than target => make the start to mid and keep finding
        if (nums[mid] < target):
            start = mid
        # else => make the end to mid
        elif (nums[mid] == target):
            end = mid
        else:
            end = mid

    if (nums[start] == target):
        return start
    if (nums[end] == target):
        return end
    return -1


example1 = [1, 4, 4, 5, 7, 7, 8, 9, 9, 10]

print("First target: ", binary_search_find_first(example1, 7))

"""
Find the last position:
Find the last position of a target number in a sorted array. Return -1 if target does not exist.
Input: nums = [1,2,2,4,5,5], target = 2
Output: 2
Input: nums = [1,2,2,4,5,5], target = 6
Output: -1
"""


def binary_search_last_position(nums: List[int], target: int) -> int:
    # write your code here
    if not nums:
        return -1
    left = 0
    right = len(nums) - 1
    while (left + 1 < right):
        mid = (left + right)//2
        if (nums[mid] > target):
            right = mid
        else:
            left = mid
    if (nums[right] == target):
        return right
    if (nums[left] == target):
        return left
    return -1


print("Last target: ", binary_search_last_position(example1, 7))

"""
Find any position of a target number in a sorted array. Return -1 if target does not exist.
Input: nums = [1,2,2,4,5,5], target = 2
Output: 1 or 2

Input: nums = [1,2,2,4,5,5], target = 6
Output: -1

"""


def findPosition(nums, target):
    # write your code here
    if not nums:
        return -1
    start = 0
    end = len(nums) - 1
    while (start + 1) < end:
        mid = (start + end)//2
        if (nums[mid] < target):
            start = mid
        else:
            end = mid
    if (nums[start] == target):
        return start
    if (nums[end] == target):
        return end
    return -1


print("Find positions for all targets: ", findPosition(example1, 7))

"""
Maximum Number in Mountain Sequence
Given a mountain sequence of n integers which increase firstly and then decrease, find the mountain top(Maximum).
Input: nums = [1, 2, 4, 8, 6, 3], 
Output: 8
Input: nums = [10, 9, 8, 7], 
Output: 10
"""


def mountain_sequence(nums: List[int]) -> int:
    # write your code here
    if not nums:
        return -1
    left = 0
    right = len(nums) - 1
    while (left + 1 < right):
        mid = (left + right)//2
        if (nums[mid] > nums[mid + 1]):
            right = mid
        else:
            left = mid
    return max(nums[left], nums[right])
print("Mountain sequence: ", mountain_sequence([1, 2, 4, 8, 6, 3]))
