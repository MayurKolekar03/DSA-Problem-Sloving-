''' LeetCode: 238
Topic: Array
Pattern: Prefix + Suffix

Logic:
answer[i] = left product × right product

Pass 1:
Left → Right
Calculate prefix

Pass 2:
Right → Left
Calculate suffix

Time: O(n)
Space: O(1) extra ''' 

class Solution:
    def productExceptSelf(self, nums):

        # Create answer array filled with 1
        # This array will store our prefix products first
        answer = [1] * len(nums)

        # prefix stores product of elements
        # that are on the LEFT side
        prefix = 1

        # Go from LEFT to RIGHT
        for i in range(len(nums)):

            # Store product of all elements
            # before nums[i]
            answer[i] = prefix

            # Add current element to prefix
            prefix = prefix * nums[i]

        # suffix stores product of elements
        # that are on the RIGHT side
        suffix = 1

        # Go from RIGHT to LEFT
        for i in range(len(nums) - 1, -1, -1):

            # answer[i] currently contains LEFT product
            # Multiply it with RIGHT product
            answer[i] = answer[i] * suffix

            # Add current element to suffix
            suffix = suffix * nums[i]

        # Return final answer
        return answer
