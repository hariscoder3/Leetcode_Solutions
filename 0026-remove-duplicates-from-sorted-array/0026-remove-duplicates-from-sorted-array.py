class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        # Initialize the pointer for unique elements
        unique_pointer = 0

        # Iterate through the array
        for i in range(1, len(nums)):
            # Check if the current element is different from the previous one
            if nums[i] != nums[unique_pointer]:
                # Move the unique pointer forward
                unique_pointer += 1
                # Update the unique element at the pointer
                nums[unique_pointer] = nums[i]

        return unique_pointer + 1
