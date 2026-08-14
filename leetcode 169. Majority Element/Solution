class Solution:
    def majorityElement(self, nums):

        # candidate = current possible majority element
        candidate = None

        # count = strength of the candidate
        count = 0

        # Go through every number in the array
        for num in nums:

            # If count becomes 0,
            # choose the current number as our new candidate
            if count == 0:
                candidate = num

            # If current number is same as candidate,
            # increase its strength
            if num == candidate:
                count += 1

            # If current number is different,
            # decrease candidate's strength
            else:
                count -= 1

        # Majority element is guaranteed to exist,
        # so candidate will be the answer
        return candidate
        
