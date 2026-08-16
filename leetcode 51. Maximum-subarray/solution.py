class Solution(object):
    def maxSubArray(self, nums):

        # Store the maximum sum found so far
        # Start with -infinity because all numbers can be negative
        maxi = float('-inf')

        # Store the sum of the current subarray
        total = 0

        # Go through every element
        for i in range(len(nums)):

            # Add current element to current subarray
            total = total + nums[i]

            # Update maximum sum if current sum is bigger
            maxi = max(maxi, total)

            # If current sum becomes negative,
            # it will hurt the next subarray
            # so start fresh from the next element
            if total < 0:
                total = 0

        # Return the maximum subarray sum
        return maxi


''' DRY RUN 
Take:

nums = [-2,1,-3,4,-1,2,1,-5,4]

Initially:

total = 0
maxi = -∞
i = 0
num = -2


total = 0 + (-2)
      = -2

Update:

maxi = max(-∞, -2)
     = -2

Now:

total < 0

So:

total = 0
i = 1
num = 1


total = 0 + 1
      = 1


maxi = max(-2, 1)
     = 1

total is positive, so don't reset.

total = 1
i = 2
num = -3


total = 1 + (-3)
      = -2


maxi = max(1, -2)
     = 1

Now:

total < 0

So:

total = 0
i = 3

Now we see:

4

Since we reset total to 0:

total = 0 + 4
      = 4


maxi = max(1, 4)
     = 4
Continue
num = -1
total = 4 + (-1) = 3
maxi = 4
num = 2
total = 3 + 2 = 5
maxi = 5
num = 1
total = 5 + 1 = 6
maxi = 6
num = -5
total = 6 - 5 = 1
maxi = 6
num = 4
total = 1 + 4 = 5
maxi = 6

Final:

maxi = 6

So:

Answer = 6  '''
