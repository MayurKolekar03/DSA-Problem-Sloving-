class Solution:
    def removeDuplicates(self, nums):

        # k tells us where we should put the next unique element
        # First element is always unique, so start k from 1
        k = 1

        # Start checking from index 1
        # Because index 0 is already considered unique
        for i in range(1, len(nums)):

            # Compare current element with the last unique element
            # nums[k - 1] = last unique element
            if nums[i] != nums[k - 1]:

                # We found a new unique element
                # Put it at position k
                nums[k] = nums[i]

                # Move k forward for the next unique element
                k += 1

        # k represents the total number of unique elements
        return k
