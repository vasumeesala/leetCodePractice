"""
https://leetcode.com/problems/search-insert-position/


Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4



"""

from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) -1
    while left <= right:
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        elif target >= nums[mid]:
            left = mid+1
        else:
            right = mid-1
    return left

