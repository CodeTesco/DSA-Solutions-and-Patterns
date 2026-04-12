'''
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
'''

class Solution:  # Define a class for the solution
    def moveZeroes(self, nums: List[int]) -> None:  # Function modifies array in-place
        left = 0  # Pointer to place the next non-zero element
        
        for right in range(len(nums)):  # Traverse the array with right pointer
            if nums[right] != 0:  # If current element is not zero
                nums[left], nums[right] = nums[right], nums[left]  # Swap non-zero with left position
                left += 1  # Move left pointer forward
'''
Walkthrough Example
Input:
nums = [0,1,0,3,12]
Start:
left = 0
nums = [0,1,0,3,12]
Step 1: right = 0
nums[0] = 0 → skip
nums = [0,1,0,3,12]
left = 0
Step 2: right = 1
nums[1] = 1 (non-zero)
swap nums[0] and nums[1]
nums = [1,0,0,3,12]
left = 1
Step 3: right = 2
nums[2] = 0 → skip
nums = [1,0,0,3,12]
left = 1
Step 4: right = 3
nums[3] = 3 (non-zero)
swap nums[1] and nums[3]
nums = [1,3,0,0,12]
left = 2
Step 5: right = 4
nums[4] = 12 (non-zero)
swap nums[2] and nums[4]
nums = [1,3,12,0,0]
left = 3
Final Output:
[1,3,12,0,0]
Time Complexity: O(n)
Space Complexity: O(1)
'''