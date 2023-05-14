"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.



Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

https://leetcode.com/problems/sort-colors/




"""

from typing import List

def sortColors(nums: List[int]) -> None:
    left, right, i = 0, len(nums)-1, 0
    while i <= right:
        if nums[i] == 0:
            nums[left], nums[i] = nums[i], nums[left]
            left += 1
        elif nums[i] == 2:
            nums[right], nums[i] = nums[i], nums[right]
            right -= 1
            i -= 1
        i += 1
    return nums
print(sortColors([2,0,2,1,1,0]))




