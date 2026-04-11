'''
136. Single Number
S
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]

Output: 1


'''
from collections import Counter #import counter 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)# converts it to number and its frequency
        for num, freq in count.items(): #num is the number while freq is the amount of times the word showed
            if freq == 1: #if it appears one
                return num# #return the number
        return